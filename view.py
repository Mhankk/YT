#!/usr/bin/python3

import time
from selenium import webdriver

#time to refresh page
Timer = 20 #refresh every 20 seconds

#youtube 
link = 'https://www.youtube.com/watch?v=axP-l0I8KD0' #put link of video in the quotation marks

#number of views
views = 1000000

driver = webdriver.Chrome()
driver.get(link)

for i in range (views):
	time.sleep(Timer)
	driver.refresh()
	print(i)
