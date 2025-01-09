import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    "User-Agent": "user agent of the device",
    "Accept-language": "accept language of device"
}

response = requests.get(url= url, headers= headers)
webp = response.text

soup = BeautifulSoup(webp, "html.parser")
price = soup.find(class_="a-price-whole").getText()
price_decimal = soup.find(class_="a-price-fraction").getText()
product_price = float(price + price_decimal)

load_dotenv()

my_email = os.getenv('GMAIL_MAIL')
password = os.getenv('PASSWORD_MAIL')

if product_price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # in order not to use connection.close()
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="end email acc",
                            msg=f"Subject:Price Checker!\n\n The price of the Rice cooker is now ${product_price}!"
                                f" Get Yours now!")
else:
    pass
