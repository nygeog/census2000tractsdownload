import re, urllib, time, zipfile, os


firsthalflink = "ftp://ftp2.census.gov/geo/tiger/TIGER2012/PUMA/"

ind_files = ["tl_2012_01_puma10.zip",
"tl_2012_02_puma10.zip",
"tl_2012_04_puma10.zip",
"tl_2012_05_puma10.zip",
"tl_2012_06_puma10.zip",
"tl_2012_08_puma10.zip",
"tl_2012_09_puma10.zip",
"tl_2012_10_puma10.zip",
"tl_2012_11_puma10.zip",
"tl_2012_12_puma10.zip",
"tl_2012_13_puma10.zip",
"tl_2012_15_puma10.zip",
"tl_2012_16_puma10.zip",
"tl_2012_17_puma10.zip",
"tl_2012_18_puma10.zip",
"tl_2012_19_puma10.zip",
"tl_2012_20_puma10.zip",
"tl_2012_21_puma10.zip",
"tl_2012_22_puma10.zip",
"tl_2012_23_puma10.zip",
"tl_2012_24_puma10.zip",
"tl_2012_25_puma10.zip",
"tl_2012_26_puma10.zip",
"tl_2012_27_puma10.zip",
"tl_2012_28_puma10.zip",
"tl_2012_29_puma10.zip",
"tl_2012_30_puma10.zip",
"tl_2012_31_puma10.zip",
"tl_2012_32_puma10.zip",
"tl_2012_33_puma10.zip",
"tl_2012_34_puma10.zip",
"tl_2012_35_puma10.zip",
"tl_2012_36_puma10.zip",
"tl_2012_37_puma10.zip",
"tl_2012_38_puma10.zip",
"tl_2012_39_puma10.zip",
"tl_2012_40_puma10.zip",
"tl_2012_41_puma10.zip",
"tl_2012_42_puma10.zip",
"tl_2012_44_puma10.zip",
"tl_2012_45_puma10.zip",
"tl_2012_46_puma10.zip",
"tl_2012_47_puma10.zip",
"tl_2012_48_puma10.zip",
"tl_2012_49_puma10.zip",
"tl_2012_50_puma10.zip",
"tl_2012_51_puma10.zip",
"tl_2012_53_puma10.zip",
"tl_2012_54_puma10.zip",
"tl_2012_55_puma10.zip",
"tl_2012_56_puma10.zip",
"tl_2012_66_puma10.zip",
"tl_2012_72_puma10.zip",
"tl_2012_78_puma10.zip"]

download_location = "E:/Dropbox/GIS/Data/Census/acs_2008_2011/" 
stop_time = 3



for indfiles in ind_files:
	#urllib.urlretrieve(firsthalflink+indfiles, download_location+indfiles)
	#print "Downloading... " + indfiles

	#zipfile.ZipFile(download_location+indfiles).extractall(download_location+"/")
	#print "Unzipping... " + indfiles

	os.remove(download_location+indfiles)
	print "Deleting... " + indfiles

	time.sleep(stop_time)