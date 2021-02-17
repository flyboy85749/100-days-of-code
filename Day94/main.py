import requests
from twilio.rest import Client
import config

STOCK_NAME = "APPN"
COMPANY_NAME = "Appian"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = config.STOCK_API_KEY
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = config.NEWS_API_KEY
TWILIO_SID = config.TWILIO_SID
TWILIO_AUTH_TOKEN = config.TWILIO_AUTH_TOKEN

ALPHA_Endpoint = "https://www.alphavantage.co/documentation/#daily"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "APPN",
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

day_before_yesterday_data = data_list[1]
day_before_yesterday_close = day_before_yesterday_data["4. close"]


difference = float(yesterday_closing_price) - float(day_before_yesterday_close)
up_down = None
if difference > 0:
    up_down = "❤"
else:
    up_down = "😣"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

# want to use title as link to article {article['url']}
    formatted_articles = [f"{STOCK_NAME}: {up_down} {diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=config.FROM_NUMBER,
            to=config.TO_NUMBER
        )


