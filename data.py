import requests
import json

getCountry = input('Enter Country: ')



def Country():
    import requests

    url = "https://covid-193.p.rapidapi.com/countries"

    headers = {
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
        "X-RapidAPI-Key": "de4b5d5543mshe4062d2b91bc892p1f7f1fjsn5f7a2a9f7e28"
    }

    CountryResponse = requests.request("GET", url, headers=headers)
    return CountryResponse.text


def Statistics():
    import requests

    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":getCountry}

    headers = {
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
        "X-RapidAPI-Key": "de4b5d5543mshe4062d2b91bc892p1f7f1fjsn5f7a2a9f7e28"
    }

    StatisticsResponse = requests.request("GET", url, headers=headers, params=querystring)
    return StatisticsResponse.text

    
def Histroy():
    import requests

    url = "https://covid-193.p.rapidapi.com/history"

    querystring = {"country":getCountry,"day":"2020-06-02"}

    headers = {
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
        "X-RapidAPI-Key": "de4b5d5543mshe4062d2b91bc892p1f7f1fjsn5f7a2a9f7e28"
    }

    HistroyResponse = requests.request("GET", url, headers=headers, params=querystring)

obj1 = Statistics()
load = json.loads(obj1)

for i in load:
    dump = json.dumps(load[i], indent=2)
# print(dump)

'''
class Test(object):
    def __init__(self, data):
	    self.__dict__ = json.loads(obj1)

test1 = Test(load)
print(test1.response)
'''