#Data Source:
#In the data_ingestion/ folder, create a script called fetch_data.py to fetch financial data from an API and store it locally:

import requests

def fetch_data(api_url, output_file):
    response = requests.get(api_url)
    data = response.json()
    
    with open(output_file, 'w') as file:
        file.write(data)
        
# Usage
fetch_data('https://api.example.com/finance-data', 'data/raw_data.json')
