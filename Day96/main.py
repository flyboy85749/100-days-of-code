import requests
import config
from datetime import datetime

USERNAME = config.USERNAME
TOKEN = config.TOKEN
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}"

graph_config = {
    "id": "graph1",
    "name": "Photography Graph",
    "unit": "photos taken",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

photo_taken = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many photos did you take today? ")
}

photo_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

response = requests.post(url=photo_endpoint, json=photo_taken, headers=headers)
print(response.text)
