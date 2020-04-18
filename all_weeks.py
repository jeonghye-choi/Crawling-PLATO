import time
from selenium import webdriver

# 홈페이지 열기

## 홈페이지 정보
path= 'https://plato.pusan.ac.kr/'

## Chrome WebDriver 이용, Chrome 실행
driver= webdriver.Chrome('C:\Program Files (x86)\Python\chromedriver.exe')
driver.get(path)
time.sleep(2)

## 올바른 페이지로 갔는지 확인
assert "부산대학교" in driver.title