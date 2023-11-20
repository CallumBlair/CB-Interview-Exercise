import requests

def query(address, key):
    header = {"x-api-key" : key}
    response = requests.get(address, headers=header)
    return response.json()
