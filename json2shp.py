import numpy as np
import pandas as pd
import geopandas as gpd
import json
from shapely.geometry import MultiPolygon ,Polygon

# rec=pd.read_csv('rectangles.csv')
with open('H:/plot_extraction/ACRE/test2.json') as j:
    points=json.load(j)['shapes']#[0]['points']
    # [[671.0, 566.0], [746.0, 925.0]] An example of the way how json records rectangle
# print(points[0][0])
n= len(points) #number of rectangles
p_lsit=[]
rec=dict()
rec['x1']=[]
rec['x2']=[]
rec['x3']=[]
rec['x4']=[]
rec['y1']=[]
rec['y2']=[]
rec['y3']=[]
rec['y4']=[]
for i in range(n):
    x1=points[i]['points'][0][0]
    y1=points[i]['points'][0][1]
    x3=points[i]['points'][1][0]
    y3=points[i]['points'][1][1]
    x2=x3
    y2=y1
    x4=x1
    y4=y3
    rec['x1'].append(x1)
    rec['x2'].append(x2)
    rec['x3'].append(x3)
    rec['x4'].append(x4)
    rec['y1'].append(y1)
    rec['y2'].append(y2)
    rec['y3'].append(y3)
    rec['y4'].append(y4)
    p_lsit.append(Polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)]))
shp=MultiPolygon(p_lsit)
features=[i for i in range(n)] # shp ID=0-49
f=gpd.GeoDataFrame({'feature':features,'geometry':shp})
f.to_file('H:/plot_extraction/ACRE/test2.shp')
rec=pd.DataFrame(rec)
rec.to_csv('H:/plot_extraction/ACRE/test2.csv',index=False)