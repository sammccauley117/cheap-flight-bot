import tweepy
import flightBotKeys as keys
import collectData, helpers, paths
import time, datetime, schedule, os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Authenticates tweepy
# Returns:
#   Authenticated tweepy api
def twitterAuth():
    # Users should fill these in with their personal keys
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
    return tweepy.API(auth)

# Returns either a headless or headed webdriver
# Parameters:
#   headless: (Bool) if True, create a headless driver
# Returns:
#   driver: (Selenium.webdriver) Selenium webdriver object
def getDriver(headless=True):
    if headless:
        options = Options()
        options.add_argument("--headless")
        return webdriver.Firefox(firefox_options=options)
    else:
        return webdriver.Firefox()

# Returns list of cheapest flight objects based on destinations.csv searches
# Parameters:
#   driver: (Selenium.webdriver) Selenium driver object
# Returns:
#   cheapest: (list<Flight>) list of cheapest Flight objects
def search(driver):
    cheapest = []

    # Used to find flights only during the university summer
    summerStart = datetime.date(2018, 5, 5)
    summerEnd = datetime.date(2018, 8, 15)

    # List of destinations
    searches = helpers.openCSV(paths.destinationsFile)
    destinations = helpers.destListToObject(searches)

    for dest in destinations:
        cheapFlight = collectData.collectData(driver=driver, departing='CVG', destination=dest.dest,
            tripLen=dest.tripLen, lowBound=summerStart, highBound=summerEnd)
        cheapest.append(cheapFlight)
    return cheapest

# Logs list of flights
# Parameters:
#   flights: (list<Flight>) list of cheapest Flights
def log(flights):
    for flight in flights:
        flight.log()

# Tweet out the flight details
# Parameters:
#   api: (tweepy.api) validated tweepy
#   flight: (Flight) flight object to tweet
#   media: (bool) if True, try to tweet with picture attached
def tweet(api, flight, media=True):
    status = str(flight)
    picPath = './../../private/pics/' + flight.dest + '.jpg'
    # if a picture for the destination exists, tweet with a picture attached
    if media and os.path.isfile(picPath):
        api.update_with_media(filename=picPath, status=status)
    else:
        api.update_status(status=status)

if __name__ == '__main__':
    driver = getDriver('headless')
    cheapest = search(driver)
    driver.quit()
    log(cheapest)
