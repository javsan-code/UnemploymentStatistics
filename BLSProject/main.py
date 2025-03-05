import requests
import json
import pandas as pd
import matplotlib as mpl


BLS_API_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

headers = {"Content-type": "application/json"}
unemployment_data = {
    "seriesid": ["LNS14000000"],  # Unemployment Rate
    "startyear": "2016",
    "endyear": "2023"
}
inflation_data = {
    "seriesid": ["CUUR0000SA0"],  # Inflation Rate
    "startyear": "2016",
    "endyear": "2023"
}

unemployment_response = requests.post(BLS_API_URL, json=unemployment_data, headers=headers)
inflation_response = requests.post(BLS_API_URL, json=inflation_data, headers=headers)
print(json.dumps(unemployment_response.json(), indent=4))
print("#######################################################")
print(json.dumps(inflation_response.json(), indent=4))