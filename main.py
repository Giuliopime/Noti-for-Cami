import random
import time

import requests
from bs4 import BeautifulSoup

inviataMailPostoDisponibile = False
inviataMailUniAggiornata = False

link_calendario = "https://tolc.cisiaonline.it/calendario.php?tolc=scienze"
link_uni = "https://offertaformativa.unitn.it/it/l/matematica/iscriversi"


def cercaPosto():
    page_calendario = requests.get(link_calendario)
    c_soup = BeautifulSoup(page_calendario.content, 'html.parser')

    table_string = str(c_soup.find_all(id="calendario")[0])
    posto_disponibile = ">posti disponibili" in table_string.lower()
    if posto_disponibile:
        # manda mail
        print("posto disponibile")
        return True
    else:
        return False


def controllaAggiornamentiUni():
    page_uni = requests.get(link_uni)
    u_soup = BeautifulSoup(page_uni.content, 'html.parser')

    string_body = str(u_soup.find_all("body"))
    if "2023" in string_body.lower():
        # manda mail
        print("sito aggiornato")
        return True
    else:
        return False


while True:
    inviataMailPostoDisponibile = cercaPosto()
    inviataMailUniAggiornata = controllaAggiornamentiUni()
    time.sleep(random.randint(180, 300))
    if inviataMailUniAggiornata and inviataMailUniAggiornata:
        exit(0)
