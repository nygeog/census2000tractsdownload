import re, urllib, time, zipfile, os 
#import os for mac and delete

url_pre = "ftp://ftp2.census.gov/geo/tiger/TIGER2010/TRACT/"
url_mid = "/tl_2010_"
url_ltr = "_tract"
url_zip = ".zip"

# full urls
#ftp://ftp2.census.gov/geo/tiger/TIGER2010/TRACT/2000/tl_2010_01_tract00.zip
#ftp://ftp2.census.gov/geo/tiger/TIGER2010/TRACT/2010/tl_2010_01_tract10.zip
#http://www2.census.gov/geo/tiger/PREVGENZ/tr/tr90shp/tr01_d90_shp.zip

census_year = "2000" #"2000" or "2010"
zipfile_year = "00" #"00" or "10"

## UNCOMMENT FOR 1990
## UNCOMMENT FOR 1990
url_pre = "http://www2.census.gov/geo/tiger/PREVGENZ/tr/tr90shp/tr"
url_mid = ""
url_ltr = "_d90_shp"
url_zip = ".zip"
census_year = "" 
zipfile_year = "" 

state_fips = ["01","02","04","05","06","08","09","10","11","12","13","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","44","45","46","47","48","49","50","51","53","54","55","56","72"]
stop_time = 3

#put your file location here between quotes ie. "/Users/<YOURUSERNAME>/Downloads/census_2000"
download_location = "/Users/danielmsheehan/Desktop/census_1990" + zipfile_year

#loop through all the state fips
for stfi in state_fips:
	
	
	#download the zip file
	urllib.urlretrieve(url_pre + census_year + url_mid + stfi + url_ltr + zipfile_year + url_zip, download_location+url_mid + stfi + url_ltr + zipfile_year + url_zip)
	print "Downloading... " + stfi 

	#unzip the file
	zipfile.ZipFile(download_location+url_mid + stfi + url_ltr + zipfile_year + url_zip).extractall(download_location+"/")
	print "Unzipping... " + stfi 

	#delete the zip file
	os.remove(download_location+url_mid + stfi + url_ltr + zipfile_year + url_zip)
	print "Deleting... " + stfi + "'s ZIP file"

	#wait 3 seconds in case network connection is slow
	time.sleep(stop_time)

