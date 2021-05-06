# Python program to convert the currency
# of one country to that of another country 
  
# Import the modules needed
import os
import json
import requests
from dotenv import load_dotenv

from app import APP_ENV

load_dotenv()
  

# source for code below: https://www.geeksforgeeks.org/currency-converter-in-python/


class Currency_convertor:
    # empty dict to store the conversion rates
    rates = {} 
    def __init__(self, url):
        data = requests.get(url).json()
  
        # Extracting only the rates from the json data
        self.rates = data["rates"] 
  
    # function to do a simple cross multiplication between 
    # the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR' :
            amount = amount / self.rates[from_currency]
  
        # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
    
# Driver code
if __name__ == "__main__":
  
    # API key is stored in .env file
    CURRENCY_API_KEY = "ed8098eb0481545d8a4822cdd2b09f08"
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', CURRENCY_API_KEY)  
    c = Currency_convertor(url)
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))
  
    c.convert(from_country, to_country, amount)