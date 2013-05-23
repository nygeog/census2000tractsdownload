import arcpy

# RUN IN WINDOWS!!!!!!!!!!!!!!!!
#you'll need ArcGIS to use the arcpy module 

#directory: you'lll need to change this to fit your file
pre = "X:/census_2000/tr"
#file extension
suf = "_d00.shp"

arcpy.Merge_management([pre+"01"+suf, pre+"02"+suf, pre+"04"+suf, pre+"05"+suf, pre+"06"+suf, pre+"08"+suf, pre+"09"+suf, pre+"10"+suf, pre+"11"+suf, pre+"12"+suf, pre+"13"+suf, pre+"15"+suf, pre+"16"+suf, pre+"17"+suf, pre+"18"+suf, pre+"19"+suf, pre+"20"+suf, pre+"21"+suf, pre+"22"+suf, pre+"23"+suf, pre+"24"+suf, pre+"25"+suf, pre+"26"+suf, pre+"27"+suf, pre+"28"+suf, pre+"29"+suf, pre+"30"+suf, pre+"31"+suf, pre+"32"+suf, pre+"33"+suf, pre+"34"+suf, pre+"35"+suf, pre+"36"+suf, pre+"37"+suf, pre+"38"+suf, pre+"39"+suf, pre+"40"+suf, pre+"41"+suf, pre+"42"+suf, pre+"44"+suf, pre+"45"+suf, pre+"46"+suf, pre+"47"+suf, pre+"48"+suf, pre+"49"+suf, pre+"50"+suf, pre+"51"+suf, pre+"53"+suf, pre+"54"+suf, pre+"55"+suf, pre+"56"+suf, pre+"72"+suf], pre+"acts"+suf)
arcpy.DefineProjection_management(pre+"acts"+suf,"GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"