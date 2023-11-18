# CurrencyApp

To start the program, go to the terminal (in my case, it's the vscode powershell terminal for windows).

activate the python virtual environment: .venv\Scripts\activate

**** if there are problems activating the Virtual Environment write this:
Set-ExecutionPolicy Unrestricted -Scope Process

install flask and all dependencies: pip install -r requirements.txt

run the app: flask run 

look for the port number on the terminal output  

Open the browser, by writing localhost:XXXX, where XXXX is the port number on the terminal output  

+++ TO CONNECT TO THE USDCOP MICROSERVICE:

* Connect to the url:

http://localhost:5000/get_exchange_rate

* This will give a value like this one in json: 

{
    "usd_cop_exchange_rate": "4079.46000000"
}