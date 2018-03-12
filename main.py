import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import urllib
import util

url=input("Enter the 9gag section url(in apostrophes): ")
im_l=input("Enter max number of images to download(if all, input all): ")

def Access(url, im_limit):

	chrome_options = Options()
	chrome_options.add_argument('headless')
	chrome_options.add_argument('start-maximized')
	

	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.get(url)
	
	util.image_download_handler(driver,im_limit)
	driver.close()

Access(url,im_l)
