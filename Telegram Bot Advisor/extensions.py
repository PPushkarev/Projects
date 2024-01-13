# extensions.py

import requests
from config import keys

class ConvertionException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = keys.get(base.lower())
            quote_key = keys.get(quote.lower())

            if base_key is None or quote_key is None:
                raise ConvertionException("Некорректные названия валют. Пожалуйста, убедитесь, что вы используете корректные значения.")

            amount = float(amount)

            response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_key}&tsyms={base_key}')
            data = response.json()

            if 'Response' in data and data['Response'] == 'Error':
                raise ConvertionException(f"Ошибка при получении данных: {data['Message']}")

            total_base = data[base_key]
            result = amount * total_base

            return result

        except ValueError:
            raise ConvertionException("Количество валюты должно быть числом")