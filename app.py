from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes
API_KEY = 'DM958STFT5HQABRF'

# This is a template format of the json query
@app.route('/docs', methods=['GET'])
def docs():
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo'
    r = requests.get(url)
    data = r.json()
    print(data)
    return data	

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Use try and except to handle errors and avoid app crashing
        try:
            # get the request from home.html 
            amount = request.form['amount']
            amount = float(amount) # convert to float - display decimals
            # get the requests from home.html
            convert_from = request.form['convert_from'] 
            convert_to = request.form['convert_to']
            # request data to api with selected currencies
            url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={convert_from}&to_currency={convert_to}&apikey={API_KEY}'
            response = requests.get(url).json()
            # get the exchange rate from the json response
            Exchange_Rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
            Exchange_Rate = float(Exchange_Rate) # convert to float - display decimals
            # calculate the conversion
            result = amount * Exchange_Rate
            # assign variables to other responses
            convert_from_code = response['Realtime Currency Exchange Rate']['1. From_Currency Code']
            convert_from_name = response['Realtime Currency Exchange Rate']['2. From_Currency Name']
            convert_to_code = response['Realtime Currency Exchange Rate']['3. To_Currency Code']
            convert_to_name = response['Realtime Currency Exchange Rate']['4. To_Currency Name']
            updated_time = response['Realtime Currency Exchange Rate']['6. Last Refreshed']
            return render_template('home.html', result=round(result, 2), amount=amount, 
                                   convert_from_code=convert_from_code, convert_from_name=convert_from_name, 
                                   convert_to_code=convert_to_code, convert_to_name=convert_to_name, 
                                   updated_time=updated_time)
        # if there is an error, return the home page
        except Exception as err_msg:
            return f'<h1> Bad Request : {err_msg} </h1>'
    else:
        return render_template('home.html')
    
######################################################################
# This is testing code to send USDCOP exchange rate to another program

@app.route('/get_exchange_rate', methods=['GET'])
def get_exchange_rate():
    # request exchange rate data
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=COP&apikey={API_KEY}'
    response = requests.get(url).json()
    exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
    
    # return the exchange rate as JSON
    return jsonify({'usd_cop_exchange_rate': exchange_rate})



if __name__ == '__main__':
    app.run(debug=True) 