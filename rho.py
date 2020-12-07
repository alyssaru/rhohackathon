import requests
import urllib.request
from bs4 import BeautifulSoup
import json

API_KEY = '6PeOM13XMqiUJls95ru5LIVliZECHIPAYWMgrVP3'
URL_START = 'https://api.nasa.gov/planetary/apod?'


def getMarsData():
    url = 'https://api.nasa.gov/insight_weather/?api_key=' + API_KEY + '&feedtype=json&ver=1.0'
    data = urllib.request.urlopen(url).read().decode()
    obj = json.loads(data)
    count = 0
    dates = []
    temps = []
    keys = obj['sol_keys']
    for num in keys:
        dateStart = obj[num]["First_UTC"]
        start = dateStart.split("-")
        startDate = start[1] + "/" + start[2][0:2] + "/" + start[0]
        dateEnd = obj[num]["Last_UTC"]
        end = dateEnd.split("-")
        endDate = end[1] + "/" + end[2][0:2] + "/" + end[0]
        totDates = startDate + "-" + endDate
        dates.append(totDates)
    
        avg = obj[num]["PRE"]["av"]
        temps.append(avg)
    f = open("SpaceWeather.txt", 'w')
    for num in range(len(keys)):
        f.write("Date: " + dates[num] + " Atmospheric pressure: " + str(temps[num]) + "\n")
    f.close()


def main():
    getMarsData()

main()
