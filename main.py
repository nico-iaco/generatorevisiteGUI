from selenium import webdriver
import time

PROXY = "122.128.109.149:80"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get("http://whatismyipaddress.com")
time.sleep(20)
chrome.get("http://facebook.com")
