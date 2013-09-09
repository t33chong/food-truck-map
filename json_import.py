import requests
import json
from json import load

class truck(object):
	
	def __init__(self, name, longitude, latitude, street_name):
		self.location = [longitude, latitude]
		self.name = name
		self.street_name = street_name


r = requests.get('http://data.sfgov.org/resource/rqzj-sfat.json')

j = json.loads(r.content)

#print j[0]['applicant'], j[0]['location']['longitude'], j[0]['location']['latitude']

listy = [1,2,3,4,5,6,7,8,9]

#for truckno in listy:
#	print j[truckno]['applicant'], j[truckno]['location']['longitude'], j[truckno]['location']['latitude'], '\n', j[truckno]['locationdescription']

truck1 = truck(j[0]['applicant'], j[0]['location']['longitude'], j[0]['location']['latitude'],  j[0]['locationdescription'])



print truck1.name
print truck1.location

trucklist = []

for items in j:
	trucklist.append(truck(j[0]['applicant'], j[0]['location']['longitude'], j[0]['location']['latitude'],  j[0]['locationdescription']))


print trucklist[0].name, trucklist[0].location
	


