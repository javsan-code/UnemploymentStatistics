import requests
import json
import pandas as pd
import matplotlib as plt

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

unemployment_response = unemployment_response.json()
inflation_response = inflation_response.json()

unemployment_results = unemployment_response["Results"]
inflation_results = inflation_response["Results"]

inflation = pd.DataFrame(inflation_results, columns=['year','periodName', 'value'])
unemployment = pd.DataFrame(unemployment_results, columns=['year','periodName', 'value'])

print(unemployment_response)
#print("#######################################################")
print(inflation_response)

ax = unemployment.plot(x='periodName', y='value')
inflation.plot(ax=ax)
plt.title('Unemployment')
plt.show()
