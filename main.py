import os
import random
import time

import requests
from bs4 import BeautifulSoup
from mailersend import emails

print("Starting")

inviataMailPostoDisponibile = False
inviataMailUniAggiornata = False

mailer = emails.NewEmail()

link_calendario = "https://tolc.cisiaonline.it/calendario.php?tolc=ingegneria"
link_uni = "https://offertaformativa.unitn.it/it/l/matematica/iscriversi"


def cercaPosto():
    page_calendario = requests.get(link_calendario)
    c_soup = BeautifulSoup(page_calendario.content, 'html.parser')

    table_string = str(c_soup.find_all(id="calendario")[0])
    posto_disponibile = ">posti disponibili" in table_string.lower()
    if posto_disponibile:
        print("Posto disponibile")
        mandaMail("C'è un posto per il tolc di mate Camiiiiiii <3 " + link_calendario + " :) luv u")
        return True
    else:
        return False


def controllaAggiornamentiUni():
    page_uni = requests.get(link_uni)
    u_soup = BeautifulSoup(page_uni.content, 'html.parser')

    string_body = str(u_soup.find_all("body"))
    if "2023" in string_body.lower():
        print("Sito aggiornato")
        mandaMail("Ci sono le info per il nuovo anno sul sito di uni Trento Camiiiiiii <3 " + link_uni + " :) luv u")
        return True
    else:
        return False

# test 2
def mandaMail(testo):
    mail = os.environ.get('MAIL_CAMI')
    mail_body = {}
    mail_from = {
        "name": "G ❤️",
        "email": "me@giuliopime.dev",
    }
    recipients = [
        {
            "name": "Cami",
            "email": mail,
        }
    ]
    reply_to = [
        {
            "name": "Giulio Pimenoff",
            "email": "giuliopime@gmail.com",
        }
    ]
    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject("Cami leggimi :)", mail_body)
    mailer.set_plaintext_content(testo, mail_body)
    mailer.set_reply_to(reply_to, mail_body)
    print("Mando la mail")
    print(mailer.send(mail_body))


while True:
    print("Entered loop")
    if inviataMailPostoDisponibile is False:
        inviataMailPostoDisponibile = cercaPosto()
    if inviataMailUniAggiornata is False:
        inviataMailUniAggiornata = controllaAggiornamentiUni()
    time.sleep(random.randint(120, 180))
    if inviataMailUniAggiornata is True and inviataMailUniAggiornata is True:
        exit(0)
