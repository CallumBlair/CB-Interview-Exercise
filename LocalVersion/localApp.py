#Import Libraries
import query as q
import requests
import string
import json


#API Adress
address = "https://durvp011gk.execute-api.eu-west-1.amazonaws.com/v1/api/forecasts?city=<name>"

#Initialise Dictionary
minMaxTemps = {"city":"undefined", "timeSeries": []}

#Request API key from user
key = input("Please enter your API Key now for temporary access: ")

#Recieve city choice from user
city = ""
while city == "":
    city = input("Please enter city now: ")
print("City selected: " + city)
minMaxTemps["city"] = city

#Build the request address from the users selection
addressCity = address.replace("<name>", city)
#Fire request using query function
response = q.query(addressCity, key)
print("Response recieved")


try:
    #Validate the request has not failed
    if response["message"] == "Forbidden":
        #Print error message
        print("Access forbidden - please check the entered key")
except:
    #Iterate through the JSON response
    for x in response["features"][0]["properties"]["timeSeries"]:
        date = x["time"].split("T")[0]
        temperature = x["screenTemperature"]
        #If the date has not been added yet add it to the dictionary with the temperature as both min and max
        if date not in [i["date"] for i in minMaxTemps["timeSeries"]]:
            minMaxTemps["timeSeries"].append({"date":date,
                                           "minTemp":temperature,
                                           "maxTemp":temperature})
        #If the date has already been added compare that times temperatures with current dates temperatures
        #Replace if it is a new minimum or maximum
        else:
            index = [i["date"] for i in minMaxTemps["timeSeries"]].index(date)
            if minMaxTemps["timeSeries"][index]["minTemp"] > temperature:
                minMaxTemps["timeSeries"][index]["minTemp"] = temperature
                
            if minMaxTemps["timeSeries"][index]["maxTemp"] < temperature:
                minMaxTemps["timeSeries"][index]["maxTemp"] = temperature

    #Save result to minMaxTemeratures.json file
    with open("minMaxTemperatures.json", "w") as output:
        json.dump(minMaxTemps, output)
    print("Output saved to minMaxTemperatures.json")
