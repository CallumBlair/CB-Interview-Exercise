from flask import Flask, request
import requests
import string
import json
import os

key = os.environ.get("x_api_key")

app = Flask(__name__)

def query(address, key):
    header = {"x-api-key" : key}
    response = requests.get(address, headers=header)
    return response.json()


@app.route('/')
def index():
    return "TEST"

@app.route('/requestTemp', methods = ["get"])
def requestTemp():
    address = "https://durvp011gk.execute-api.eu-west-1.amazonaws.com/v1/api/forecasts?city=<name>"
    city = request.args.get('city')
    minMaxTemps = {"city":"undefined", "timeSeries": []}


    #print("City selected: " + city)

    minMaxTemps["city"] = city


    addressCity = address.replace("<name>", city)
    response = query(addressCity, key)
    #print("Response recieved")
    #return(response)
    
    
    if "message" in response and response["message"] == "Forbidden":
        return("Access forbidden - please check the entered key")
    else:
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
        
        return minMaxTemps

        
    


if __name__ == "__main__":
    #app.run(debug=True)
    app.run()
