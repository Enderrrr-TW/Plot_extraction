from numba import njit, types, vectorize, prange
import numpy as np
import laspy
import time
import pandas as pd
import geopandas as gpd
import random
import matplotlib.pyplot as plt
import json
import gdal
import glob
from shapely.geometry import MultiPolygon ,Polygon
import cv2

shp=gpd.read_file('./shp/corners_htma_inverted_modified.shp')
# print(shp['geometry'][0].exterior.coords.xy[0][0]) #x1
print(shp['geometry'][0].exterior.coords.xy)
g=shp['geometry']
csv=dict()
csv['x1']=[]
csv['y1']=[]
csv['x2']=[]
csv['y2']=[]
csv['x3']=[]
csv['y3']=[]
csv['x4']=[]
csv['y4']=[]
for i in range(len(shp['geometry'])):
    csv['x1'].append(g[i].exterior.coords.xy[0][0])
    csv['x4'].append(g[i].exterior.coords.xy[0][1])
    csv['x2'].append(g[i].exterior.coords.xy[0][2])
    csv['x3'].append(g[i].exterior.coords.xy[0][3])
    csv['y1'].append(g[i].exterior.coords.xy[1][0])
    csv['y4'].append(g[i].exterior.coords.xy[1][1])
    csv['y2'].append(g[i].exterior.coords.xy[1][2])
    csv['y3'].append(g[i].exterior.coords.xy[1][3])
df=pd.DataFrame(csv)
df.to_csv('Karoll_modified.csv')