import smtplib
from bs4 import BeautifulSoup as Soup
import requests
import threading

timer = 20
massage = ''


def check_flash_sale():
    global massage
    r = requests.get("http://www.awok.com/deals/")
    data = r.text
    soup = Soup(data, "lxml")

    for i in soup.find('div', attrs={"class": 'flashsale_productbuynow'}).find_previous_siblings('div',
                                                                        attrs={"class": 'flashsale_producttitle'}):
        print('Trenutno na akciji je:' + repr(i.text))
        massage = 'Trenutno na akciji je:' + repr(i.text)
        if i.text == 'Apple iPhone 6S, 16GB, Space Gray':
            send_mail()
            print('Promena!')
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
    threading.Timer(timer, regular_check()).start()


regular_check()
