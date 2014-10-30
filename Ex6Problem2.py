import arcpy
from arcpy import env
fcdesc=[]
env.workspace = "F:/UWTacoma/GIS_501_AU_2014/lab_4/data/Exercise06/"
arcpy.CreateFileGDB_management("Results/", "NM.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    fcgeo = str(fcdesc.shapeType)
    if fcgeo == "Polygon":
        arcpy.CopyFeatures_management(fc, "F:/UWTacoma/GIS_501_AU_2014/lab_4/data/Exercise06/Results/NM.gdb/" + fcdesc.basename)
