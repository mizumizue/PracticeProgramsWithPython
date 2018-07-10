import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 転職サイトGreen
BASE_URL = "https://www.green-japan.com/"
EMAIL = os.getenv('GREEN_EMAIL')
PASSWORD = os.getenv('GREEN_PASSWORD')

# ドライバ読み込み
chromedriver = os.getenv('CHROME_DRIVER_PATH')
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(30)

# クローリング開始、ログイン画面に遷移
# TODO 例外処理
driver.get(BASE_URL + "login")
mail_input = driver.find_element_by_id('user_mail')
mail_input.send_keys(EMAIL)
password_input = driver.find_element_by_id('user_password')
password_input.send_keys(PASSWORD)
password_input.submit()

# クローリング
driver.get(BASE_URL + "search_key/01?case=tlogin")
search_div_id = os.getenv('SEARCH_SELECT_DIV_ID')
search_select_div = driver.find_element_by_id(div_id)
search_select_div.click()

# DB保存

# クローリング終了
driver.close()
driver.quit()