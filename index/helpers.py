import csv

class Destination:
    def __init__(self, dest, tripLen, city, country):
        self.dest = dest
        self.tripLen = tripLen
        self.city = city
        self.country = country


# Parse CSV and return a list
def openCSV(path):
    with open(path) as filename:
        return list(csv.reader(filter(lambda row: row[0]!='#', filename)))

# Takes a list of destinations and turns them into a list of Destination objects
def destListToObject(list):
    toReturn = []
    for item in list:
        toReturn.append(Destination(item[0],int(item[1]),item[2],item[3]))
    return toReturn
