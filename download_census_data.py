import re, urllib, time, zipfile, os

url_1st = "http://www.census.gov/geo/cob/bdy/tr/tr00shp/tr"
url_2nd = "_d00_shp.zip"
state_fips = ["01","02","04","05","06","08","09","10","11","12","13","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","44","45","46","47","48","49","50","51","53","54","55","56","72"]
stop_time = 3

download_location = "/Users/danielmsheehan/Downloads/census_2000"

#loop through all the state fips
for stfi in state_fips:
	
	print "Downloading... " + stfi 
	#download the zip file
	urllib.urlretrieve(url_1st + stfi + url_2nd, download_location+"/tr"+stfi+"_d00_shp.zip")

	#unzip the file
	zipfile.ZipFile(download_location+"/tr"+stfi+"_d00_shp.zip").extractall(download_location+"/")

	#delete the zip file
	os.remove(download_location+"/tr"+stfi+"_d00_shp.zip")
	print "Deleting... " + stfi + "'s ZIP file"

	#wait 3 seconds in case network connection is slow
	time.sleep(stop_time)

