import tweepy
import flightBotKeys as keys
import collectData, helpers
import time, datetime
from selenium import webdriver

#Use tweepy to sign into bot
driver = webdriver.Firefox()
cheapest = []

# Used to find flights only during the university summer
summerStart = datetime.date(2018, 5, 5)
summerEnd = datetime.date(2018, 8, 11)

for dest in helpers.airports.keys():
    cheapFlight = collectData.collectData(driver=driver, departing='CVG', destination=dest,
        tripLen=helpers.tripLen[dest], lowBound=summerStart, highBound=summerEnd)
    cheapest.append(cheapFlight)

# Sort the flights from best to worst deal
print '\n \nORDERED CHEAPEST FLIGHTS \n \n'
cheapestSorted = sorted(cheapest, key=lambda x: x.percentage)
for flight in cheapestSorted:
    print str(flight) + '\n' + str(flight.percentage) + '\n'
    flight.log()

# Authenticate Twitter API in using tweepy
# auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
# auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
# api = tweepy.API(auth)

# Update Twitter with the best flight
# api.update_with_media(filename='./../../private/pics/' + cheapestSorted[0].dest + '.jpg', status=str(cheapestSorted[0]))
