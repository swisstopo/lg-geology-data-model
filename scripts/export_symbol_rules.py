import arcpy
import json
import logging
import pandas as pd

# https://pro.arcgis.com/en/pro-app/latest/arcpy/data-access/searchcursor-class.htm

"""logging.basicConfig(filename='used_symbols.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)"""

logging.basicConfig(
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)

MAPSHEET_LAYER = "Mapsheet"


def arcgis_table_to_df(in_fc, input_fields=None, query="", spatial_filter=None):
    OIDFieldName = arcpy.Describe(in_fc).OIDFieldName
    available_fields = [field.name for field in arcpy.ListFields(in_fc)]
    logging.debug(available_fields)
    logging.debug(input_fields)
    if input_fields:
        final_fields = list(set([OIDFieldName] + input_fields) & set(available_fields))
    else:
        final_fields = available_fields
    logging.debug("Intersection:", final_fields)
    data = [
        row
        for row in arcpy.da.SearchCursor(
            in_fc,
            final_fields,
            where_clause=query,
            spatial_filter=spatial_filter,
            search_order="SPATIALFIRST",
        )
    ]
    fc_dataframe = pd.DataFrame(data, columns=final_fields)
    fc_dataframe = fc_dataframe.set_index(OIDFieldName, drop=True)
    return fc_dataframe


def process_layers(l):
    """if l.isGroupLayer:
    for sublayer in l.listLayers():
        process_layers(sublayer, d=d)"""
    d = {"renderer": {}, "query_defn": {}}
    if l.isFeatureLayer:
        sym = l.symbology
        renderer = sym.renderer

        d["renderer"]["type"] = sym.renderer.type

        logging.debug(f"--- {l.name} ---")
        ## Layer Validation
        if l.supports("DEFINITIONQUERY"):
            # Lists Definition Queries
            dfn = []
            query = l.listDefinitionQueries()
            # List Dictionary
            for dic in query:
                for key, value in dic.items():
                    logging.debug(key, value)
                    dfn.append({key: value})
            d["query_defn"] = dfn

        fields = {}
        for fld in arcpy.Describe(l).fields:
            fields[fld.aliasName] = fld.name

        if hasattr(renderer, "groups"):
            for grp in renderer.groups:
                dd = {}
                heading = list(map(str.strip, grp.heading.split(",")))
                headings = [v.strip() for v in grp.heading.split(",")]
                logging.debug(f"   {headings}")
                dd["headings_alias"] = headings
                dd["headings"] = [fields.get(f) for f in headings]
                dd["labels"] = []
                dd["values"] = []
                for itm in grp.items:
                    # print(itm)
                    logging.debug(f"   {itm.label}")
                    # print(f"   {itm.symbol}")
                    logging.debug(f"   {itm.values}")
                    dd["labels"].append(itm.label)
                    dd["values"].append(itm.values)
            d["renderer"] = dd
        else:
            logging.error(f"Layer {l.name}: {sym.renderer.type}")

    return d


"""def query_layer(fc, bbox, fields):
    with arcpy.da.SearchCursor(
        fc, fields, spatial_filter=bbox, search_order="SPATIALFIRST"
    ) as cursor:
        for row in cursor:
            logging.debug(f"{row[0]}: {row[1]}")


def get_mapsheet_shape(mapsheet_lyr, mapsheet_name):
    for bbox in [
        (row[0], row[1])
        for row in arcpy.da.SearchCursor(mapsheet_lyr, ["SHAPE@", "MSH_MAP_TITLE"])
    ]:
        shp, name = bbox
        if name == mapsheet_name:
            return shp

    return None


def count_features(l, map_shp, input_fields):
    try:
        available_fields = [field.name for field in arcpy.ListFields(l)]

        available_fields_alias = [field.aliasName for field in arcpy.ListFields(l)]
        OIDFieldName = arcpy.Describe(l).OIDFieldName
        final_fields = list(set([OIDFieldName] + input_fields) & set(available_fields))

        df = arcgis_table_to_df(l, input_fields=final_fields, spatial_filter=map_shp)

        # df[(df['Gender']=='Male') & (df['Year']==2014)]

        return df

    except RuntimeError as e:
        logging.error(f"Error while counting inf layer={l.name}: {e}")


def filter_attributes(df, attr):
    logging.info(json.dumps(attr, indent=4))
    renderer = attr["renderer"]
    columns = renderer["headings"]

    logging.info(f"columns: {columns}, df {df.columns}")

    filter_criteria = []

    for v in renderer.get("values"):
        filter_criteria.append(zip(columns, v))

    # Example filter criteria: list of (column, value) pairs
    # filter_criteria = [('A', 1), ('B', 5)]

    results = {}

    for criteria in filter_criteria:
        # Create the filter expression dynamically
        filter_expression = pd.Series([True] * len(df))

        for column, value in criteria:
            filter_expression = filter_expression & (df[column] == value)

        # Apply the filter
        filtered_df = df[filter_expression]

        # Store the count and the matching rows
        results[tuple(criteria)] = {"count": len(filtered_df), "rows": filtered_df}

    # Print the results
    for criteria, result in results.items():
        print(f"\nFilter Criterion: {criteria}")
        print(f"Count: {result['count']}")
        print("Matching Rows:")
        print(result["rows"])"""


def main():
    # Define the path to your ArcGIS Pro project
    fc = "Mapsheet"
    fields = ["OBJECTID", "MSH_MAP_TITLE", "MSH_MAP_NBR"]
    try:
        aprx = arcpy.mp.ArcGISProject("CURRENT")
    except OSError as e:
        logging.error(e)
        project_path = r"D:\ArcGIS\GOTOP\GOTOP\GOTOP.aprx"

        # Open the ArcGIS Pro project
        aprx = arcpy.mp.ArcGISProject(project_path)

    m = aprx.listMaps()[0]
    fc = "GC_Pro_@Default_I\Point_Objects\Point Objects_Erraticker"
    input_fields = ["OBJECTID", "KIND"]

    mapsheet_lyr = None

    for l in m.listLayers():
        if MAPSHEET_LAYER in l.name:
            mapsheet_lyr = l

    map_shp = get_mapsheet_shape(mapsheet_lyr, "Bivio")

    res = {}
    for l in m.listLayers():
        if MAPSHEET_LAYER not in l.name and l.isFeatureLayer:
            df = count_features(l, map_shp, input_fields)
            feat_count = len(df) if df is not None else 0

            logging.info(f"\n--- {l.name} {feat_count}---")

            attributes = process_layers(l)

            res[l.name] = attributes

            if "Quelle" in l.name:
                logging.info("######## Filtering ##############")
                # filter_attributes(df, attributes)

    with open("used_symbols.json", "w") as f:
        f.write(json.dumps(res, indent=4))


if __name__ == "__main__":
    main()
