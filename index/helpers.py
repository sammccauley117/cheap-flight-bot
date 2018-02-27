# This file contains misc. helper functions

# All airports to check
airports = {
    'ATH' : 'Athens, Greece',
    'AMS' : 'Amsterdam, Netherlands',
    'BCN' : 'Barcelona, Spain',
    'BRU' : 'Brussels, Belgium',
    'BUD' : 'Budapest, Hungary',
    'CDG' : 'Paris, France',
    'CMN' : 'Casablanca, Morocco',
    'DUB' : 'Dublin, Ireland',
    'FRA' : 'Frankfurt, Germany',
    'HAV' : 'Havana, Cuba',
    'KEF' : 'Reykjav\xC3\xADk, Iceland',
    'LHR' : 'London, England',
    'LIH' : 'Kauai, Hawaii',
    'LIM' : 'Lima, Peru',
    'MAD' : 'Madrid, Spain',
    'SJC' : 'San Jose, Costa Rica',
    'TLV' : 'Tel Aviv, Israel',
    'VIE' : 'Vienna, Austria',
    'ZRH' : 'Z\xC3\xBCrich, Switzerland'
}

# Takes a airport acronym and translates it to its corresponding city and country
def decodeAirport(airport):
    if airport in airports:
        return airports[airport]
    else:
        if airport is 'CVG':
            return 'Cincinnati, Ohio'
        else:
            return 'N/A'
