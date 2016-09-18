import smtplib


def sendemail(from_addr, to_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    # header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    server.sendmail(from_addr, to_addr_list, message)
    server.quit()

 sendemail(from_addr='xx@xx.com' ,
           to_addr_list=['xx@xx.com'],
           # cc_addr_list=['RC@xx.co.uk'],
           subject='Howdy',
           message='Howdy from a python function',
           login='xx@xx.com',
           password='xxx')


