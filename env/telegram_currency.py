import requests
import json
from dotenv import load_dotenv
import os 
from telegram_currency import telegram_currency

load_dotenv()
key = os.environ.get('ECXHANGERATE_API')
def valut(val):
	url = f'https://v6.exchangerate-api.com/v6/{key}/latest/{val.upper()}'

	response = requests.get(url)
	dict_response = json.loads(response.text)
	valuts = dict_response.get('conversion_rates')
	new_str = ""
	for new_valut in valuts:
		new_str += new_valut + ": " + str(valuts[new_valut]) 
	return new_str

# print(get_weather('Бишкек'))

