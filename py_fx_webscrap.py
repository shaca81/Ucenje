from bs4 import BeautifulSoup
import requests
import logging
import threading

#  Input data section ------------------------------------------------------------------------
cur1 = input("Please enter the first currency in capital letters: ")
cur2 = input("Please enter the second currency in capital letters: ")
timer_update = 10

trade_ammount = 100.00
broker_fee = 5.00
profit_limit = 20.00
loss_limit = 10.00

#  Logging section ---------------------------------------------------------------------------

logger = logging.getLogger(cur1 + "/" + cur2)
logger.setLevel(logging.INFO)

handler = logging.FileHandler(cur1 + cur2 + '.log')  # create a file handler
handler.setLevel(logging.INFO)

#  formatter = logging.Formatter('%(asctime)s | %(name)s | %(message)s')  # create a logging format
formatter = logging.Formatter('%(asctime)s | %(message)s')  # create a logging format
handler.setFormatter(formatter)

logger.addHandler(handler)  # add the handlers to the logger

# Web crawler section ----------------------------------------------------------------------


def currency_print():

    global timer_update

    currency_pair = requests.get("http://www.investing.com/currencies/" + cur1 + "-" + cur2)
    soup = BeautifulSoup(currency_pair.text, "html.parser")

    for price in soup.find_all('span', attrs={"id": "last_last"}):
        price = float(price.text)
        print(cur1 + "/" + cur2 + " price:", price)
        logger.info(price)

    # for price_change in soup.find_all('span', attrs={"class": "arial_20 greenFont pid-1-pc"}):
    #     price_change = float(price_change.text)
    #     print(cur1 + "/" + cur2 + " price change:", price_change)
    #     logger.info(price_change)

    # for price_change_percentage in soup.find_all('span', attrs={"class": "arial_20 greenFont pid-1-pcp parenthesis"}):
    #     price_change_percentage = float(price_change_percentage.text)
    #     print(cur1 + "/" + cur2 + " price change percentage:", price_change_percentage, "%")
    #     logger.info(price_change_percentage)

    # for price_bid in soup.find_all('span', attrs={"class": "inlineblock pid-1-bid"}):
    #     price_bid = float(price_bid.text)
    #     print(cur1 + "/" + cur2 + " price bid:", price_bid)
    #     logger.info(price_bid)
    #
    # for price_ask in soup.find_all('span', attrs={"class": "inlineblock pid-1-ask"}):
    #     price_ask = float(price_ask.text)
    #     print(cur1 + "/" + cur2 + " price bid:", price_ask)
    #     logger.info(price_ask)
    #     logger.info('--------------')

    #  trade_total_amount = (trade_ammount + broker_fee) * price
    #  print("Total trade amound: ", trade_total_amount)
    threading.Timer(timer_update, currency_print).start()

    # return price


currency_print()



# Decision section ----------------------------------------------------------------------

#  Takes the price, ads a broker fee and checks if the signals on the website are buy or sell



#  Do the trade according to the signal


#  Calculate constantly what is the profit or loss and if limit is reached stop the trade
