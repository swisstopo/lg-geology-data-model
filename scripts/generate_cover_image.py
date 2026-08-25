import json
import random
import time
from datetime import datetime
from io import BytesIO
from pathlib import Path

import click
import requests
from PIL import Image, UnidentifiedImageError
from rich.console import Console
from shapely.geometry import Point, shape

console = Console()

# --- Configuration ---
WMS_URL = "https://wms.geolover.ch"
BASE_LAYER = "hillshade"
GEO_LAYERS = "bedrock,tecto_lines,unconsolidated,surfaces,linear_features,point_features"

WIDTH, HEIGHT = 1000, 600
SCALE = 12000  # random-location search extent, in map units
EPSG = "EPSG:2056"
OVERLAY_OPACITY = 0.6  # 0.0 (invisible) to 1.0 (opaque)

OUTPUT_DIR = Path("assets")
SWISS_BORDER_GEOJSON = "../mapserver-geocover/data/ch.geojson"


def get_random_location(geojson_path, scale, w, h):
    with open(geojson_path, "r") as f:
        swiss_border = shape(json.load(f)["geometry"])

    px_m = 0.00028 * scale
    margin = max(w * px_m, h * px_m) / 2
    safe_zone = swiss_border.buffer(-margin)

    minx, miny, maxx, maxy = safe_zone.bounds
    while True:
        pnt = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if safe_zone.contains(pnt):
            return pnt.x, pnt.y, px_m


def fetch_wms(layers, bbox_str, transparent="FALSE", retries=3):
    params = {
        "SERVICE": "WMS",
        "VERSION": "1.3.0",
        "REQUEST": "GetMap",
        "LAYERS": layers,
        "CRS": EPSG,
        "BBOX": bbox_str,
        "WIDTH": str(WIDTH),
        "HEIGHT": str(HEIGHT),
        "FORMAT": "image/png",
        "TRANSPARENT": transparent,
        "STYLES": "",
    }
    # The backend occasionally returns a truncated/broken PNG under load; a plain
    # retry clears it up almost every time, so don't fail the whole run over it.
    for attempt in range(1, retries + 1):
        res = requests.get(WMS_URL, params=params, timeout=30)
        res.raise_for_status()
        try:
            return Image.open(BytesIO(res.content)).convert("RGBA")
        except UnidentifiedImageError:
            if attempt == retries:
                raise
            console.print(
                f"[yellow]WMS returned a broken image for '{layers}' "
                f"(attempt {attempt}/{retries}), retrying...[/yellow]"
            )
            time.sleep(1)


def parse_bbox(ctx, param, value):
    if value is None:
        return None
    parts = value.split(",")
    if len(parts) != 4:
        raise click.BadParameter("must be 'minx,miny,maxx,maxy'")
    try:
        return tuple(float(p) for p in parts)
    except ValueError:
        raise click.BadParameter("all four values must be numbers")


@click.command()
@click.option(
    "--bbox",
    callback=parse_bbox,
    default=None,
    metavar="MINX,MINY,MAXX,MAXY",
    help="Fixed extent in EPSG:2056 meters. Skips the random-location search when given.",
)
@click.option(
    "--geojson",
    "geojson_path",
    default=SWISS_BORDER_GEOJSON,
    show_default=True,
    help="Swiss border geojson used to pick a random location (ignored with --bbox).",
)
def main(bbox, geojson_path):
    """Generate a GeoCover map extract PNG used as the docs cover figure."""
    try:
        if bbox:
            minx, miny, maxx, maxy = bbox
            bbox_str = f"{minx},{miny},{maxx},{maxy}"
        else:
            cx, cy, px_m = get_random_location(geojson_path, SCALE, WIDTH, HEIGHT)
            hw, hh = (WIDTH * px_m) / 2, (HEIGHT * px_m) / 2
            bbox_str = f"{cx - hw},{cy - hh},{cx + hw},{cy + hh}"

        console.print(f"[cyan]Fetching layers for BBox:[/cyan] {bbox_str}")

        # Hillshade doesn't need transparency; geology overlay definitely does
        background = fetch_wms(BASE_LAYER, bbox_str, "FALSE")
        overlay = fetch_wms(GEO_LAYERS, bbox_str, "TRUE")

        # Apply custom transparency to the overlay: new_alpha = old_alpha * OVERLAY_OPACITY
        alpha = overlay.getchannel("A")
        alpha = alpha.point(lambda i: int(i * OVERLAY_OPACITY))
        overlay.putalpha(alpha)

        final_img = Image.alpha_composite(background, overlay)

        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = OUTPUT_DIR / f"geocover_{timestamp}.png"

        final_img.save(filename)
        console.print(f"[green]Success![/green] Composite image saved to {filename}.")

    except Exception as e:
        console.print(f"[red]Failed to generate image:[/red] {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
