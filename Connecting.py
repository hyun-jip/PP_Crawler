from selenium.webdriver.common.keys import Keys

def connect_webpage(driver, PP_ID, PP_PW):
  driver.get("https://pp.kepco.co.kr/")
  assert "한전 파워플래너" in driver.title
  
  input = driver.find_element_by_id("RSA_USER_ID")
  input.send_keys(PP_ID)
  input = driver.find_element_by_id("RSA_USER_PWD")
  input.send_keys(PP_PW)
  input.send_keys(Keys.RETURN)

  driver.get("https://pp.kepco.co.kr/rs/rs0102.do?menu_id=O010202")
