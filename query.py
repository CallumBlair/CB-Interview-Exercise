import requests

def query(address):
    #header = {"x-api-key" : key}
    #response = requests.get(address, headers=header)
    response = requests.get(address)
    return response.json()
