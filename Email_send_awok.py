import smtplib
from bs4 import BeautifulSoup as Soup
import requests
import threading

timer = 10  # vreme provere sajta u sekundama
massage = ''


def check_flash_sale():
    global massage
    r = requests.get("http://www.awok.com/deals/")  # strana koja se proverava
    data = r.text
    soup = Soup(data, "lxml")

    for i in soup.find('div', attrs={"class": 'flashsale_productbuynow'}).find_previous_siblings('div',
                                                                        attrs={"class": 'flashsale_producttitle'}):
        item_name = str(i.text[1:-1])
        print('Trenutno na akciji je: ' + item_name)
        massage = 'Trenutno na akciji je: ' + str(i.text[1:-1])
        if item_name == 'Apple iPhone 6S, 16GB, Space Gray':  # ukoliko pronadje text za Apple, da objavi i
            # posalje email
            send_mail()
            print('Promena! Apple iPhone 6S, 16GB, Space Gray.')
        elif item_name == 'Samsung Galaxy Note 7 N930, 4G LTE, Black Onyx':  # isto kao za Apple
            send_mail()
            print('Promena! Samsung Galaxy Note 7 N930, 4G LTE, Black Onyx.')
        else:
            print('Nema promene...')


def send_mail():
    global massage
    fromaddr = 'stankovic.milos@gmail.com'
    toaddrs = 'stankovic.milos@gmail.com'
    subject = 'Subject: Promena na flash sale AWOK!\n\n'
    # body_text = subject + 'Upravo u prodaji: XXXXXXXXX!'
    massage = subject + massage

    # Credentials (if needed)
    username = 'stankovic.milos'
    password = 'Drugalozinka12!'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, massage)
    server.quit()


def regular_check():
    check_flash_sale()
    threading.Timer(timer, regular_check).start()  # definisanje provere sajta na tacno odredjeno vreme


regular_check()
