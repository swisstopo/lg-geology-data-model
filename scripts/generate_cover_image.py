import json
import random
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image
from rich.console import Console
from shapely.geometry import Point, shape

console = Console()

(
    "hillshade,bedrock,unconsolidated,surfaces,tecto_lines,linear_features,point_features",
)

# --- Configuration ---
# --- Configuration ---
WMS_URL = "https://wms.dubious.cloud"
BASE_LAYER = "hillshade"
GEO_LAYERS = (
    "bedrock,unconsolidated,surfaces,tecto_lines,linear_features,point_features"
)

WIDTH, HEIGHT = 1000, 600
SCALE = 12000  # 20000
EPSG = "EPSG:2056"
OVERLAY_OPACITY = 0.6  # 0.0 (invisible) to 1.0 (opaque)

OUTPUT_DIR = Path("assets")


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


def fetch_wms(layers, bbox_str, transparent="FALSE"):
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
    res = requests.get(WMS_URL, params=params, timeout=30)
    res.raise_for_status()
    return Image.open(BytesIO(res.content)).convert("RGBA")


# --- Process ---
try:
    # 1. Setup Coordinates
    cx, cy, px_m = get_random_location(
        "../mapserver-geocover/data/ch.geojson", SCALE, WIDTH, HEIGHT
    )
    hw, hh = (WIDTH * px_m) / 2, (HEIGHT * px_m) / 2
    bbox_str = f"{cx - hw},{cy - hh},{cx + hw},{cy + hh}"

    print(f"Fetching layers for BBox: {bbox_str}")

    # 2. Fetch Base (Hillshade) and Overlay (Geology)
    # Hillshade doesn't need transparency; Geology definitely does
    background = fetch_wms(BASE_LAYER, bbox_str, "FALSE")
    overlay = fetch_wms(GEO_LAYERS, bbox_str, "TRUE")

    # 3. Apply custom transparency to the overlay
    # We modify the alpha channel: new_alpha = old_alpha * OVERLAY_OPACITY
    alpha = overlay.getchannel("A")
    alpha = alpha.point(lambda i: int(i * OVERLAY_OPACITY))
    overlay.putalpha(alpha)

    # 4. Composite the images
    # alpha_composite handles the transparency math correctly
    final_img = Image.alpha_composite(background, overlay)

    # final_img.show()
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = OUTPUT_DIR / f"geocover_{timestamp}.png"

    final_img.save(filename)
    print(f"Success! Composite image saved to {filename}.")

except Exception as e:
    print(f"Failed to generate image: {e}")
