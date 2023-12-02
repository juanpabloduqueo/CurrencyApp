import requests

def get_stock_prices(stock_ticker):
    # request stock data to API
    url_stock = 'http://localhost:5001/api/processJSON'
    data_stock = {'stocks': stock_ticker}
    
    try:
        response_stock = requests.post(url_stock, json=data_stock, headers={'Content-Type': 'application/json'})
        result_stock = response_stock.json()
        day_low_stock = result_stock['data'][0]['day.l']
        day_high_stock = result_stock['data'][0]['day.h']
    except Exception as error:
        print('Error:', error)
    
    return day_low_stock, day_high_stock