import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

from datetime import date
import requests
import numpy as np


def Global():
    import requests

    url = "https://covid-19-v1.p.rapidapi.com/v1/all"

    headers = {
        "X-RapidAPI-Host": "covid-19-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "de4b5d5543mshe4062d2b91bc892p1f7f1fjsn5f7a2a9f7e28"
    }

    response = requests.request("GET", url, headers=headers)

    return response.text


def Country():
    import requests

    url = "https://covid-193.p.rapidapi.com/countries"

    headers = {
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
        "X-RapidAPI-Key": "de4b5d5543mshe4062d2b91bc892p1f7f1fjsn5f7a2a9f7e28"
    }

    CountryResponse = requests.request("GET", url, headers=headers)
    return CountryResponse.text
    
    

Date = date.today()
currentDay =  Date.strftime("%Y-%m-%d")
def History(country, Day = currentDay):
    # currentDate = input('Enter day Y-M-D: ')

    url = "https://covid-193.p.rapidapi.com/history"

    querystring = {"country": country,"day":Day}

    headers = {
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
        "X-RapidAPI-Key": "de4b5d5543mshe4062d2b91bc892p1f7f1fjsn5f7a2a9f7e28"
    }

    CountryHistory = requests.request("GET", url, headers=headers, params=querystring)

    return CountryHistory.text
        
h = History('usa','2020-06-02')
load = json.loads(h)
data = load['response']
time = []
recovered = []
death = []
cases = []

for i in data:
    time.append(i['time'].replace(i['day']+'T','').replace("+00:00",''))
    recovered.append(i['cases']['recovered'])
    death.append(i['deaths']['total'])
    cases.append(i['cases']['total'])
   

#a = np.array(time,recovered)
#print(a)


plt.plot(time, recovered, label='recovered')
#recoveredmin, recoveredmax = min(recovered), max(recovered)
plt.plot( time, death)
casesmin, casesmax = min(recovered), max(recovered)
plt.show()




'''     
#print(time)    
#print(recovered)    
#print(death)   
x = np.array(time)
y = np.array(cases)

x2 = np.array(time)
y2 = np.array(recovered)

plt.plot(x, y, 'r', x2, y2,'--b')
plt.show()

#x1 = np.array(data)
#print(x1)

print(data[2]['population'])
df = pd.DataFrame(columns=['time', 'cases', 'recovered'])
df2 = pd.DataFrame(columns=['time', 'recovered'])
df3 = pd.DataFrame(columns=['time', 'death'])

for i in range(0, len(data)):
    currentItem = data[i]
    df.loc[i] = [data[i]['time'], data[i]['cases']['total'], data[i]['cases']['recovered']] 
    df2.loc[i] = [data[i]['time'], data[i]['cases']['recovered']]
    df3.loc[i] = [data[i]['time'], data[i]['deaths']['total']] 


#plt.plot(df['time'],df['recovered'])
plt.plot(df['time'],df['cases'])


plt.show()

#print(type(df), df, sep='\n')
#print(np.shape(arr), type(arr), arr, sep='\n')

arr = np.array([df['time'], df['cases']])
plt.plot(arr[0, 'time'], arr[0, 'cases'], 'g', label='Line y')


xAxis = [i for i in df['time']]
yAxis = [i for i in df['cases']]
xAxis2 = [i for i in df2['time']]
yAxis2 = [i for i in df2['recovered']]

labels = xAxis
plt.grid(True)

plt.plot(xAxis, yAxis, color='maroon' )
plt.plot(xAxis2, yAxis2, color='green' )

plt.xlabel('countries')
plt.ylabel('cases')
plt.xticks(xAxis, labels, rotation=30, ha='right')

plt.show()
'''