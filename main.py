from selenium import webdriver
import time
import random

f = open("proxy.txt", "r")
PROXYS = []
for proxy in f.readlines():
        PROXYS.append(proxy)
f.close()
n = random.randint(0, (PROXYS.__len__())-1)
print('Proxy usato: '+PROXYS.__getitem__(n))
mask = PROXYS.__getitem__(n)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://%s' % mask)
n = int(input('Inserisci numero visite da generare:'))
sito = str(input('Inserisci URL sito da visualizzare:'))
i = 0
chrome = webdriver.Chrome(chrome_options=chrome_options)
while i < n:
    chrome.get(sito)
    print('Richiesta eseguita')
    i += 1
    time.sleep(15)
chrome.close()
