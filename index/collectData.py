'''
    File: collectData.py
    Description: this program opens up a FireFox browser. Using Selenium, it
                 loads a flight request and scrapes the cheapest flight from
                 the webpage. The data is then logged to a corresponding .csv
                 file.
    Date: 2/22/2018
    Version: 0.0.0
'''

import time, datetime, sys, locale
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Pass: Selenium element that contains flight price
# Returns: price parsed to integer
def toInt(price):
    ret = price.text.replace('$','')
    ret = ret.replace(',','')
    return int(ret)



def collectData():
    # Constants
    URL     = 'https://www.google.com/flights/#search;f={};t={};d={};r={}'
    FROM    = 'CVG' # Departing airport
    MINDATE = 60    # Creates a scanning range of
    MAXDATE = 90    # [today + MINDATE, today + MAXDATE]
    TRIPLEN = 10    # How long the trip lasts
    PRICECLASS    = 'LJV2HGB-d-Ab'   # HTML class where the price is stored
    DESTINTATIONS = ['CDG', 'BCN', 'LHR', # Paris    Barce.    Londo.
                     'AMS', 'FRA', 'MAD', # Amste.   Frank.    Madrid
                     'ZRH', 'ATH'] #'VIE', # Zuric.   Athens    Vienna
                     #'BUD', 'BRU']        # Budap.   Bruss.
    oLowPrice   = sys.maxint # overall lowest price
    oLowDest    = ''      # overall lowest destination
    oLowDepDate = ''         # overall lowest departure date
    oLowRetDate = ''         # overall lowest return date

    # Creates Selenium web driver object
    driver = webdriver.Firefox()

    # Creates a list of all datetimes to check
    dateRange   = []
    for i in range(MINDATE, MAXDATE):
        dateRange.append(datetime.date.today() + datetime.timedelta(i))

    # Open log book
    with open('./../src/data/log.csv', 'a') as myfile:
        myfile.write(datetime.date.today().strftime("%Y-%m-%d") + ',')

    # Main loop
    for dest in DESTINTATIONS:
        destPriceList = [] # List of all the cheapest prices for a destination
        for date in dateRange:

            # Open up URL and get lowest price
            # Departure date
            d = date.strftime("%Y-%m-%d")
            # Return date
            r = (date + datetime.timedelta(TRIPLEN)).strftime("%Y-%m-%d")
            driver.get(URL.format(FROM, dest, d, r)) # Opens URL
            time.sleep(1) # Allows the page to load. Needs a better trigger
            # list of all class elements
            prices = driver.find_elements_by_class_name(PRICECLASS)
            lowest = sys.maxint # lowest price of specific day
            for price in prices:
                if toInt(price) < lowest:
                    lowest = toInt(price)
                    if lowest < oLowPrice: # updates overall low
                        oLowPrice   = lowest
                        oLowDest    = dest
                        oLowDepDate = date.strftime("%m/%d/%Y")
                        oLowRetDate = (date + datetime.timedelta(TRIPLEN)).strftime("%m/%d/%Y")
            destPriceList.append(lowest)

        # Opens dest database and adds average price
        with open('./../src/data/' + dest + '.csv', 'a') as myfile:
            myfile.write(datetime.date.today().strftime("%Y-%m-%d") + ',')
            myfile.write(str(sum(destPriceList)/len(destPriceList)) + '\n')
    # Confirms completion
    with open('./../src/data/log.csv', 'a') as myfile:
        myfile.write('completed\n')

    # Return overall low data
    return oLowPrice, oLowDest, oLowDepDate, oLowRetDate
















































# I put comments down here so that I can scroll past the bottom of my code
