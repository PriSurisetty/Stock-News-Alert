import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

YESTERDAYS_DATE = "2024-07-22"
PREV_DATE = "2024-07-19"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
WHATSAPP_PHONE_NUMBER = os.environ.get("WHATSAPP_PHONE_NUMBER")


# Documentation for Stock Data : https://www.alphavantage.co/documentation/#daily

apikey = os.environ.get("apikey")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": apikey

}

news_parameters = {
    "q": COMPANY_NAME,
    "from": YESTERDAYS_DATE,
    "language": "en",
    "apiKey": NEWS_API_KEY,
    "sortBy": "popularity"
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()

data = response.json()


"""Getting closing prices"""
yesterdays_c_price = float(data["Time Series (Daily)"][YESTERDAYS_DATE]["4. close"])


prev_day_c_price = float(data["Time Series (Daily)"][PREV_DATE]["4. close"])


"""Finding the positive & percent difference between the two prices"""
pos_difference = float(yesterdays_c_price) - float(prev_day_c_price)

up_down = None
if pos_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percent_difference = round((pos_difference / float(yesterdays_c_price)) * 100)

""" If percentage is greater than 5 then get the news data."""

response2 = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
response2.raise_for_status()

news_data = response2.json()

articles = news_data["articles"][:3]


formatted_articles = [(f"Headline: {STOCK_NAME}: {up_down}{percent_difference}%\n{articles["title"]}\nBrief: "
                       f"{articles["description"]}") for articles in articles]


client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        from_=f'whatsapp:{WHATSAPP_PHONE_NUMBER}',
        body=article,
        to=f'whatsapp:{PHONE_NUMBER}',
    )

