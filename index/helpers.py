# This file contains misc. helper functions

# Takes a airport acronym and translates it to its serving city and country
def decodeAirport(airport):
    dests  = ['CDG', 'BCN', 'LHR',
              'AMS', 'FRA', 'MAD',
              'ZRH', 'ATH', 'VIE',
              'BUD', 'BRU']
    decode = ['Paris, France', 'Barcelona, Spain', 'London, England',
              'Amsterdam, Netherlands', 'Frankfurt, Germany', 'Madrid, Spain',
              'Z\xC3\xBCrich, Switzerland', 'Athens, Greece', 'Vienna, Austria',
              'Budapest, Hungary', 'Brussels, Belgium']
    for i in range(len(dests)):
        if(dests[i] == airport):
            return decode[i]
