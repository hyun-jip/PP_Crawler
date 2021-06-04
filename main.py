from Connecting import connect_webpage
from Saving import save_to_file
from Crawling import crawl_data, select_date
from selenium import webdriver

PP_ID = input("파워플래너 ID 입력: ")
PP_PW = input("파워플래너 PW 입력: ")
print('** 데이터 수집기간을 입력하세요. 참고(년도: 2017 ~ 2023 / 월: 1 ~ 12) **')
START_YEAR = int(input("데이터 수집기간 시작년도 입력(2017~2023): "))-2017
START_MONTH = int(input("데이터 수집기간 시작월 입력(1~12): "))-1
END_YEAR = int(input("데이터 수집기간 종료년도 입력(2017~2023): "))-2017
END_MONTH = int(input("데이터 수집기간 종료월 입력(1~12): "))-1

print(f"[{START_YEAR+2017}년 {START_MONTH+1}월] 부터 [{END_YEAR+2017}년 {END_MONTH+1}월] 까지의 데이터를 수집합니다.")

PATH = 'C:/Users/10149072/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(PATH)

connect_webpage(driver, PP_ID, PP_PW)
SELECTED_DATE = select_date(START_YEAR, END_YEAR, START_MONTH, END_MONTH)
CRAWLING_DATA = crawl_data(driver, SELECTED_DATE, PP_ID)
save_to_file(CRAWLING_DATA)

