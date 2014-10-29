import arcpy
from arcpy import env
env.workspace = "F:/UWTacoma/GIS_501_AU_2014/lab_4/data/Exercise05"
arcpy.AddXY_management("hospitals.shp")

