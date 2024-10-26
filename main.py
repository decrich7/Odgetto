# -- coding: utf8 --


import requests
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5OTM4NDU3LCJpYXQiOjE3Mjk5MzgxNTcsImp0aSI6ImIyYjMzNzI3MzlmODRkNjQ4MTZiOWE4OTk3MDZlYmRmIiwidXNlcl9pZCI6NH0.XIlDLgbAcOUy3lVvE_eo_KUwaYoX5OwzNhiEk-PFgIo'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# a = requests.get(' http://127.0.0.1:8000/api/auth/profile/', headers=headers)
# a = requests.post('http://127.0.0.1:8000/api/auth/register/', json={'username':'pavel', 'password':'testdfdjnf34./sdf', 'email':'df34hfdddddf4f@gmail.com', 'full_name':"pavsdfdsfel"})
#
# print(a)
# print(a.json())
# print(a.content)

url = 'http://127.0.0.1:8000/messaging/send_message/'
data = {
    'message': 'пися попа)))))))',
    'user_id': 4
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.get(url, json=data, headers=headers)
print(response)

# {'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMDAyNDEzMiwiaWF0IjoxNzI5OTM3NzMyLCJqdGkiOiJlYTZhYjQ0YjZmYmY0NWRjYjhkZGQ2OGVmOGM1NzhmNyIsInVzZXJfaWQiOjN9.bMqIhazi536qFcN5bw87YxpAz5n-7UkeZQxinjQvq9Y', 'access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5OTM4MDMyLCJpYXQiOjE3Mjk5Mzc3MzIsImp0aSI6IjgxOGI1OTlhOGMwYzQxNTNiMGQ3MDNhN2NjZDZhY2E2IiwidXNlcl9pZCI6M30.A-4I-AR5ipLTuZmj1je6T0iQVO4mgAKqwWTxkrg6Um4'}
