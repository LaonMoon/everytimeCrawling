from urllib.request import urlopen
import requests
import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/이름/Downloads/chromedriver_win32 (1)/chromedriver.exe')

# 처음 : 핫게 첫 페이지 게시글 url 수집

now_page1 = "https://everytime.kr/hotarticle"
now_page2 = "https://everytime.kr/hotarticle/p/2"
now_page3 = "https://everytime.kr/hotarticle/p/3"
scrapList1 = []
totalUrl1 = []
titleList = []

# 에브리타임 로그인

driver.get(now_page1)
time.sleep(0.1)

driver.find_element_by_xpath("""//*[@id="container"]/form/p[1]/input""").send_keys("아이디") # 입력 버튼 클릭.    
time.sleep(0.1)
driver.find_element_by_xpath("""//*[@id="container"]/form/p[2]/input""").send_keys("비밀번호")
time.sleep(0.1)
driver.find_element_by_xpath("""//*[@id="container"]/form/p[3]/input""").click()

for now_url in [now_page1, now_page2, now_page3]:
    for i in range(1,21):

        driver.get(now_url)
        time.sleep(0.3)
        
        pre_title = driver.find_element_by_xpath('//*[@id="container"]/div[2]/article[%s]/a/p'%i).text

        driver.find_element_by_xpath("""//*[@id="container"]/div[2]/article[%s]/a""" %i).click() # 입력 버튼 클릭.    
        time.sleep(0.3)
        now_url1 = driver.current_url
        
        try:
            scrapData1 = driver.find_element_by_xpath('//*[@id="container"]/div[2]/article/a/ul[2]/li[4]').text
            scrapList1.append(scrapData1)
        except:
            scrapData1 = driver.find_element_by_xpath('//*[@id="container"]/div[2]/article/a/ul[2]/li[3]').text
            scrapList1.append(scrapData1)
            
        try:
            titleData1 = driver.find_element_by_xpath('//*[@id="container"]/div[2]/article/a/h2').text
            titleList.append(titleData1)
        except:
            titleList.append(pre_title)
    
        totalUrl1.append(now_url1)

new_ScrapList = []
index = 0

for i in range(len(scrapList1)):
    if int(scrapList1[i])>5:
        new_ScrapList.append(index)
    index = index + 1

print("<hot 게시판 스크랩 10개 이상 글들>")
print()

for i in new_ScrapList:
    print(titleList[i])
    print(totalUrl1[i])
    print()

scrapList2 = []
totalUrl2 = []
titleList2 = []

inform_page1 = "https://everytime.kr/375125"
inform_page2 = "https://everytime.kr/375125/p/2"

for now_url in [inform_page1]:
    for i in range(1,21):
        
        driver.get(now_url)
        time.sleep(0.3)

        driver.find_element_by_xpath("""//*[@id="container"]/div[3]/article[%s]/a""" %i).click() # 입력 버튼 클릭.   
        
        time.sleep(0.3)
        now_url1 = driver.current_url
        
        try:
            scrapData1 = driver.find_element_by_xpath('//*[@id="container"]/div[3]/article/a/ul[2]/li[4]').text
            scrapList2.append(scrapData1)
        except:
            scrapData1 = driver.find_element_by_xpath('//*[@id="container"]/div[3]/article/a/ul[2]/li[3]').text
            scrapList2.append(scrapData1)
            

        titleData1 = driver.find_element_by_xpath('//*[@id="container"]/div[3]/article/a/h2').text
        titleList2.append(titleData1)
        
        totalUrl2.append(now_url1)
        
print(scrapList2)

second_ScrapList = []
index = 0

for i in range(len(scrapList2)):
    if int(scrapList2[i])>5:
        second_ScrapList.append(index)
    index = index + 1

print("정보 게시판 스크랩 5개 이상인 글")

for i in second_ScrapList:
    print(titleList2[i])
    print(totalUrl2[i])

totalUrl3 = []
titleList3 = []

#소융 검색 결과
sw_page = "https://everytime.kr/search/all/%EC%86%8C%EC%9C%B5"
#컴공 검색 결과
com_page = "https://everytime.kr/search/all/%EC%BB%B4%EA%B3%B5"
#개발자 검색 결과
dev_page="https://everytime.kr/search/all/%EA%B0%9C%EB%B0%9C%EC%9E%90"

for now_url in [sw_page,com_page,dev_page]:
    for i in range(1,12):
        
        driver.get(now_url)
        time.sleep(0.3)
        
        pre_title = driver.find_element_by_xpath('//*[@id="container"]/div[2]/article[%s]/a/p'%i).text
        
        driver.find_element_by_xpath("""//*[@id="container"]/div[2]/article[%s]/a""" %i).click() # 입력 버튼 클릭.   
        
        time.sleep(0.3)
        now_url1 = driver.current_url
            
        try:
            titleData1 = driver.find_element_by_xpath('//*[@id="container"]/div[2]/article/a/h2').text
            titleList3.append(titleData1)
        except:
            titleList3.append(pre_title)
        
        totalUrl3.append(now_url1)

print("소융 검색 글들")
print()
for i in range(11):
    print(titleList3[i])
    print(totalUrl3[i])
    print()
    
print("컴공 검색 글들")
print()
for i in range(11,21):
    print(titleList3[i])
    print(totalUrl3[i])   
    print()    

print("개발자 검색 글들")
print()

for i in range(21,31):
    print(titleList3[i])
    print(totalUrl3[i]) 
    print()

totalUrl4 = []
titleList4 = []

#소융/컴공 게시판 주소
swcom_page = "https://everytime.kr/462636"

for now_url in [swcom_page]:
    for i in range(1,11):
        
        driver.get(now_url)
        time.sleep(0.3)
        
        pre_title = driver.find_element_by_xpath('//*[@id="container"]/div[2]/article[%s]/a/p'%i).text

        driver.find_element_by_xpath("""//*[@id="container"]/div[2]/article[%s]/a""" %i).click() # 입력 버튼 클릭.   
        time.sleep(0.3)
        now_url1 = driver.current_url
            
        titleData1 = pre_title
        titleList4.append(titleData1)
        
        totalUrl4.append(now_url1)

print("소융/컴공 게시판 글들")
print()
for i in range(10):
    print(titleList4[i])
    print(totalUrl4[i])
    print()

driver.quit()
