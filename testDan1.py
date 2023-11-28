import requests

url = 'http://localhost:5001/api/processJSON'
# data = {'stocks': 'MSFT'}

def stock_lowest_price(stock_ticker):
    data = {'stocks': stock_ticker}
    try:
        response = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
        result = response.json()
        day_low = result['data'][0]['day.l']
        return day_low
    except Exception as error:
        print('Error:', error)

if __name__ == '__main__':
    stock_ticker = input("write the stock ticker: ")
    day_low = stock_lowest_price(stock_ticker)
    print("The lowest price of the day for the stock ticker", stock_ticker,"is",day_low)  