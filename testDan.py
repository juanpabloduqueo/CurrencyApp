import requests

url = 'http://localhost:5001/api/processJSON'
data = {'stocks': 'MSFT'}

try:
    response = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
    result = response.json()
    day_low = result['data'][0]['day.l']
    print(day_low)
except Exception as error:
    print('Error:', error)
