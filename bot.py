import json
import cloudscraper
import tweepy
import secret
from time import sleep


def get_quote():
    headers = {"Accept": "application/json"}

    scraper = cloudscraper.create_scraper()
    response = scraper.get("https://api.animemoe.us/quotes/random/v2/", headers=headers)

    if response.status_code == 200:
        response = json.loads(response._content)
        return response
    else:
        return False


def update_status():

    quote = get_quote()

    if quote:
        auth = tweepy.OAuthHandler(secret.consumer_key, secret.consumer_secret)
        auth.set_access_token(secret.key, secret.secret_key)
        api = tweepy.API(auth)

        try:
            api.update_status(
                f"{quote['quote']}\n\n{quote['character']}, {quote['anime']}"
            )
            print("Tweeet created!")
        except:
            print("Try again...")
    else:
        print("Try again...")


update_status()
