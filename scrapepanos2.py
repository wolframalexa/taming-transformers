from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

file = open('panos.txt', 'a')
driver = webdriver.Chrome('/mnt/c/Program Files (x86)/chromedriver.exe')

# go to each page of website
for i in range(0,10):
	driver.get('https://pixexid.com/tag/360?page=' + str(i))
