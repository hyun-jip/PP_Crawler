from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def select_date(START_YEAR, END_YEAR, START_MONTH, END_MONTH):
  DATE_LIST = []
  for i in range(END_YEAR-START_YEAR+1):
    if((START_YEAR==END_YEAR) and (START_MONTH > END_MONTH)):
      break  
    for j in range(12):
        DATE_LIST.append([START_YEAR,START_MONTH])
        START_MONTH = START_MONTH+1
        if(START_MONTH == 12):
            START_MONTH = 0
            START_YEAR = START_YEAR+1
            break
        if((START_YEAR==END_YEAR) and (START_MONTH==END_MONTH+1)):
            break
    if((START_YEAR==END_YEAR) and (START_MONTH==END_MONTH+1)):
            break
  if(DATE_LIST==[]):
      print("날짜 선택을 다시해주세요.")
  return DATE_LIST



def crawl_data(driver, DATE_LIST, PP_ID):
  DATA_LIST = []
  for i in range(len(DATE_LIST)):
     wait = WebDriverWait(driver, 10)       
     select_year = Select(driver.find_element_by_id('SEARCH_YEAR'))
     select_month = Select(driver.find_element_by_id('SEARCH_MONTH'))
     select_year.select_by_index(DATE_LIST[i][0])
     select_month.select_by_index(DATE_LIST[i][1])

     wait.until(EC.invisibility_of_element((By.CLASS_NAME, 'loadingwrap')))
     ActionChains(driver).double_click(on_element=driver.find_element_by_class_name('search_btn')).perform()
     wait.until(EC.invisibility_of_element((By.CLASS_NAME, 'loadingwrap')))

     table = driver.find_element_by_class_name('ui-jqgrid-btable')
     tbody = table.find_element_by_tag_name("tbody")
     rows = tbody.find_elements_by_tag_name("tr")

     print(f"{DATE_LIST[i][0]+2017}년 {DATE_LIST[i][1]+1}월 데이터 수집중...")

     for index, value in enumerate(rows):
       if(value.find_elements_by_tag_name("td")[0].text=="" or value.find_elements_by_tag_name("td")[0].text=="-"):
         continue
       DATE_FORMAT_1 = str(DATE_LIST[i][0]+2017) + value.find_elements_by_tag_name("td")[0].text[0:2] + value.find_elements_by_tag_name("td")[0].text[4:6]
       DATA_LIST.append({"PP_ID": PP_ID, "DATE": DATE_FORMAT_1 , "USAGE": value.find_elements_by_tag_name("td")[1].text})

     for index, value in enumerate(rows):
       if(value.find_elements_by_tag_name("td")[4].text=="" or value.find_elements_by_tag_name("td")[5].text=="-"):
         continue
       DATE_FORMAT_2 = str(DATE_LIST[i][0]+2017) + value.find_elements_by_tag_name("td")[4].text[0:2] + value.find_elements_by_tag_name("td")[4].text[4:6]
       DATA_LIST.append({"PP_ID": PP_ID, "DATE": DATE_FORMAT_2, "USAGE": value.find_elements_by_tag_name("td")[5].text})
  return DATA_LIST