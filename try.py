import requests
import alpha_vantage

API_URL = "https://www.alphavantage.co/query"

data = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "M&M.NSE",
    "outputsize": "compact",
    "apikey": "Y6R97WE44INDGJBZ"
    }
response = requests.get(API_URL, params=data)
print(response.json())