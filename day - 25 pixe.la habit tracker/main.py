import requests

endpoint_url = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN":"Krevory123"
}
user_parameter = {
    "token":"Krevory123",
    "username":"kim0001",
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

#user created
# response = requests.post(url=endpoint_url,json=user_parameter)
# print(response.text)

# graph_endpoint = f"{endpoint_url}/kim0001/graphs"
#
# graph_parameter = {
#     "id":"a1",
#     "name":"cycling",
#     "unit":"Km",
#     "type":"float",
#     "color":"shibafu"
# }
#
# response = requests.post(url=graph_endpoint,json=graph_parameter,headers=headers)
# print(response.text)

pixel_post = f"{endpoint_url}/kim0001/graphs/a1"

pixel_post_parameter = {
    "date":"20210825",
    "quantity": "5"
}

response = requests.post(url=pixel_post,json=pixel_post_parameter,headers=headers)
print(response.text)
