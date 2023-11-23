#Import Libraries
import query as q
import requests
import string
import json
import os

#API address
address = "https://cb-interview-exercise.ew.r.appspot.com/requestTemp?city=<name>"

#Initialise min max temperature dictionary
minMaxTemps = {"city":"undefined", "timeSeries": []}

#Recieve city choice from user
city = ""
while city == "":
    city = input("Please enter city now: ")
print("City selected: " + city)

#Build the request address from the users selection
addressCity = address.replace("<name>", city)

#Send response
response = q.query(addressCity)
print("Response recieved")

#Save result to minMaxTemeratures.json file
with open("minMaxTemperatures.json", "w") as output:
    json.dump(response, output)
print("Output saved to minMaxTemperatures.json")
