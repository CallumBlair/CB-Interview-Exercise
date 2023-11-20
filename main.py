import constants as c
import query as q
import requests
import string
import json

minMaxTemps = {"city":"undefined", "timeSeries": []}


#city = input("enter city")
city = "London"
minMaxTemps["city"] = city


address = c.address.replace("<city>", city)
response = q.query(address, c.apiKey)


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
