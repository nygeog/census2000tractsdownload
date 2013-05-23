import arcpy
from arcpy import env
env.overwriteOutput = True

# RUN IN WINDOWS!!!!!!!!!!!!!!!!
#you'll need ArcGIS to use the arcpy module 

#directory: you'lll need to change this to fit your file
pre = "X:/census_2000/tr"
#file extension
suf = "_d00.shp"

arcpy.Merge_management([pre+"01"+suf, pre+"02"+suf, pre+"04"+suf, pre+"05"+suf, pre+"06"+suf, pre+"08"+suf, pre+"09"+suf, pre+"10"+suf, pre+"11"+suf, pre+"12"+suf, pre+"13"+suf, pre+"15"+suf, pre+"16"+suf, pre+"17"+suf, pre+"18"+suf, pre+"19"+suf, pre+"20"+suf, pre+"21"+suf, pre+"22"+suf, pre+"23"+suf, pre+"24"+suf, pre+"25"+suf, pre+"26"+suf, pre+"27"+suf, pre+"28"+suf, pre+"29"+suf, pre+"30"+suf, pre+"31"+suf, pre+"32"+suf, pre+"33"+suf, pre+"34"+suf, pre+"35"+suf, pre+"36"+suf, pre+"37"+suf, pre+"38"+suf, pre+"39"+suf, pre+"40"+suf, pre+"41"+suf, pre+"42"+suf, pre+"44"+suf, pre+"45"+suf, pre+"46"+suf, pre+"47"+suf, pre+"48"+suf, pre+"49"+suf, pre+"50"+suf, pre+"51"+suf, pre+"53"+suf, pre+"54"+suf, pre+"55"+suf, pre+"56"+suf, pre+"72"+suf], pre+"acts"+suf)
arcpy.DefineProjection_management(pre+"acts"+suf,"GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"

try:
	arcpy.DeleteField_management(pre+"acts"+suf,"TR01_D00_;TR01_D00_I;TR02_D00_;TR02_D00_I;TR04_D00_;TR04_D00_I;TR05_D00_;TR05_D00_I;TR06_D00_;TR06_D00_I;TR08_D00_;TR08_D00_I;TR09_D00_;TR09_D00_I;TR10_D00_;TR10_D00_I;TR11_D00_;TR11_D00_I;TR12_D00_;TR12_D00_I;TR13_D00_;TR13_D00_I;TR15_D00_;TR15_D00_I;TR16_D00_;TR16_D00_I;TR17_D00_;TR17_D00_I;TR18_D00_;TR18_D00_I;TR19_D00_;TR19_D00_I;TR20_D00_;TR20_D00_I;TR21_D00_;TR21_D00_I;TR22_D00_;TR22_D00_I;TR23_D00_;TR23_D00_I;TR24_D00_;TR24_D00_I;TR25_D00_;TR25_D00_I;TR26_D00_;TR26_D00_I;TR27_D00_;TR27_D00_I;TR28_D00_;TR28_D00_I;TR29_D00_;TR29_D00_I;TR30_D00_;TR30_D00_I;TR31_D00_;TR31_D00_I;TR32_D00_;TR32_D00_I;TR33_D00_;TR33_D00_I;TR34_D00_;TR34_D00_I;TR35_D00_;TR35_D00_I;TR36_D00_;TR36_D00_I;TR37_D00_;TR37_D00_I;TR38_D00_;TR38_D00_I;TR39_D00_;TR39_D00_I;TR40_D00_;TR40_D00_I;TR41_D00_;TR41_D00_I;TR42_D00_;TR42_D00_I;TR44_D00_;TR44_D00_I;TR45_D00_;TR45_D00_I;TR46_D00_;TR46_D00_I;TR47_D00_;TR47_D00_I;TR48_D00_;TR48_D00_I;TR49_D00_;TR49_D00_I;TR50_D00_;TR50_D00_I;TR51_D00_;TR51_D00_I;TR53_D00_;TR53_D00_I;TR54_D00_;TR54_D00_I;TR55_D00_;TR55_D00_I;TR56_D00_;TR56_D00_I;TR72_D00_;TR72_D00_I")
except:
	print "fields are clean"