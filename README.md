# Stock News Alert:

The Stock News Alert project is a Python script that monitors stock price changes and sends news updates if significant changes occur. 
It fetches stock data, compares closing prices between two dates, and sends WhatsApp notifications with relevant news if the price change 
exceeds a certain threshold.

<img src="https://github.com/user-attachments/assets/9bd6f943-f907-4e91-a90a-655506fa8f11" alt="description" width="300" />



## Features:

- Fetches historical stock prices from Alpha Vantage API.
- Retrieves news articles related to the stock from News API.
- Sends WhatsApp messages with news updates if the stock price change is significant.

## Requirements:

- Python 3.x
- `requests` library for making HTTP requests
- `twilio` library for sending WhatsApp messages

## Setup:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/YourUsername/Stock-News-Alert.git
    cd Stock-News-Alert
    ```

2. **Install dependencies:**

    ```bash
    pip install requests twilio
    ```

3. **Set up environment variables:**

    Create a `.env` file in the root directory and add the following lines with your respective API keys and tokens:

    ```
    NEWS_API_KEY = your_news_api_key
    TWILIO_SID = your_twilio_sid
    TWILIO_AUTH_TOKEN = your_twilio_auth_token
    PHONE_NUMBER = your_phone_number
    WHATSAPP_PHONE_NUMBER = your_whatsapp_phone_number
    ```

4. **Run the script:**

    ```bash
    python main.py
    ```

## Script Overview:

- **`main.py`**: The main script that handles:
  - Fetching stock price data from Alpha Vantage.
  - Comparing stock prices from two dates.
  - Fetching news articles related to the stock.
  - Sending WhatsApp messages with the news if the stock price change is significant.

## Notes:

- Ensure that you have a valid API key for News API and Twilio credentials.
- Replace placeholder values in the `.env` file with your actual credentials.


