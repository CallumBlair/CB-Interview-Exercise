#Import Libraries
from flask import Flask, request
import requests
import string
import json
import os

#Initialise key from server enviroment variables
key = os.environ.get("x_api_key")

#Define flask application
app = Flask(__name__)

#Query function
def query(address, Apikey):
    #Create header using the given API Key 
    header = {"x-api-key" : Apikey}
    #Fire get request and return the JSON file
    response = requests.get(address, headers=header)
    return response.json()


#Request Temp route
#Returns a sorted JSON response with the minimum and maximum temperatures
@app.route('/requestTemp', methods = ["get"])
def requestTemp():
    #API address
    address = "https://durvp011gk.execute-api.eu-west-1.amazonaws.com/v1/api/forecasts?city=<name>"
    #Parse city parameter
    city = request.args.get('city')
    #Initialise min max temperature dictionary
    minMaxTemps = {"city":"undefined", "timeSeries": []}
    minMaxTemps["city"] = city

    #Build the request address from the users selection
    addressCity = address.replace("<name>", city)
    #Fire request using query function
    response = query(addressCity, key)
    
    #Validate the request has not failed
    if "message" in response and response["message"] == "Forbidden":
        #Return error message
        return("Access forbidden - please check the entered key")
    else:
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
        #Return minMaxTemps dictionary
        return minMaxTemps

        
    


if __name__ == "__main__":
    #app.run(debug=True)
    app.run()
