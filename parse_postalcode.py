import sys
import requests
import json
import csv

def getJson(adres):
	postcode_hnr = str.split(adres, ' ')
	postcode = postcode_hnr[0]
	hnr = postcode_hnr[1]
	requestString = 'http://api.postcodedata.nl/v1/postcode/?postcode=%s&streetnumber=%s&ref=domeinnaam.nl&type=json' % (postcode, hnr)
	return requests.get(requestString).text

def parseFile(filename, outfile):
	c = csv.writer(open(outfile, "wb"))
	c.writerow(["adres","city","province","municipality","street","lat","lon"])
	with open(filename, "r") as ifile:
		for line in ifile:
			json_txt = getJson(line)
			json_parsed = json.loads(json_txt)
			print line
			adres = line.strip()
			city = json_parsed['details'][0]['city'] 
			province = json_parsed['details'][0]['province'] 
			municipality = json_parsed['details'][0]['municipality']
			street = json_parsed['details'][0]['street']  
			lat = json_parsed['details'][0]['lat']
			lon = json_parsed['details'][0]['lon']
			c.writerow([adres, city,province,municipality,street,lat,lon])  


filename = sys.argv[1]
outfile = sys.argv[2]
parseFile(filename, outfile)

