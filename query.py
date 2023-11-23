#Import Libraries
import requests

#Query function returning JSON from API
def query(address):
    response = requests.get(address)
    return response.json()
