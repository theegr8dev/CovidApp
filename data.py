import requests
from datetime import date



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
    
