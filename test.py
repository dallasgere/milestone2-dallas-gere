import json
import requests

url = "https://en.wikipedia.org/w/api.php"
title = "Bullet Train movie"

# this will be used to find the page id
params = {
    "action": "query",
    "format": "json",
    "titles": title,
    "prop": "links"
}

response = requests.get(
    url,
    params
)

json_data_id = response.json()
read_id = json.dumps(json_data_id, indent = 1, sort_keys=True) 
#print(read_id)
print("")

# this will be used to find the final url which needs the page id
parameters = {
    "action": "query",
    "format": "json",
    "titles": title,
    "prop": "info",
    "inprop": "url|talkid",
}

response = requests.get(
    url,
    parameters
)

json_data = response.json()
read = json.dumps(json_data, indent = 1, sort_keys=True) 
print(read)
var = json_data['query']['pages']['-1']['fullurl']
print("")
print(var)