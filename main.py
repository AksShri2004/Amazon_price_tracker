import os

from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}
response = requests.get("https://www.amazon.in/MSI-Esports-Monitor-1920x1080-FreeSync/dp/B0BNGP36KY/"
                        , headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")
# print(soup)
soup_price = soup.find("span", class_="a-price-whole")
soup_price = int((soup_price.get_text().strip(".")).replace(",", ""))
# print(soup_price)

my_email = os.getenv("my_email")
password = os.getenv("password")
email = os.getenv("email")


def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Price Low BUY ASAP MONITOR, Current Price: {soup_price}"
        )


#
if soup_price <= 11000:
    send_mail()
