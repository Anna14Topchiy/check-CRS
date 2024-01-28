#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shapely.geometry import shape
import json
import os
from pyproj import Proj, transform
import geopandas as gpd


# Load lines from Shapefile
lines_gdf = gpd.read_file(r"C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\scrip_snap_points_to_line\nl_roads.shp")
points_gdf = gpd.read_file(r"C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\scrip_snap_points_to_line\merged_stop.geojson")
# Check the CRS of the loaded GeoDataFrame
print("Original CRS of lines_gdf:", lines_gdf.crs)
print("Original CRS of points_gdf:", points_gdf.crs)