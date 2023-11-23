import query as q
import requests
import string
import json
import os


address = "https://cb-interview-exercise.ew.r.appspot.com/requestTemp?city=<name>"

minMaxTemps = {"city":"undefined", "timeSeries": []}

city = ""
while city == "":
    city = input("Please enter city now: ")

print("City selected: " + city)




addressCity = address.replace("<name>", city)

response = q.query(addressCity)
print("Response recieved")

with open("minMaxTemperatures.json", "w") as output:
    json.dump(response, output)

print("Output saved to minMaxTemperatures.json")
