import requests
import json

# api-endpoint
URL = "https://api.umd.io/v1/courses"
 
 
# defining a params dict for the parameters to be sent to the API
PARAMS = {}
 
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
 
# extracting data in json format
data = r.json()

with open("course_data.json", "w") as file: 
    json.dump(data, file)
 