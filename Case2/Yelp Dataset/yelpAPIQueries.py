#pip3 install yelp
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

CONSUMER_KEY = 'aFU9Unr7b5Z9EYZzdUoG-w'
CONSUMER_SECRET = '4YP7fQZNt20FtayojbrNeWhFZes'
TOKEN = 'Y3EwaElLgdNqaldbrxkxXVJxmQ3cH8Ub'
TOKEN_SECRET = 'DAWwdVm_pmIBV7f9MW2z8zZfypQ'

def loginClientAPI():
    auth = Oauth1Authenticator( consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, token=TOKEN, token_secret=TOKEN_SECRET)
    return Client(auth)

client = loginClientAPI()

# Sample code source of yelp api for python: https://github.com/Yelp/yelp-python
# https://www.yelp.com/developers/documentation/v2/search_api
WorcesterFood = client.search('Worcester, MA',{ 'term': 'food' })
print(WorcesterFood)

#https://www.yelp.com/developers/documentation/v2/business