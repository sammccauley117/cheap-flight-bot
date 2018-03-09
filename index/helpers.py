# This file contains misc. helper functions

# All airports to check
airports = {
    'AKL' : 'Auckland, New Zealand',
    'AMS' : 'Amsterdam, Netherlands',
    'ATH' : 'Athens, Greece',
    'BCN' : 'Barcelona, Spain',
    'BKK' : 'Bangkok, Thailand',
    'BRU' : 'Brussels, Belgium',
    'BUD' : 'Budapest, Hungary',
    'CDG' : 'Paris, France',
    'CMN' : 'Casablanca, Morocco',
    'CPT' : 'Cape Town, South Africa',
    'DUB' : 'Dublin, Ireland',
    'EZE' : 'Buenos Aires, Argentina',
    'FRA' : 'Frankfurt, Germany',
    'HAV' : 'Havana, Cuba',
    'HND' : 'Tokyo, Japan',
    'ICN' : 'Seoul, South Korea',
    'KEF' : 'Reykjav\xC3\xADk, Iceland',
    'LHR' : 'London, England',
    'LIH' : 'Kauai, Hawaii',
    'LIM' : 'Lima, Peru',
    'MAD' : 'Madrid, Spain',
    'NAS' : 'Nassau, Bahamas',
    'NRT' : 'Tokyo, Japan',
    'PTY' : 'Panama City, Panama',
    'SCL' : 'Santiago, Chile',
    'SGN' : 'Ho Chi Minh City, Vietnam',
    'SIN' : 'Singapore',
    'SJC' : 'San Jose, Costa Rica',
    'TLV' : 'Tel Aviv, Israel',
    'VIE' : 'Vienna, Austria',
    'YUL' : 'Montreal, Canada',
    'ZRH' : 'Z\xC3\xBCrich, Switzerland'
}

# Optimal trip length
tripLen = {
    'AKL' : 7,
    'AMS' : 10,
    'ATH' : 7,
    'BCN' : 10,
    'BKK' : 10,
    'BRU' : 10,
    'BUD' : 10,
    'CDG' : 10,
    'CMN' : 7,
    'CPT' : 8,
    'DUB' : 6,
    'EZE' : 7,
    'FRA' : 10,
    'HAV' : 6,
    'HND' : 10,
    'ICN' : 10,
    'KEF' : 6,
    'LHR' : 7,
    'LIH' : 6,
    'LIM' : 6,
    'MAD' : 6,
    'NAS' : 6,
    'NRT' : 10,
    'PTY' : 5,
    'SCL' : 6,
    'SGN' : 10,
    'SJC' : 6,
    'SIN' : 7,
    'TLV' : 7,
    'VIE' : 10,
    'YUL' : 3,
    'ZRH' : 10
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
