import requests

api_token = "ed59e6df342decc4ebbd71aa60e6e23d"

#this is my github repository
github = "https://github.com/texasdan91/dansrepo.git"

#includes api token and the url to my github repository
data = {'token': api_token , 'github': github}

url = "http://challenge.code2040.org/api/register"

request = requests.post(url, json = data)