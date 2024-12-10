import base64
import requests
import webbrowser
import urllib.parse
from dotenv import load_dotenv
import os

load_dotenv()

# Spotify credentials (replace with your own)

clientId = os.getenv('clientId')
clientSecret = os.getenv('clientSecret')
redirectUri = 'http://127.0.0.1:4000'

# Open the Authorization URL
def openSpotifyAuthorization():
    baseUrl = "https://accounts.spotify.com/authorize"
    params = {
        "client_id": clientId,
        "response_type": "code",
        "redirect_uri": redirectUri,
        "scope": "user-top-read"
    }
    authUrl = f"{baseUrl}?{urllib.parse.urlencode(params)}"
    print(f"Opening URL for authorization: {authUrl}")
    webbrowser.open(authUrl)  
    
#Token handler
def getAccessToken(authCode):
    # Encoding client ID and secret
    authStr = f"{clientId}:{clientSecret}"
    authBytes = authStr.encode('utf-8')
    authBase64 = base64.b64encode(authBytes).decode('utf-8')

    headers = {
        'Authorization': f'Basic {authBase64}',
    }

    data = {
        'grant_type': 'authorization_code',
        'code': authCode,
        'redirect_uri': redirectUri,
    }

    # Sending the POST request to exchange authorization code for access token
    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

    # Checking te responseh
    if response.status_code == 200:
        tokenResponse = response.json()
        print("Access Token:", tokenResponse['access_token'])
        print("Refresh Token:", tokenResponse['refresh_token'])
        return tokenResponse
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None


def getToken():
    
    openSpotifyAuthorization()
    # Paste the code here
    authCode = input("Enter the authorization code from the URL: ")

    # Fetch the access token using the provided authorization code
    tokenResponse = getAccessToken(authCode)

    # Store it or use it for subsequent API requests if success
    if tokenResponse:
        print(f"Access Token: {tokenResponse['access_token']}")
        print(f"Refresh Token: {tokenResponse['refresh_token']}")
        return tokenResponse['access_token']

token = getToken()

print(f"Token to use in API requests: {token}")
