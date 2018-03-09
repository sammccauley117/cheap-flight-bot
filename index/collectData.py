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
import helpers
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Flight:
    logPath = 'C:\Users\Sam\Documents\Git\CheapFlightBot\private\data\\'
    def __init__(self, dep='', dest='', price=10000000, avg=1, logDate=datetime.date.today(),
        depDate=datetime.date.today(), retDate=datetime.date.today(), percentage=-1.00, tweeted=False):
        self.dep = dep         # (String) departing airport
        self.dest = dest       # (String) destination airport
        self.price = price     # (int) price
        self.avg = avg         # (int) average price
        self.logDate = logDate # (date) date at which this was logged
        self.depDate = depDate # (date) departing date
        self.retDate = retDate # (date) return date
        self.tweeted = tweeted # (bool) True = tweeted, False = not tweeted
        self.percentage = 1000000.0
    def __str__(self):
        dateFormat = "%m/%d/%Y"
        ret = '$' + str(self.price) + ' round trip:\n'
        ret += helpers.decodeAirport(self.dep)
        ret += ' \xE2\x9C\x88 ' + helpers.decodeAirport(self.dest) + '\n'
        ret += self.depDate.strftime(dateFormat)
        ret += ' - ' + self.retDate.strftime(dateFormat) + '\n'
        ret += self.getURL()
        return ret
    def getURL(self):
        URL_DATE_FORMAT = "%Y-%m-%d"
        URL = 'https://www.google.com/flights/#search;f={};t={};d={};r={}'
        return URL.format(self.dep, self.dest, self.depDate.strftime(URL_DATE_FORMAT),
            self.retDate.strftime(URL_DATE_FORMAT))
    def setAverage(self, avg):
        self.avg = avg
        self.percentage = (float(self.price) / self.avg) * 100
    def tweeted(self):
        # Call if this flight was tweeted (BEFORE LOGGING)
        self.tweeted = True
    def log(self):
        # .csv format:
        # time, departing airport, price, average price, percentage, tweeted
        dateFormat = "%m/%d/%Y"
        with open(self.logPath + self.dest + '.csv', 'a') as logFile:
            logFile.write(self.logDate.strftime(dateFormat) + ',' +
                self.dep + ',' +
                self.dest + ',' +
                self.depDate.strftime(dateFormat) + ',' +
                self.retDate.strftime(dateFormat) + ',' +
                str(self.price) + ',' +
                str(self.avg) + ',' +
                str(self.tweeted) + '\n')



# Pass: String in the format 'US$1,000'
# Returns: String parsed to integer
def toInt(price):
    ret = price.replace('US','')
    ret = price.replace('$','')
    ret = ret.replace(',','')
    return int(ret)



def collectData(driver, departing, destination, tripLen, lowBound=datetime.date.today(),
    highBound=datetime.date.today()):
    # Constants
    OFFSET = 28 # This is the ammount that the arrow progresses the chart by
    D = lowBound # Initial departure for URL
    R = lowBound + datetime.timedelta(tripLen) # Initial return for URL
    if lowBound is datetime.date.today() and highBound is datetime.date.today():
        D += datetime.timedelta(40) # preserves the count accuracy
        R += datetime.timedelta(40)

    URL_DATE_FORMAT = "%Y-%m-%d"
    URL = 'https://www.google.com/flights/#search;f={};t={};d={};r={}'.format(
        departing, destination, D.strftime(URL_DATE_FORMAT), R.strftime(URL_DATE_FORMAT))

    driver.get(URL) # Opens URL
    time.sleep(.5)  # Loading buffer

    # Ultimately does all of the navigation to open up the graphical view
    element = driver.find_element(By.XPATH, '//div[contains(@class, "LJV2HGB-G-s LJV2HGB-G-r LJV2HGB-c-r LJV2HGB-D-a")]')
    element = element.find_element(By.XPATH, '//div[contains(@class, "LJV2HGB-G-m")]')
    element.click()
    element = element.find_element(By.XPATH, '//div[contains(@class, "LJV2HGB-o-I LJV2HGB-o-x")]')
    element.click()
    time.sleep(3)

    # Graph container div
    element = element.find_element(By.XPATH, '//div[contains(@class, "LJV2HGB-gb-s LJV2HGB-gb-b")]')
    # Arrow to proceed down the graph
    arrow = element.find_element(By.XPATH, '//div[contains(@class, "LJV2HGB-fb-d LJV2HGB-c-b")]')
    # The average that Google Flights calculates
    flightAvg = toInt(element.find_element(By.XPATH, '//div[contains(@class, "LJV2HGB-gb-f")]').text)
    flights = [] # List of all Flight objects
    valid = True # Becomes false when data is failed to be collected (when a bar is gray)
    inBound = True # Becomes false when dates leave the upper and lower bounds
    count = 0 # Used to efficiently calculate what day it is by adding timedelta(count)

    # Loops through all bars on the chart
    while(valid):
        bars = element.find_elements(By.XPATH, '//div[contains(@class, "LJV2HGB-gb-z")]')
        for i in range(len(bars) - OFFSET, len(bars)):
            if inBound:
                ActionChains(driver).move_to_element(bars[i]).perform()
                price = bars[i].find_element(By.XPATH, '//div[contains(@class, "LJV2HGB-gb-I")]').text
                date  = bars[i].find_element(By.XPATH, '//div[contains(@class, "LJV2HGB-gb-H")]').text
                if price == '' or date == '':
                    valid = False
                else:
                    depDate = D + datetime.timedelta(count)
                    retDate = R + datetime.timedelta(count)
                    flights.append(Flight(dep=departing, dest=destination, price=toInt(price),
                        avg=flightAvg, depDate=depDate, retDate=retDate))
                    if flights[-1].retDate > highBound or flights[-1].depDate < lowBound:
                        valid = False
                        inBounds = False
                count = count + 1
        if valid and inBound:
            ActionChains(driver).move_to_element(arrow).perform()
            arrow.click()
            time.sleep(5)

    # Finds the best deal of all the flights
    priceSum = 0.0
    lowestFlight = Flight()
    for flight in flights:
        priceSum += flight.price
        if(flight.price < lowestFlight.price):
                lowestFlight = flight
    lowestFlight.setAverage(int(priceSum/len(flights)))
    print str(lowestFlight) + '\n'

    # Return best deal
    return lowestFlight

















































# I put comments down here so that I can scroll past the bottom of my code
