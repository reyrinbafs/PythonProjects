import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "VVHZQNOXLLPHNJJY"
NEWS_API_KEY = "6cf99288bc0d4402af7817a7d8ef3ee7"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
#  [new_value for (key, value) in dictionary.items()]
parameters = {
    "apikey": API_KEY,
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
data_list = [value for (key, value) in stock_data["Time Series (Daily)"].items()]
yesterday_close_prize = data_list[0]['4. close']
yesterday_open_prize = data_list[0]['1. open']

# TODO 2. - Get the day before yesterday's closing stock price
day_bef_close_prize = data_list[1]['4. close']
day_bef_open_prize = data_list[1]['1. open']

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp

diff = abs(float(day_bef_close_prize) - float(yesterday_close_prize))
print(diff)


# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.

diff_percent = round((diff / float(yesterday_close_prize)), 2) * 100
print(diff_percent)


## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 1:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]


    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint:
    #  https://stackoverflow.com/questions/509211/understanding-slice-notation

    news_top = news_data[:3]
    print(news_top[0]['title'])


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_article = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in news_top]
    print(formatted_article)

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
