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

team_item = driver.find_element(By.CLASS_NAME, "sc-team__item")
# print(team_item.find_element(By.CLASS_NAME, "sc-team__menuItem").text)  # value: チーム情報
team_info_url = team_item.find_element(By.TAG_NAME, "a").get_attribute("href")  # チーム情報のURL取得
# 「チーム情報」へ遷移
driver.get(team_info_url)

# 「順位」のデータを取得
team_rank_info_col = driver.find_element(By.CLASS_NAME, "sc-tableTeamRank")
print(team_rank_info_col.text)
# 順位 勝点 試合数 勝数 引分数 敗数 得点 失点 得失点差
# 14 16 15 4 4 7 18 32 -14


# TODO pandasでDataFrameに変換
# TODO 取得した「順位」データをcsvファイルに保存
# TODO 全チームの順位データを取得



