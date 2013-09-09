import requests
import json
import pygmaps

class Truck(object):

    def __init__(self, name, longitude, latitude, street_name):
        self.location = [longitude, latitude]
        self.name = name
        self.street_name = street_name

    def get_latitude(self):
        """Accessor method; returns latitude."""
        return self.location[1]

    def get_longitude(self):
        """Accessor method; returns longitude."""
        return self.location[0]

    def get_name(self):
        """Accessor method; returns name."""
        return self.name

    def get_street_name(self):
        """Accessor method; returns street name."""
        return self.street_name


r = requests.get('http://data.sfgov.org/resource/rqzj-sfat.json')

j = json.loads(r.content)

#print j[0]['applicant'], j[0]['location']['longitude'], j[0]['location']['latitude']

listy = [1,2,3,4,5,6,7,8,9]

#for truckno in listy:
#    print j[truckno]['applicant'], j[truckno]['location']['longitude'], j[truckno]['location']['latitude'], '\n', j[truckno]['locationdescription']

truck1 = Truck(j[0]['applicant'], j[0]['location']['longitude'], j[0]['location']['latitude'],  j[0]['locationdescription'])



print truck1.name
print truck1.location

trucklist = []

for items in j:
    trucklist.append(Truck(j[0]['applicant'], j[0]['location']['longitude'], j[0]['location']['latitude'],  j[0]['locationdescription']))


print trucklist[0].name, trucklist[0].location

sf = pygmaps.maps(37.783333, -122.416667, 14)
