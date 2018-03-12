import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import urllib

SCROLL_PAUSE_TIME = 0.5

downloadlist=[]

def image_download_handler(driver,im_limit):
	if im_limit != "all":
		while True and len(downloadlist)<im_limit:
			last_height = driver.execute_script("return document.body.scrollHeight")
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		    	time.sleep(SCROLL_PAUSE_TIME)
			new_height = driver.execute_script("return document.body.scrollHeight")
			if new_height == last_height:
				break
			last_height = new_height
			html_source = driver.page_source
			images = driver.find_elements_by_tag_name('img')
			for image in images:
				str=image.get_attribute('src')
				if(str and str.startswith('https://img-9gag-fun.9cache.com/photo/') and str not in downloadlist):
			    			downloadlist.append(str)
		cnt=0		
		d_len=len(downloadlist)
		while(cnt<im_limit and cnt<d_len):
			image_name=downloadlist[cnt][38:]
			print image_name
			urllib.urlretrieve(downloadlist[cnt],image_name)
			cnt=cnt+1
		
	else:
		while True:
			last_height = driver.execute_script("return document.body.scrollHeight")
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		    	time.sleep(SCROLL_PAUSE_TIME)
			new_height = driver.execute_script("return document.body.scrollHeight")
			if new_height == last_height:
				break
			last_height = new_height
			html_source = driver.page_source
			images = driver.find_elements_by_tag_name('img')
			for image in images:
				str=image.get_attribute('src')
				if(str and str.startswith('https://img-9gag-fun.9cache.com/photo/') and str not in downloadlist):
			    			downloadlist.append(str)
		cnt=0		
		d_len=len(downloadlist)
		while(cnt<d_len):
			image_name=downloadlist[cnt][38:]
			print image_name
			urllib.urlretrieve(downloadlist[cnt],image_name)
			cnt=cnt+1
	
	
		
