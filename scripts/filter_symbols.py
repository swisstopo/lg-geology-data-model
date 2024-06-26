import os
import sys
import json
import geopandas as gpd
import pandas as pd
import logging
import re
import click
from datetime import datetime

from shapely.geometry import box


gpd.options.io_engine = "pyogrio"

GDB_PATH = "/media/marco/G12/GEODATA/20240503_0300_2030-12-31.gdb"


USED_SYMBOLS_PATH = "layer_used_symbols.json"

layername = "GC_POINT_OBJECTS"

bivio = box(2760000, 1146000, 2777500, 1158000)
vals = box(2725000, 1158000, 2742500, 1170000)

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def cleanup(x):
    if x == "<Null>" or x is None:
        return 0
    else:
        return int(x)


def clean_headings(headings):
    if headings is None or None in headings:
        logging.error(f"No headings {headings}")
        return None
    else:
        headings = list(map(get_last_element, headings))
    logging.info(f"    headings={headings}")

    return headings


def filter_from_criteria(data, gdf):
    headings = data.get("headings")

    values = data.get("values")
    labels = data.get("labels")

    headings = clean_headings(headings)

    filter_criteria = zip(labels, values)

    filters = []
    results = {}

    for criteria in filter_criteria:
        logging.info(f"\nApplying criteria: {criteria}")

        # Start with a True series to filter
        filter_expression = pd.Series([True] * len(df), index=df.index)

        for column, value in criteria:
            # Update the filter expression for each (column, value) pair
            filter_expression &= df[column] == value
            logging.info(f"Filter status for ({column} == {value}):")
            logging.info(filter_expression)
            logging.info(f"Matching rows count: {filter_expression.sum()}")

        filters.append(filter_expression)



    '''for criterion in filter_criteria:
        label, values = criterion
        # Create the filter expression dynamically

        for value in values:
            filter_expression = pd.Series([True] * len(gdf))
            for i, head in enumerate(headings):
                filter_expression = filter_expression & (gdf[head] == cleanup(value[i]))
        filters.append(filter_expression)'''

    return filters


def get_last_element(s):
    if s is None:
        return s
    elements = s.split(".")
    return elements[-1]


def process_layer(layername, gdf, data, all_value=True):
    results = {}

    headings = data.get("headings")
    logging.debug(headings)

    values = data.get("values")
    labels = data.get("labels")

    if headings is None or None in headings:
        logging.error(f"No headings found for {layername}: {headings}")
        return results
    else:
        headings = list(map(get_last_element, headings))
    logging.debug(headings)
    if headings:
        logging.debug(headings)
        logging.debug(f"Before cleanup: {gdf.columns}")
        gdf = gdf[headings]

    gdf = gdf.fillna(0.0).astype(int)

    filters = filter_from_criteria(data, gdf)

    filter_criteria = zip(labels, values, filters)

    for filter_criterion in filter_criteria:
        label, values, filter_expression = filter_criterion

        # Apply the filter
        filtered_df = gdf[filter_expression]

        # Store the count and the matching rows
        results[label] = len(filtered_df)

        if len(filtered_df) > 0:
            logging.info(f"    {label}: {len(filtered_df)}")

    return {"rules": results}


def process_layers_symbols(layers, gdb_path, mask_geom):
    results = {}
    dataset = None

    for layername in layers.keys():
        logging.info(f"--- {layername} ---")
        data = layers.get(layername)
        logging.debug(data)

        datasource = data.get("dataSource")

        logging.info(f"datasource={datasource}")

        dataset = None
        m = re.findall(",Dataset=(.*)", datasource)
        if m and len(m) > 0:
            dataset = m[0].split(".").pop()

        # TTEC_LIM_TYP
        try:
            logging.info(f"    dataset={dataset}")
            renderer = data.get("renderer")
        except Exception as e:
            logging.error(f"    Cannot get renderer for {layername}: {e}")
            continue

        if dataset is None:
            logging.error(f"    No dataset found for {layername}")
            continue

        logging.info(dataset)
        bbox = mask_geom.boundary
        logging.debug(bbox)

        unfiltered_gdf = gpd.read_file(gdb_path, layer=dataset, bbox=bbox)

        gdf = unfiltered_gdf[unfiltered_gdf.intersects(mask_geom)]

        logging.debug(gdf)

        # TODO: this should be dynamic
        if "Bedrock_HARMOS" in layername:
            df = gpd.read_file(gdb_path, layer="GC_BED_FORM_ATT")

            gdf = gdf.merge(df, left_on="FORM_ATT", right_on="UUID")

            logging.debug(f"After merged cleanup: {gdf.head()}")
            logging.debug(f"After merged cleanup: {gdf.columns}")

        logging.debug(gdf.columns)

        rules = process_layer(layername, gdf, renderer)

        results[layername] = rules

    return results


def print_keys_with_non_null_subkey(dictionary, subkey):
    for key, value in dictionary.items():
        # Check if the value is a dictionary and the subkey exists with a non-null value
        if isinstance(value, dict) and subkey in value and value[subkey] is not None:
            logging.debug(key)


def _arg_split(ctx, param, value):
    # split columns by ',' and remove whitespace
    try:
        bbox = list(map(float, [c.strip() for c in value.split(",")]))
        # validate
        if len(bbox) != 4:
            raise ValueError("bbox must have four values")
    except ValueError as e:
        raise click.BadOptionUsage("resolution", f"--bbox: {e}")

    return bbox


# Define a function to configure the logging level
def configure_logging(level):
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {level}")
    logging.basicConfig(
        level=numeric_level, format="%(asctime)s - %(name)s - %(levelname)s %(message)s"
    )  # Initial configuration (if no handlers exist)
    logging.getLogger().setLevel(
        numeric_level
    )  # Set the root logger's level explicitly


@click.command()
@click.option(
    "-b",
    "--bbox",
    required=False,
    nargs=1,
    type=click.STRING,
    callback=_arg_split,
    default="2725000,1158000,742500,1170000",  # Vals
    help="bounding box to filter",
)
@click.option(
    "--gdb-path", type=click.Path(exists=True), default=GDB_PATH, help="GDB file"
)
@click.option(
    "-o",
    "--output",
    type=click.Path(exists=False),
    # default=USED_SYMBOLS_PATH,
    help="Used symbols file",
)
@click.option(
    "-l",
    "--log-level",
    default="INFO",
    type=click.Choice(
        ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=True
    ),
    help="Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
)
def main(bbox, gdb_path, output, log_level):
    configure_logging(log_level)

    dirname = os.path.dirname(__file__)
    config_json = os.path.join(dirname, "layer_symbols.json")
    now = datetime.now()

    results = {"bbox": bbox, "gdb_path": gdb_path, "datetime": now.isoformat()}

    extent = box(*bbox)

    with open(config_json, "r") as f:
        layers = json.load(f)

    results["layers"] = process_layers_symbols(layers, gdb_path, extent)

    if output is not None:
        logging.info(f"Writing to {output}")

        with open(output, "w", encoding="utf-8") as f:
            # Serialize the data and write it to the file
            json.dump(results, f, ensure_ascii=False, indent=4)
    else:
        print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()
