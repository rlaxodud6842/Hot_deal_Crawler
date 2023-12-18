from selenium import webdriver
import time
from selenium.webdriver.common.by import By



url = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu' #링크 넣기

driver.get(url)
time.sleep(1)

# 링크를 주면 내가 의도한대로 파싱 해서 알려주는것
# 추가로 주기적으로 알려주는거
# 유저시스템 도입

aa = driver.find_elements(By.CLASS_NAME,"list_title")
for i,item in enumerate(aa): 
    
    print(item.text)
    
class crwaler():
    def __init__(self,url):
        self.driver = webdriver.Chrome()
        
    def read_item_pp(self):
        pass
    
    
    
        
        