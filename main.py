from selenium import webdriver
import time

PROXY = "122.128.109.149:80"        #Funziona solo per le richieste http e non per quelle https

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
n = int(input('Inserisci numero visite da generare:'))
sito = str(input('Inserisci URL sito da visualizzare:'))
i = 0
chrome = webdriver.Chrome(chrome_options=chrome_options)
while i < n:
    chrome.get(sito)
    print('Richiesta eseguita')
    i += 1
    time.sleep(20)