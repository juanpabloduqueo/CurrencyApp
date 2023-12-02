import requests

def get_exchange_data(amount, convert_to, convert_from, API_KEY):
        url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={convert_from}&to_currency={convert_to}&apikey={API_KEY}'
        response = requests.get(url).json()
        Exchange_Rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
        Exchange_Rate = float(Exchange_Rate) # convert to float - display decimals
        result = round(amount * Exchange_Rate, 2)
        curr_exchange = response['Realtime Currency Exchange Rate']
        return result, curr_exchange['1. From_Currency Code'], curr_exchange['2. From_Currency Name'], \
               curr_exchange['3. To_Currency Code'], curr_exchange['4. To_Currency Name'], curr_exchange['6. Last Refreshed']    