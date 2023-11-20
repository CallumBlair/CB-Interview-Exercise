import constants as c
import query as q
import requests
import string
import json

address = "https://durvp011gk.execute-api.eu-west-1.amazonaws.com/v1/api/forecasts?city=<name>"

minMaxTemps = {"city":"undefined", "timeSeries": []}

city = ""
while city == "":
    city = input("Please enter city now: ")

print("City selected: " + city)

minMaxTemps["city"] = city


addressCity = address.replace("<name>", city)
response = q.query(addressCity, c.apiKey)
print("Response recieved")

for x in response["features"][0]["properties"]["timeSeries"]:
    date = x["time"].split("T")[0]
    temperature = x["screenTemperature"]
    if date not in [i["date"] for i in minMaxTemps["timeSeries"]]:

        minMaxTemps["timeSeries"].append({"date":date,
                                       "minTemp":temperature,
                                       "maxTemp":temperature})
    else:
        index = [i["date"] for i in minMaxTemps["timeSeries"]].index(date)
        if minMaxTemps["timeSeries"][index]["minTemp"] > temperature:
            minMaxTemps["timeSeries"][index]["minTemp"] = temperature
            
        if minMaxTemps["timeSeries"][index]["maxTemp"] < temperature:
            minMaxTemps["timeSeries"][index]["maxTemp"] = temperature


with open("minMaxTemperatures.json", "w") as output:
    json.dump(minMaxTemps, output)

print("Output saved to minMaxTemperatures.json")
