import tweepy
import flightBotKeys as keys
import collectData
import helpers

#Use tweepy to sign into bot
auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
api = tweepy.API(auth)

lowPrice, lowDest, lowDepDate, lowRetDate = collectData.collectData()
tweet = '''The cheapest flight of the day is ${}:\n\nCincinnati to {}\n{} - {}\n
Book using Google Flights'''.format(str(lowPrice), helpers.decodeAirport(lowDest),
lowDepDate, lowRetDate)
api.update_status(status=tweet)
