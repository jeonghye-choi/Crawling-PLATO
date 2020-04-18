import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr = 'ID'
pwd = 'PASSWORD'


## 부산대학교 홈페이지 열기

path = "https://plato.pusan.ac.kr/"
# Chrome WebDriver를 이용해 Chrome 실행
driver = webdriver.Chrome('C:\Program Files (x86)\Python\chromedriver.exe')   
driver.get(path)
time.sleep(2)

assert "부산대학교" in driver.title

## 로그인하기

# html element 이름을 찾습니다! 아이디비번
inputElement = driver.find_element_by_id('input-username') # 아이디 입력란 id 찾아 커서 둠
inputElement.send_keys(usr) # 커서 위치한 곳에 값을 넣음
inputElement = driver.find_element_by_id('input-password') # 비번 입력란 id 찾아 커서 둠
inputElement.send_keys(pwd) # 커서 위치한 곳에 값을 넣음
inputElement.send_keys(Keys.RETURN) # Enter 키를 누름

time.sleep(2)
