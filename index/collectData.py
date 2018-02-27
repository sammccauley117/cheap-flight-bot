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
    def __init__(self, dep='', dest='', price=0, depDate=datetime.date.today(), retDate=datetime.date.today()):
        self.dep = dep          # (String) departing airport
        self.dest = dest        # (String) destination airport
        self.price = price      # (int) price
        self.depDate = depDate  # (date) departing date
        self.retDate = retDate  # (date) return date
        self.perc = 100000.00   # (float) percentage of average
    def __str__(self):
        dateFormat = "%m/%d/%Y"
        ret = '$' + str(self.price) + ' round trip:\n'
        ret += helpers.decodeAirport(self.dep)
        ret += ' \xE2\x9C\x88 ' + helpers.decodeAirport(self.dest) + '\n'
        ret += self.depDate.strftime(dateFormat)
        ret += ' - ' + self.retDate.strftime(dateFormat) + '\n'
        ret += '(' + str(int(100 - self.perc)) + '%' + ' cheaper than usual)'
        return ret
    def calcPerc(self, avg):
        self.perc = (float(self.price) / avg) * 100



# Pass: String in the format 'US$1,000'
# Returns: String parsed to integer
def toInt(price):
    ret = price.replace('US','')
    ret = price.replace('$','')
    ret = ret.replace(',','')
    return int(ret)



def collectData(driver, departing, destination):
    # Constants
    OFFSET  = 40
    TRIPLEN = 6    # How long the trip lasts
    URL_DATE_FORMAT = "%Y-%m-%d"
    D = datetime.date.today() + datetime.timedelta(OFFSET) # Initial departure for URL
    R = datetime.date.today() + datetime.timedelta(OFFSET+TRIPLEN) # Initial return for URL
    DEP = departing # Which airport to depart from
    DEST = destination # Destination airport
    URL = 'https://www.google.com/flights/#search;f={};t={};d={};r={}'.format(
        DEP, DEST, D.strftime(URL_DATE_FORMAT), R.strftime(URL_DATE_FORMAT))

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
    valid = 1 # Becomes false when data is failed to be collected (when a bar is gray)
    count = 0 # Used to efficiently calculate what day it is by adding timedelta(count)

    # Loops through all bars on the chart
    while(valid):
        bars    = element.find_elements(By.XPATH, '//div[contains(@class, "LJV2HGB-gb-z")]')
        for i in range(len(bars) - 28, len(bars)):
            ActionChains(driver).move_to_element(bars[i]).perform()
            price = bars[i].find_element(By.XPATH, '//div[contains(@class, "LJV2HGB-gb-I")]').text
            date  = bars[i].find_element(By.XPATH, '//div[contains(@class, "LJV2HGB-gb-H")]').text
            if price == '' or date == '':
                valid = 0
            else:
                depDate = D + datetime.timedelta(count)
                retDate = R + datetime.timedelta(count)
                flights.append(Flight(DEP, DEST, toInt(price), depDate, retDate))
                flights[-1].calcPerc(flightAvg)
            count = count + 1
        ActionChains(driver).move_to_element(arrow).perform()
        arrow.click()
        time.sleep(3)

    # Finds the best deal of all the flights
    lowestFlight = Flight()
    for flight in flights:
        if(flight.perc < lowestFlight.perc):
                lowestFlight = flight

    # Return best deal
    return lowestFlight

















































# I put comments down here so that I can scroll past the bottom of my code
