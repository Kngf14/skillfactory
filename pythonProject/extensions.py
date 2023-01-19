import requests
import json
from config import keys

class ConvertionException(Exception): #Исключения
    pass

class ExchangeConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base or keys[quote] == keys[base]:
            raise ConvertionException(f'Одинаковые валюты равны.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base