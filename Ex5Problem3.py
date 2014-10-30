import arcpy
from arcpy import env
env.workspace = "F:/UWTacoma/GIS_501_AU_2014/lab_4/data/Exercise05"
env.overwriteOutput = True
in_features = "parks.shp"
out_features = "Results/parks_Dis.shp"
dissolve_field = 'PARK_TYPE'
arcpy.Dissolve_management(in_features, out_features, dissolve_field, )
