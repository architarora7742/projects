# We are using the requests module for a while now, and we have been using it to make HTTP requests across the internet.
# GET -> This is the way for us to get the pieces of data from somebody else like an API provider.
# POST -> A Post request is where we give the external system some piece of data. We are not interested in getting the response back, whetehre we are successful or not.
# PUT -> It is where you update a piece of data in the external service.
# DELETE -> It is where you Delete a piece of data from an external service.

import requests

USERNAME = "architarora"
TOKEN = "your token"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    #     YOU CAN CREATE YOUR OWN API TOKEN
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# STEP 1
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "cycling",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# STEP 2
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# The request is done through the request header (X-USER-TOKEN)
# There are three ways for a request, 1. api key, 2. X-API-KEY, 3. Authorization
# The request is recommended using HTTP header so that api key isn't visible to others in logs or request sniffing.
# headers are like header for a letter
# Normally we make a request to that URL and pass over these parameters, all our secret stuff is in request itself, so if anybody is monitoring this, then they will be able to see all of this info,
# One of the things that is reassuring is that this API is accessed via HTTPS (S for Secure ) - The request is actually encrypted ,but it doesn't stop somebody from installing something in your browser to look at what requests that you are making ,and they might get your API key.

pixel_data = {
    "date": "20250908",
    "quantity": "10",

}

# STEP 3
response = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}", headers=headers, json=pixel_data)
print(response.text)
