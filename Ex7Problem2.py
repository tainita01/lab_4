import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "F:/UWTacoma/GIS_501_AU_2014/lab_4/data/Exercise07/"
infc= "roads.shp"
outfc = "Results/roads.shp"
newfield = "FERRY"
fieldtype = "TEXT"
fieldname = arcpy.ValidateFieldName(newfield)
delimitedfield = arcpy.AddFieldDelimiters(outfc, "FEATURES")
query = "\"FEATURES\" = \'""\'"
selected = arcpy.Select_analysis(infc, outfc, delimitedfield +" = \'Ferry Crossing\'")
addfield = arcpy.AddField_management(outfc, fieldname, fieldtype)


cursor = arcpy.da.UpdateCursor(fc, newfield)
if row in selected:
    row[0] = "YES"
    cursor.updateRow(row)
else:
    row[0] = "NO"
    cursor.updateRow(row)
