import arcpy
from arcpy import env
fcdesc=[]
env.workspace = "F:/UWTacoma/GIS_501_AU_2014/lab_4/data/Exercise06/"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    fcgeo = str(fcdesc.shapeType)
    print str(fcdesc.basename) + " is a " + fcgeo.lower() + " feature class"
