import requests
from bs4 import BeautifulSoup
from config import CLIENT_ID, CLIENT_SECRET


def get_stepik_token():
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    response = requests.post('https://stepik.org/oauth2/token/',
                            data={'grant_type': 'client_credentials'},
                            auth=auth)
    token = response.json().get('access_token', None)
    if not token:
        raise Exception('Unable to authorize with provided credentials')
    return token


def stepik_data(url, stepik_token):
    response = requests.get(url,
                        headers={'Authorization': 'Bearer ' + stepik_token})
    if response.status_code == 200:
        return response.json()
    else:
        stepik_token = get_stepik_token()
        return stepik_data(url, stepik_token)


def html_title(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title
    title = soup.title.string.strip()[:-9]

    return title