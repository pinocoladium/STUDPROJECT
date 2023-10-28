import requests

response = requests.post('http://127.0.0.1:5000/users/',
                         json={'name': 'user_1', 'password': '12gsdedsrfergsdgesgeg34'})
print(response.status_code)
print(response.text)

# response = requests.patch('http://127.0.0.1:5000/users/3',
#                          json={'name': 'user_36777', 'password': '12gsdedsrfergsdgesgeg34', 'token': '4a60fddd-f7dc-4f7b-a78c-72419d7e28e7'})
# print(response.status_code)
# print(response.text)

# response = requests.get('http://127.0.0.1:5000/users/3',
#                         )
# print(response.status_code)
# print(response.text)

# response = requests.delete('http://127.0.0.1:5000/users/3',
#                          json={'name': 'user_36777', 'password': '12gsdedsrfergsdgesgeg34', 'token': '4a60fddd-f7dc-4f7b-a78c-72419d7e28e7'})
# print(response.status_code)
# print(response.text)

# response = requests.get('http://127.0.0.1:5000/users/3',
#                         )
# print(response.status_code)
# print(response.text)

# response = requests.post('http://127.0.0.1:5000/anno/',
#                          json={'header': 'best very header', 'description': '12gsdedsgsdgesgeg34 ghntyddd55555hyth', 'user_id': 4, 'token':'294fdb15-8488-4b4a-aaa3-dab7dbb76cb8'})
# print(response.status_code)
# print(response.text)

# response = requests.get('http://127.0.0.1:5000/anno/3',
#     )
# print(response.status_code)
# print(response.text)

# response = requests.patch('http://127.0.0.1:5000/anno/3',
#                          json={'header': 'best header23232', 'token':'294fdb15-8488-4b4a-aaa3-dab7dbb76cb8'})
# print(response.status_code)
# print(response.text)

# response = requests.delete(
#     "http://127.0.0.1:5000/anno/3", json={'token':'294fdb15-8488-4b4a-aaa3-dab7dbb76cb8'}
# )

# print(response.status_code)
# print(response.text)

# response = requests.get('http://127.0.0.1:5000/anno/3',
#     )
# print(response.status_code)
# print(response.text)

# response = requests.get("http://127.0.0.1:5000/users/1")

# print(response.status_code)
# print(response.text)
