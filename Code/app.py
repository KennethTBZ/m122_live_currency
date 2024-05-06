# Created: March, 2024
# @author Aryan Bisen
# This programm makes a get request to the API of Coin Market Cap. Functions make it possable to return the current Bitcion price as well
# as the top crypto currencies by market cap. It stores it in a variable and it gets used in index.html to display the data. 


from flask import Flask, render_template
from requests import Session
import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

env_path = ".env"

load_dotenv(dotenv_path=env_path)

# Create instance of flask app to create server and debug
# Tells Flask where to look for templates
app = Flask(__name__)

#CMC class
class CMC:
    # intitialize function
    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token}
        self.session = Session()
        self.session.headers.update(self.headers)
    # Get all info from every coin
    def getAllCoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        response = self.session.get(url)
        data = response.json()['data']
        return data
    # Top Crypto currencies by market cap. Limit = 10
    def getTopCurrencies(self, limit=10):
        url = f'{self.apiurl}/v1/cryptocurrency/listings/latest'
        parameters = {'limit': limit}
        #Session is from the request library. Makes get request with the parameters
        response = self.session.get(url, params=parameters)
        data = response.json()['data']
        # Sort data based on market capitalization and return it
        # Biggest first
        sorted_data = sorted(data, key=lambda x: x['quote']['USD']['market_cap'], reverse=True)
        print("\nTop 10 cryptocurrencies by market capitalization:")
        # Loops till the top 10 are throw
        for i, currency in enumerate(sorted_data[:limit], start=1):  # Use sorted_data here
            name = currency['name']
            symbol = currency['symbol']
            price = currency['quote']['USD']['price']
            print(f"{i}. {name} ({symbol}): ${price}")
        return sorted_data
    # price still has to be defined when it's called 
    def getPrice(self, symbol):
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        parameters = {'symbol': symbol}
        #Session is from the request library. Makes get request with the parameters
        response = self.session.get(url, params=parameters)
        data = response.json()
        return data
# Send Email
def send_email(receiver_email, message):
    smtp_server = "smtp.gmail.com"
    port = 587
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    # Infos about the email
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = receiver_email
    msg['Subject'] = "Top Cryptocurrencies Prices"

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", e)

cmc = CMC(os.getenv("API_KEY"))

@app.route("/")
#main function
def home():
    #Creaet variables for bitcoin price and top currencies
    btc_price = cmc.getPrice('BTC')['data']['BTC']['quote']['USD']['price']
    top_currencies = cmc.getTopCurrencies()
    #Email
    email_message = f"Current Bitcoin Price\n${btc_price}\n\nTop 10 Cryptocurrencies\n"
    for currency in top_currencies:
        email_message += f"{currency['name']}: ${currency['quote']['USD']['price']}\n"
    receiver_email = os.getenv('RECEIVER_EMAIL')
    send_email(receiver_email, email_message)
    #BTC price and top currencies in index.html
    return render_template("index.html", btc_price=btc_price, top_currencies=top_currencies)



if __name__ == '__main__':
    app.run(debug=True,port=5501)
