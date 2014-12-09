import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "F:/UWTacoma/GIS_501_AU_2014/lab_4/data/Exercise07/"
fc = "airports.shp"
delimitedField = arcpy.AddFieldDelimiters(fc, "FEATURE")
cursor = str(arcpy.da.SearchCursor(fc,"FEATURE", delimitedField +" = \'Airport\'"))
if row in cursor:
    unique_name = arcpy.CreateUniqueName("Results/airport_buffer.shp")
    arcpy.Buffer_analysis(fc, unique_name, "15000 METERS")    
else:
    unique_name = arcpy.CreateUniqueName("Results/seaplane_buffer.shp")
    arcpy.Buffer_analysis(fc, unique_name, "7500 METERS")
