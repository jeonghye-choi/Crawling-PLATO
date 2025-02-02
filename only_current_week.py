import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

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


    # BeautifulSoup 이용해서 해당 페이지 html 파싱  --> source를 html형태로 만드는 것이기에 클릭같은 동적인 제어 X
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    coursename = soup.find('h2',class_="coursename")
    print("title : " + coursename.get('title') + "\n")

    content = soup.find_all('div', class_="content")[1]
    print("content.text : " + content.text+ "\n")


    # 교수님의 말
    try:

        label = content.find_all('li', class_="label")
        for i in label:
            print("label:  ",i.text, "\n")
    except:
        pass

    # 참고자료  (url 로 되어있으니까 연결 해주기 - url주소 가져오기)
    try:
        url = content.find_all('li', class_="url")
        for i in url:
            print("url:  ", i.text, "\n")
    except:
        pass

    # 파일
    try:
        ubfile = content.find_all('li', class_="ubfile")
        for i in ubfile:
            print("ubfile:  ",i.text, "\n")
    except:
        pass


    # 강의 ( 날짜 따로 분류하기 )
    try:
        vod = content.find_all('li', class_="vod")
        for i in vod:
            print("vod:  ", i.text, "\n")
    except:
        pass

    # 과제 ( 제한 날짜 클릭해서 찾아서 가져와야함 -> v2)
    try:
        assign = content.find_all('li', class_="assign") 
        for i in assign:
            print("assign: ", i.text,"\n")
    except:
        pass
        
    
    # 퀴즈 ( 제한 날짜 클릭해서 찾아서 가져와야함 )
    try:
        quiz = content.find_all('li', class_="quiz")
        for i in quiz:
            print("quiz:  ", i.text, "\n")
    except:
        pass

    print("-"*20)



    # 이전 페이지로
    lect_num -= 1
    driver.back()  # 이전 페이지로 이동
    time.sleep(2)
