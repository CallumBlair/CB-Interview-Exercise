import constants as c
import query as q
import requests
import string

#city = input("enter city")
city = "London"
address = c.address.replace("<city>", city)
q.query(address, c.apiKey)
