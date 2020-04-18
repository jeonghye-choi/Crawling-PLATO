import time
from selenium import webdriver


## 부산대학교 홈페이지 열기

path = "https://plato.pusan.ac.kr/"
# Chrome WebDriver를 이용해 Chrome 실행
driver = webdriver.Chrome('C:\Program Files (x86)\Python\chromedriver.exe')   
driver.get(path)
time.sleep(2)

assert "부산대학교" in driver.title
