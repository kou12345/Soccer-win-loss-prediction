from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

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


all_team_items = driver.find_elements(By.CLASS_NAME, "sc-team__item")

all_team_url = []

for i in all_team_items:
    all_team_url.append(i.find_element(By.TAG_NAME, "a").get_attribute("href"))

print(all_team_url)

tmp_list = [[]]

# 全チームの順位データを取得
for team_url in all_team_url:
    # 遷移
    driver.get(team_url)
    # 成功
    team_rank_info = driver.find_element(By.CLASS_NAME, "sc-tableTeamRank__row").text
    print(driver.find_element(By.CLASS_NAME, "sc-tableTeamRank__row").text)

    tmp_list.append(team_rank_info.split())

# 先頭の空listを削除
del tmp_list[0]
print(tmp_list)


# TODO pandasでDataFrameに変換
# TODO 取得した「順位」データをcsvファイルに保存


