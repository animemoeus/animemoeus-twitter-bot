import requests
import json
import tweepy
import time
import random
import secrets

def get_data():
    response = requests.get('https://api.animemoe.us/quotes/random/').text
    response = json.loads(response)['data']
    return response

def create_status():
    #get twitter login session
    auth = tweepy.OAuthHandler(secrets.alpha, secrets.beta)
    auth.set_access_token(secrets.gamma, secrets.delta)
    api = tweepy.API(auth)

    data = get_data()

    #create tweet
    try:
        print('Creating tweet.')
        if len(data['text']) >= 280:
            print('Tweet needs to be a bit shorter.')
        else:
            text = data['text']+'\n\n~'+data['author']+', '+data['source']
            api.update_status(text)
            print(text)
    except:
        print('Something wrong.')


if __name__ == '__main__':
    create_status()