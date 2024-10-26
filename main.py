# -- coding: utf8 --


import requests
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5OTc4MzU1LCJpYXQiOjE3Mjk5NzgwNTUsImp0aSI6IjZmNGMzNjkxYWEyOTQyZWJiMWM2MGQyMzliYzk0ZjhiIiwidXNlcl9pZCI6N30.4fShw2FRLgx-gPhnrnoH3pL79xEIEtqXVGRBRVGO1bs'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# a = requests.get(' http://127.0.0.1:8000/api/auth/profile/', headers=headers)
# a = requests.post('http://127.0.0.1:8000/api/auth/login/', json={'username':'pavdel', 'password':'tesdtdfdjnf34./sdf', 'email':'ddf4f@gmail.com', 'full_name':"pasfel"})
#
# print(a)
# print(a.json())
# print(a.content)

url = 'http://127.0.0.1:8000/messaging/send_message/'
data = {
    'message': 'text',
    'user_id': 5
}

# data = {
#     'messages': [{'role': 'user', 'content': 'предложи идею для челленджа'}, {'role': 'assistant', 'content': 'Хорошая идея для челленджа!\n\nНазовем его "Фитнес-Блиц"!\n\n**Цель:** Пройти 10 км за неделю, используя любые виды физической активности (ходьба, бег, велоспорт, плавание и т. д.)'}, {'role': 'user', 'content': 'про что этот челлендж'}]
# }
# headers = {
#     'Content-Type': 'application/json'
# }

response = requests.get(url, json=data, headers=headers)
# # print(response)
print(response.json())

# {'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMDAyNDEzMiwiaWF0IjoxNzI5OTM3NzMyLCJqdGkiOiJlYTZhYjQ0YjZmYmY0NWRjYjhkZGQ2OGVmOGM1NzhmNyIsInVzZXJfaWQiOjN9.bMqIhazi536qFcN5bw87YxpAz5n-7UkeZQxinjQvq9Y', 'access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5OTM4MDMyLCJpYXQiOjE3Mjk5Mzc3MzIsImp0aSI6IjgxOGI1OTlhOGMwYzQxNTNiMGQ3MDNhN2NjZDZhY2E2IiwidXNlcl9pZCI6M30.A-4I-AR5ipLTuZmj1je6T0iQVO4mgAKqwWTxkrg6Um4'}
