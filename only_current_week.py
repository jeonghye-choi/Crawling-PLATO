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


## 강의클릭하기

lect_num = 8
while lect_num >0 :

    lect_list = driver.find_elements_by_xpath("//li[@class='course-label-r']/div/a[@class='course-link']")[8-lect_num]  # 강의리스트 찾기

    lect_list.send_keys(Keys.ENTER) # 강의 클릭
                                    # 다른 방법(강제) - 비추
                                    # driver.execute_script("arguments[0].click();", i)
    time.sleep(2)

    # 내용가져오기


    # 이전 페이지로
    lect_num -= 1
    driver.back()  # 이전 페이지로 이동
    time.sleep(2)
