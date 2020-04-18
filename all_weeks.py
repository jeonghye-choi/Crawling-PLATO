import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 홈페이지 열어서 로그인
## user 정보
usr= '201845729'
pwd= 'yeriel6409!'

## 홈페이지 정보
path= 'https://plato.pusan.ac.kr/'

## Chrome WebDriver 이용, Chrome 실행
driver= webdriver.Chrome('C:\Program Files (x86)\Python\chromedriver.exe')
driver.get(path)
time.sleep(2)

## 올바른 페이지로 갔는지 확인
assert "부산대학교" in driver.title

## 로그인
inputElement= driver.find_element_by_id('input-username')
inputElement.send_keys(usr)
inputElement= driver.find_element_by_id('input-password')
inputElement.send_keys(pwd)
inputElement.send_keys(Keys.RETURN)
time.sleep(2)


## 강의 클릭
lect_num= 8
while lect_num>0:
    lect_list = driver.find_elements_by_xpath("//li[@class='course-label-r']/div/a[@class='course-link']")[8-lect_num]
    lect_list.send_keys(Keys.ENTER)
    time.sleep(2)

    # 내용찾기

    ### 이전페이지로
    lect_num -= 1
    driver.back()