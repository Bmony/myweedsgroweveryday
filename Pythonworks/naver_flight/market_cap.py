import time
from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)
time.sleep(1)
# 첫 팝업 화면 끄기
close = browser.find_element(By.XPATH,'//div[@class="btns"]')
close.click()

begin_date = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
begin_date.click()

time.sleep(1)
day27 = browser.find_elements(By.XPATH, '//b[text()="27"]')
day27[0].click()

time.sleep(1)
day31 = browser.find_elements(By.XPATH, '//b[text()="31"]')
day31[0].click()

time.sleep(1)
arrival = browser.find_element(By.XPATH, '//b[text()="도착"]')
arrival.click()

time.sleep(1)
domestic = browser.find_element(By.XPATH, '//button[text()="국내"]')
domestic.click()

time.sleep(1)
jeju = browser.find_element(By.XPATH, '//i[text()="제주국제공항"]')
jeju.click()

time.sleep(1)
search = browser.find_element(By.XPATH, '//span[text()="항공권 검색"]')
search.click()

time.sleep(5)
require = browser.find_element(By.XPATH, '//button[text()="출발시각 빠른 순"]')
require.click()

time.sleep(2)
row_price = browser.find_element(By.XPATH, '//span[text()="가격 낮은 순"]')
row_price.click()

time.sleep(5)
elem = WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))

for i in elem:
    print(i.text)