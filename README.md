# CurrencyApp

To start the program, go to the terminal (in my case, it's the vscode powershell terminal for windows).

activate the python virtual environment: .venv\Scripts\activate

**** if there are problems activating the Virtual Environment write this:
Set-ExecutionPolicy Unrestricted -Scope Process

install flask and all dependencies: pip install -r requirements.txt

run the app: flask run 

look for the port number on the terminal output  

Open the browser, by writing localhost:XXXX, where XXXX is the port number on the terminal output  

# Communication Contract to use the Currency App as as Microservice:
### how to programmatically REQUEST data from the microservice (call example)
-> to request data from the microservice there are two required parameters that refer to the currency of origin and currency of destination (origin, destination), and an optional parameter that refers to the quantity of money to convert from one currency to the other (quantity). This would have a request address of the following form:
http://localhost:5000/get_exchange_rate?origin={origin}&destination={destination}&quantity={quantity}

or (since quantity is optional):
http://localhost:5000/get_exchange_rate?origin={origin}&destination={destination}

example:
The url to request data to convert 10000000 GBP to COP would be:
http://localhost:5000/get_exchange_rate?origin=GBP&destination=COP&quantity=10000000

### how to programmatically RECEIVE data from the microservice
following the given example, the data received (JSON) would be:
{
  "from_currency": "GBP",
  "quantity": 10000000.0,
  "result": "50690000000.0",
  "to_currency": "COP"
}

### UML sequence diagram showing how requesting and receiving data works

