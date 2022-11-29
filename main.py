from selenium import webdriver
from selenium.webdriver.common.by import By

# webdriverオブジェクトを作る (ブラウザが開く)
driver_path = "./chromedriver.exe"
driver = webdriver.Chrome()

# urlを指定してブラウザで開く
url = "https://soccer.yahoo.co.jp/ws/category/eng/schedule/202205201/16/?gk=52"
driver.get(url)

# print(driver.page_source)

item = driver.find_element(By.CLASS_NAME, "sn-notice__text")
print(item)
print(type(item))
print(item.text)

items = driver.find_elements(By.CLASS_NAME, "sc-tableGame__team")

for i in items:
    print(i.text)

# points = driver.find_elements(By.CLASS_NAME, "sc-tableGame__scoreDetail")
# for point in points:
#     print(point.text)

point = driver.find_element(By.CLASS_NAME, "sc-tableGame__scoreDetail")
print(point.text)
