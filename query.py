import requests

def query(address, key):
    header = {"x-api-key" : key}
    response = requests.get(address, headers=header)
    print(response.json())
