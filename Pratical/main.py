import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import requests

def History(country):
    import requests

    url = "https://covid-193.p.rapidapi.com/history"

    querystring = {"country":country,"day":"2020-06-02"}

    headers = {
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
        "X-RapidAPI-Key": "de4b5d5543mshe4062d2b91bc892p1f7f1fjsn5f7a2a9f7e28"
    }

    HistroyResponse = requests.request("GET", url, headers=headers, params=querystring)
    return HistroyResponse.text
    
def Statistics(country):
    
    url = "https://covid-193.p.rapidapi.com/statistics"

    #querystring = {"country":country}

    headers = {
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
        "X-RapidAPI-Key": "de4b5d5543mshe4062d2b91bc892p1f7f1fjsn5f7a2a9f7e28"
    }

    StatisticsResponse = requests.request("GET", url, headers=headers)
    return StatisticsResponse.text

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

my_


time = []
recovered = []
death = []
cases = []

for i in data:
    time.append(i['time'].replace(i['day']+'T','').replace("+00:00",''))
    print(i['cases'])
    death.append(i['deaths']['total'])
    cases.append(i['cases']['total'])
''' 
x1 = [
'2020-06-02T23:45:06+00:00', '2020-06-02T23:30:06+00:00', '2020-06-02T23:15:06+00:00', '2020-06-02T23:06:42+00:00', '2020-06-02T22:45:08+00:00', '2020-06-02T22:30:06+00:00', '2020-06-02T22:15:06+00:00', '2020-06-02T21:45:06+00:00', '2020-06-02T21:30:06+00:00', '2020-06-02T21:15:06+00:00']
y1 = [
1, 2, 3, 4, 5, 6, 7, 8, 9, 2 ]

x2 = ['2020-06-02T23:45:06+00:00', '2020-06-02T23:30:06+00:00', '2020-06-02T23:15:06+00:00', '2020-06-02T23:06:42+00:00', '2020-06-02T22:45:08+00:00', '2020-06-02T22:30:06+00:00', '2020-06-02T22:15:06+00:00', '2020-06-02T21:45:06+00:00', '2020-06-02T21:30:06+00:00', '2020-06-02T21:15:06+00:00']

y2 = [ 2, 3,1, 2, 3,1,  1, 1, 1, 2]

a = []
b  = []
for i in x1:
    a.append(i.replace('2020-06-02T',''))
    
for c in x2:    
    b.append(c.replace('2020-06-02T',''))
    
#print(a)      

#print(b)  


plt.plot(b, y2)
plt.plot(b, y1)

plt.show()

#print(a.replace('2020-06-02T',''))

#from datetime import datetime
#date = "2020-06-02T23:45:06+00:00"
#a = date.replace('2020-06-02T','')
#print(a)






x1 = [
'02-20T23:45:06+00:00-2021', '02-20T23:00:06+00:00-2021', '02-20T22:45:06+00:00-2021', '02-20T22:30:06+00:00-2021']
y1 = [28671866, 28670843, 28669726, 28668488]
x2 = ['02-20T23:45:06+00:00-2021', '02-20T23:00:06+00:00-2021', '02-20T22:45:06+00:00-2021', '02-20T22:30:06+00:00-2021']
y2 =[28651866, 22370843, 21169726, 28668158]

#tick = (28671866, 28670843, 28669726, 28668488)
#plt.yticks(y1, tick)
plt.plot(x1, y1)

plt.plot(x2,y2)
plt.show()





x1 = [
'02-20T23:45:06+00:00-2021', '02-20T23:00:06+00:00-2021', '02-20T22:45:06+00:00-2021', '02-20T22:30:06+00:00-2021']
y1 = [1,3,5,7]
x2 = ['02-20T23:45:06+00:00-2021', '02-20T23:00:06+00:00-2021', '02-20T22:45:06+00:00-2021', '02-20T22:30:06+00:00-2021']
y2 = [1,7,2,9]

tick = [28671866, 28670843, 28669726, 28668488]
plt.yticks(y1, tick)
plt.plot(x1, y1)

plt.plot(x2,y2)
plt.show()
'''
'''    
obj1 = History('USA', '2022-02-20')
load = json.loads(obj1)
data = load['response']

df = pd.DataFrame(columns=['time', 'cases' ])
df2 = pd.DataFrame(columns=['time', 'deaths' ])

for i in range(0, len(data)):
    currentItem = data[i]
    df.loc[i] = [data[i]['time'], data[i]['cases']['total']]
    df2.loc[i] = [data[i]['time'], data[i]['deaths']['total']]
    
xAxis = [i for i in df['time']]
yAxis = [i for i in df['cases']]
plt.plot(xAxis, yAxis, color='maroon', marker='o')
xAxis2 = [i for i in df2['time']]
yAxis2 = [i for i in df2['deaths']]
plt.plot(xAxis, yAxis2, color='green', marker='*')
labels = xAxis
plt.grid(True)


plt.xlabel('countries')
plt.ylabel('cases')
plt.xticks(xAxis, labels, rotation=30, ha='right')

plt.show()

width = 2
height = 2
width_height = (width,height)
plt.figure(figsize=width_height)
'''