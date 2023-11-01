import requests 

# URL of the currency APP
app_url = 'http://localhost:5000'

def exchange_rate():
    try:
        response = requests.get(f'{app_url}/get_exchange_rate')
        if response.status_code == 200:
            data = response.json()
            exchange_rate = data.get('usd_cop_exchange_rate')
            if exchange_rate:
                return exchange_rate
            else:
                return 'Exchange rate not found in the response'
        else:
            return f'Failed to fetch exchange rate. Status Code: {response.status_code}, Response Content: {response.text}'
    except requests.RequestException as e:
        return f'Error: {e}'
    
if __name__ == '__main__':  
    exchange_rate = exchange_rate()
    print('Exchange rate (USD to COP):', exchange_rate)
    