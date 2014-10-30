import arcpy
print "The following extensions are available:"
if arcpy.CheckExtension('3D') == "Available":
    print '3D'
if arcpy.CheckExtension('Network') == "Available":
    print 'Network Analyst'
if arcpy.CheckExtension('Spatial') == "Available":
    print 'Spatial Analyst'
