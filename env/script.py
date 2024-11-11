import base64
import requests
import webbrowser
import urllib.parse

# Spotify credentials (replace with your own)
clientId = 'df8f7091e27a4629bd0a531d717ea0ad'
clientSecret = '8990c8a785c6447086b24410aada80b1'
redirectUri = 'http://localhost:3000/callback'

# Step 1: Open the Authorization URL
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
    webbrowser.open(authUrl)  # This will open the URL in your default web browser

# Step 2: Token Retrieval
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

    # Checking the response
    if response.status_code == 200:
        tokenResponse = response.json()
        print("Access Token:", tokenResponse['access_token'])
        print("Refresh Token:", tokenResponse['refresh_token'])
        return tokenResponse
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

# Step 3: Automate the full process
def getToken():
    # Open the authorization URL for the user to log in and approve
    openSpotifyAuthorization()

    # After user authorizes, they will be redirected with the authorization code
    # You need to paste the code here for now
    authCode = input("Enter the authorization code from the URL: ")

    # Fetch the access token using the provided authorization code
    tokenResponse = getAccessToken(authCode)

    # If you get the token successfully, store it or use it for subsequent API requests
    if tokenResponse:
        print(f"Access Token: {tokenResponse['access_token']}")
        print(f"Refresh Token: {tokenResponse['refresh_token']}")
        return tokenResponse['access_token']

# Call the function to initiate the process
token = getToken()

# Use the token for API requests if needed
print(f"Token to use in API requests: {token}")
