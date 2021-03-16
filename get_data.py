import requests
import json

def main(person, config):
    rapid_api_key= config['rapid_api_key']

    url = "https://covid-19-data.p.rapidapi.com/totals"

    headers = {
        'x-rapidapi-key': rapid_api_key,
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    #response_json = json.loads(response.text)
    return(response.text)