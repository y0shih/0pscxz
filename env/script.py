import base64
import requests

# Spotify auth code reset every few minutes so make sure to get it before run
# Replace these with your token and stuff
client_id = 'df8f7091e27a4629bd0a531d717ea0ad'
client_secret = '8990c8a785c6447086b24410aada80b1'
auth_code = 'AQCIXtOIFMc8yka06R9xnb0sktRzyLIlashozqqpYc6B4UwCxaCR73GZODQQvuaMjk5geocCHGQtaYXA_jE8u74SnCk1E0P8m4WO9hrOZsL_wUyMBsG89TQctHNJe7-FediOgPIDcwE8tvJnBaHZwUUVQxIXhgqI4BRxczdwUroJUhbN3vZ0yeFpWdZfQ75vYA'
redirect_uri = 'http://localhost:3000/callback'

# Encoding the client ID and secret
auth_str = f"{client_id}:{client_secret}"
auth_bytes = auth_str.encode('utf-8')
auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

# Defining the headers and data
headers = {
    'Authorization': f'Basic {auth_base64}',
}

data = {
    'grant_type': 'authorization_code',
    'code': auth_code,
    'redirect_uri': redirect_uri,
}

# Sending the POST request
response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

# Checking the response
if response.status_code == 200:
    print("Access Token:", response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.json())
