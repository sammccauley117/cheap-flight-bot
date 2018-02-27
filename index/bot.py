import tweepy
import flightBotKeys as keys
import collectData
import helpers
import time
from selenium import webdriver

#Use tweepy to sign into bot
driver = webdriver.Firefox()
cheapest = []

for d in helpers.airports.keys():
    cheapest.append(collectData.collectData(driver, 'CVG', d))

# Sort the flights from best to worst deal
cheapestSorted = sorted(cheapest, key=lambda x: x.perc)

# Authenticate Twitter API in using tweepy
auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
api = tweepy.API(auth)

# Update Twitter with the best flight
api.update_status(status=str(cheapestSorted[0]))
