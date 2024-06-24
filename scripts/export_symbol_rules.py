import arcpy
import json
import logging
import pandas as pd

# https://pro.arcgis.com/en/pro-app/latest/arcpy/data-access/searchcursor-class.htm


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

        ## Layer Validation
        if l.supports("DefinitionQuery"):
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
                # heading = list(map(str.strip, grp.heading.split(",")))
                headings = [v.strip() for v in grp.heading.split(",")]
                logging.debug(f"   {headings}")
                dd["headings_alias"] = headings
                dd["headings"] = [fields.get(f) for f in headings]
                dd["labels"] = []
                dd["values"] = []
                for itm in grp.items:
                    logging.debug(f"   {itm.label}")
                    logging.debug(f"   {itm.values}")
                    dd["labels"].append(itm.label)
                    cleaned_list = [
                        [None if item == "<Null>" else item for item in sublist]
                        for sublist in itm.values
                    ]

                    logging.debug(cleaned_list)
                    dd["values"].append(cleaned_list)
            try:
                d["renderer"] = dd
            except Exception as e:
                logging.error(f"Cannot add symbology: {l.name}: {e}")
        else:
            logging.error(f"Layer {l.name}: {sym.renderer.type}")
            return d

    return d
