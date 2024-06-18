"""
import folium
import phonenumbers
from myphone import numbers

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(numbers)
location = geocoder.description_for_number(pepnumber, "en")
print(location) 

from phonenumbers import carrier
service = phonenumbers.parse(numbers)
print(carrier.name_for_number(service, "en"))

from opencage.geocoder import OpenCageGeocode

key = "d951d9c0df4c47d78da6b55a958392eb"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]

print(lat,lng)

map = folium.Map(location = [lat,lng], zoom_start = 9)
folium.Marker([lat,lng], popup = location).add_to(map)

map.save("location.html")
"""