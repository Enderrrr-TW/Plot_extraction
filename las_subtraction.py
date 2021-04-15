import laspy
import pandas as pd
import numpy as np
import geopandas as gpd

raw=las=laspy.file.File('./DSM/f54m_ground_points/20200702/LAS_UAV_Field54m_sbdtccal.las')
rawx=raw.x
rawy=raw.y 
rawz=raw.z
ground=laspy.file.File('./DSM/f54m_ground_points/20200702/ground_point_res2_buf_01_rig3.las')
groundx=ground.x
groundy=ground.y
groundz=ground.z

indexx=np.in1d(rawx,groundx)
indexy=np.in1d(rawy,groundy)
indexz=np.in1d(rawz,groundz)
indexxy=np.logical_and(indexx,indexy)
indexxyz=np.logical_and(indexxy,indexz)
index=np.logical_not(indexxyz)
new=laspy.file.File('./DSM/f54m_ground_points/20200702/20200702_F54N_nground_subset.las',mode='w',header=raw.header)
new.x=rawx[index]
new.y=rawy[index]
new.z=rawz[index]
new.close()
print(False in index)