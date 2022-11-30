from selenium import webdriver
from selenium.webdriver.common.by import By

# webdriverオブジェクトを作る (ブラウザが開く)
driver_path = "./chromedriver.exe"
driver = webdriver.Chrome()

# urlを指定してブラウザで開く
url = "https://soccer.yahoo.co.jp/ws/category/eng/teams"
driver.get(url)

# チーム名の取得
teams = driver.find_elements(By.CLASS_NAME, "sc-team__title")

teams_list = []  # チーム名のリスト

for team in teams:
    if team.text != "":
        teams_list.append(team.text)

print(f"teams_list: {teams_list}")

# TODO 「チーム情報」をクリック
# TODO 「sc-tableTeamRank__data」のデータを取得


# points = driver.find_elements(By.CLASS_NAME, "sc-tableGame__scoreDetail")
# for point in points:
#     print(point.text)

# スコアを取得 例 1 - 2
# point = driver.find_element(By.CLASS_NAME, "sc-tableGame__scoreDetail")
# print(point.text)

