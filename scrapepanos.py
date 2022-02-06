from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

file = open('panos.txt', 'a')
driver = webdriver.Chrome('/mnt/c/Program Files (x86)/chromedriver.exe')
numpanos = 10000

# go to website
driver.get('https://istreetview.com/')

for i in range(0,numpanos):
	# click "random street view" button
	btn = driver.find_element_by_xpath('//*[@id="m_rnd_sv"]')
	driver.execute_script('arguments[0].click()', btn)

	# get current URL and extract PanoID
	currenturl = driver.current_url
	panoID = currenturl.replace("https://istreetview.com/", '')
	print(panoID)

	# write to file
	file.writelines(panoID + '\n')

	# wait so I don't get booted by Google
	time.sleep(1)
