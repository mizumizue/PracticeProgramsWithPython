import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = os.getenv("CHROME_DRIVER_PATH")
driver = webdriver.Chrome(chromedriver)
url = "https://yahoo.co.jp"
driver.get(url)

# 検索欄を取得して、キーワード検索
seatch_input = driver.find_element_by_id("srchtxt")
if seatch_input.is_displayed:
    seatch_input.send_keys("今日の献立" + Keys.ENTER)
    seatch_input.submit

driver.close()
driver.quit()
