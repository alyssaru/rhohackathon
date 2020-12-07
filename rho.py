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
    f.write("This week's weather on Mars: \n")
    for num in range(len(keys)):
        f.write("Date: " + dates[num] + " Atmospheric pressure: " + str(temps[num]) + "\n")
    f.close()

def getSolarFlare():
    url = 'https://api.nasa.gov/DONKI/FLR?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=' + API_KEY
    data = urllib.request.urlopen(url).read().decode()
    obj = json.loads(data)
    dates = []
    times = []
    for item in obj:
        lastFlare = item['flrID']
        day = lastFlare.split("-")
        date = day[1] + "/" + day[2][0:2] + "/" + day[0]
        dates.append(date)
    
        peakTime = item['peakTime']
        timeFlare = peakTime.split("T")[1][:5]
        times.append(timeFlare)
    f = open("SpaceWeather.txt", 'w')
    f.write("Most recent Solar Flares: \n")
    for num in range(len(dates)):
        f.write("Date: " + dates[num] + " Time: " + str(times[num]) + "\n")
    f.close()


def main():
    print("Commands:\nM - Mars Weather\nS - Solar Flares\nQ - Quit\n")
    val = input("Enter your value: ")
    if val == "M":
        getMarsData()
        print("Success! Open SpaceWeather.txt to see data\n")
        main()
    elif val == "S":
        getSolarFlare()
        print("Success! Open SpaceWeather.txt to see data\n")
        main()
    elif val == "Q":
        pass
    else:
        print("Invalid input\n")
        main()


main()
