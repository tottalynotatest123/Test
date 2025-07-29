import requests

USERNAME = 'panviceontop@gmail.com'
PASSWORD = 'qawszedx'

response = requests.get('https://api.pcloud.com/userinfo', params={
    'getauth': 1,
    'username': USERNAME,
    'password': PASSWORD
})

auth_token = response.json().get('auth')
print("Auth token:", auth_token)
