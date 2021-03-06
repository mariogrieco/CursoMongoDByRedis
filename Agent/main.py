import requests
import pymongo

API_URL = 'https://api.coinmarketcap.com/v1/ticker/'

# Establecer conexión con la base de datos
def get_db_connection(uri):
    client = pymongo.MongoClient(uri)
    return client.cryptongo

def get_cryptocurrencies_from_api():
    req = requests.get(API_URL)
    if req.status_code == 200:
        result = req.json()
        return result
    raise Exception('API Error')

def check_if_exists(db_connection, ticker_data=None):
    if not ticker_data:
        return False
    
    if db_connection.tickers.find_one({'ticker_hash': 's'}):
        return True

    return False

def save_ticker(db_connection, ticker_data=None):
    if not ticker_data:
        return False

    if check_if_exists(db_connection, ticker_data):
        return False

    # Casting

    ticker_data['rank'] = int(ticker_data['rank'])
    ticker_data['last_updated'] = int(ticker_data['last_updated'])

    # Insertar documento en la coleccion de mongoDB
    db_connection.tickers.insert_one(ticker_data)

    return True
