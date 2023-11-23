#Import Libraries
import requests

#Query function
def query(address, key):
    #Create header using the given API Key 
    header = {"x-api-key" : key}
    #Fire get request and return the JSON file
    response = requests.get(address, headers=header)
    return response.json()
