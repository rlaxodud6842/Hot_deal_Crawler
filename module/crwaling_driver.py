from selenium import webdriver
import time
from user import User
from UserManageUnit import UserManageUnit


driver = webdriver.Chrome() 
driver.get('https://www.google.co.kr/')

time.sleep(3)