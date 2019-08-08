import requests
from bs4 import BeautifulSoup
import selenium
import  smtplib
import time

URL='https://ethereumprice.org/btc/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    global price
    price = soup1.find(class_="value").get_text().strip()
    converted_price = float(price[0:6].replace(',','.'))
    print(converted_price)

    if(converted_price < 10.500):
        send_mail()



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('weto1337@gmail.com', 'iqeclbzyrygrmhlv')

    subject = "Bitcoin price fell down!"
    body = 'Price of bitcoing fell down to ' + price[0:6] + '$ | https://bitbay.net/pl/kursy-walut'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'weto1337@gmail.com',
        'weto1337@gmail.com',
        msg
    )
    print("Mail has been sent")

    server.quit()

while(True):
    check_price()
    time.sleep(500)



