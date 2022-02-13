import requests
from datetime import datetime
import config

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = config.USERNAME
TOKEN = config.TOKEN
GRAPH_ID = config.GRAPH_ID

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# ---------------- Create a new account ---------------------
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# ------------------ Create a graph -----------------------
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': GRAPH_ID,
    'name': 'Programming Graph',
    'unit': 'minutes',
    'type': 'int',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# ------------ PUT a graph (change graph settings) ------------------
put_graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

put_graph_config = {
    'name': 'Python Bootcamp',
    'unit': 'hour',
    'timezone': 'Europe/Warsaw'
}

# response = requests.put(url=put_graph_endpoint, json=put_graph_config, headers=headers)
# print(response.text)


# --------------- POST a pixel into a graph -------------------------
post_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now()
format_today = today.strftime('%Y%m%d')

post_pixel_config = {
    'date': format_today,
    'quantity': input("How many hours have you been coding today? Only integers, please: "),
}
response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
print(response.text)


# ------------------- PUT a pixel (change) -----------------------------------------
put_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{format_today}'

put_pixel_config = {
    'quantity': '3',
}
# response = requests.put(url=put_pixel_endpoint, json=put_pixel_config, headers=headers)
# print(response.text)


# ----------------- DELETE a pixel ---------------------------
delete_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{format_today}'

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)