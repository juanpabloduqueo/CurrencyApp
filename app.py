from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS
from random import randint
import json
from externalService import get_stock_prices
from internalService import get_exchange_data
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)
API_KEY = os.environ.get('API_KEY')
CORS(app) # This will enable CORS for all routes

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
        amount = float(request.form['amount'])
        convert_from = request.form['convert_from'] 
        convert_to = request.form['convert_to']
        (result, from_code, from_name, to_code, to_name, updated_time) = get_exchange_data(amount, convert_to, convert_from, API_KEY) 

        ###################### This is my partner's microservice part #####################
        stock_ticker = request.form['stock_ticker']
        (day_low_stock, day_high_stock) = get_stock_prices(stock_ticker)
        ###################### End of my partner's microservice part ######################      
        
        return render_template('home.html', amount=amount, result=result,
                            convert_from_code=from_code, convert_from_name=from_name, 
                            convert_to_code=to_code, convert_to_name=to_name, 
                            updated_time=updated_time, day_low_stock=day_low_stock, 
                            day_high_stock=day_high_stock,stock_ticker=stock_ticker)  
    else:
        return render_template('home.html')
    
############################################################################################################
# This is the endpoint to connect to this app as a microservice
@app.route('/get_exchange_rate', methods=['GET'])
def get_exchange_rate():
    # request exchange rate data
    origin = request.args['origin']
    if "origin" not in request.args:
        return jsonify({'query string error': "Expected origin parameter"}) 
    
    destination = request.args['destination']
    if "destination" not in request.args:
        return jsonify({'query string error': "Expected destination parameter"}) 
    
    quantity = 1 if "quantity" not in request.args else float(request.args['quantity']) 

    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={origin}&to_currency={destination}&apikey={API_KEY}'
    
    response = requests.get(url).json()
    
    if "Information" in response:
        return "This is an academic app. Daily allowed requests have been exhausted. Change of IP address and API key is needed to proceed." 
    
    exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
    
    result = quantity * float(exchange_rate) 
    
    # return the exchange rate as JSON
    return jsonify({'from_currency': origin, 'to_currency': destination, 'quantity': quantity,'result': str(result)})

##########################################################
    
if __name__ == '__main__':
    app.run(debug=True) 