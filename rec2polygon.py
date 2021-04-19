import geopandas as gpd
import pandas as pd
from shapely.geometry import MultiPolygon ,Polygon
rec=pd.read_csv('./result/median_008_10cm.csv')
p_lsit=[]
for i in range(len(rec['x1'])):
    p_lsit.append(Polygon([(rec['x1'][i],rec['y1'][i]),(rec['x2'][i],rec['y2'][i]),(rec['x3'][i],rec['y3'][i]),(rec['x4'][i],rec['y4'][i])]))
shp=MultiPolygon(p_lsit)
features=[i for i in range(len(rec['x1']))] # shp ID=0-49
f=gpd.GeoDataFrame({'feature':features,'geometry':shp})
f.to_file('./result/median_008_10cm.shp')