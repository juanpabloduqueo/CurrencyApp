import requests 

# URL of the currency APP
app_url = 'http://localhost:5000'

def exchange_rate(origin, destination, quantity=1):
    response = requests.get(f'{app_url}/get_exchange_rate?origin={origin}&destination={destination}&quantity={quantity}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f'Failed to fetch exchange rate. Status Code: {response.status_code}, Response Content: {response.text}'

if __name__ == '__main__':  
    origin = input("write the origin currency: ")
    destination = input("write the destination currency: ")
    quantity = float(input("write the quantity to convert: "))
    data = exchange_rate(origin, destination, quantity)
    print(data)
    