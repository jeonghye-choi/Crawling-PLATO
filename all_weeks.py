import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# 홈페이지 열어서 로그인
## user 정보
usr = 'ID'
pwd = 'PASSWORD'

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


    #### 주차별 찾기!
    for weeks in range(1,15):
        ### 클릭한 후!
        html= driver.page_source
        soup= BeautifulSoup(html,'lxml')

        #### 과목이름
        coursename= soup.find('h2', class_="coursename")
        print(str(weeks)+ "주차 title : " + coursename.get('title') + "\n") 

        # weeks= str(weeks)
        print(str(weeks) + "주차\n")


        #### 종류구분 (종류에 따라서 처리가 다름)
        content= soup.find('li', id='section-'+ str(weeks))
        print("content : " + content.text)

        # 1. 현재 페이지에서 처리 가능한 것들
        #### 강의(클릭X, 해당페이지에 기한정보있음, 동영상url로 이동했을 때 출석체크되는지 확인해보기) - vod O
        try:
            vod= content.find_all('li', class_="vod")
            for i in vod:
                print("vod: ", i.text, "\n")
        except:
            pass
        #### 참고 공지사항 - label O
        try:
            label= content.find_all('li', class_="label")
            for i in label:
                print("label: ", i.text, "\n")
        except:
            pass

        #### 과제물(클릭해야함) - assign
        try:
            assign = content.find_all('li', class_="assign") 
            assign_num= len(assign)
            print(assign_num)
            count= 0
            print(type(weeks))

            while count<assign_num:
                assigns= driver.find_elements_by_xpath(f'//li[@id="section-{str(weeks)}"]/div[@class="content"]/ul/li[contains(@class, "assign")]//a')
                assigns[count].click()
                time.sleep(1)

                html= driver.page_source
                soup= BeautifulSoup(html, 'lxml')
                tbody= soup.find('tbody')
                print(tbody)
                driver.back()
                time.sleep(2)

                count+= 1

        except:
            pass

        #### ppt등 강의자료(클릭하면 url로 이동 가능) - url O
        try:
            url= content.find_all('li', class_="url")
            for i in url:
                link= i.find('a')
                print("url: ",link.get('href'), "\n")
        except:
            pass
