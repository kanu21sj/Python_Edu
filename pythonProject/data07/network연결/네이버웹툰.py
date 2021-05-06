import requests #alt + enter하면 설치됨
import pandas as pd
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
result = requests.get(url)

content = BeautifulSoup(result.content, "html.parser")

# content

t_list = content.findAll("div", {"class": "genreRecomInfo"})
# print(tag)
w_list = content.findAll("a", {"class": "user"})
# print(tag2)
j_list = content.findAll("div", {"class": "rating_type"})
# print(tag3)

title_list = []
for index in range(0, 9):
    data = t_list[index].find("a").text
    title_list.append(data)
print(len(title_list))
print(title_list)

writer_list = []
for index in range(0, 9):
    data = w_list[index].text
    writer_list.append(data)
print(len(writer_list))
print(writer_list)

jumsu_list = []
for index in range(0, 9):
    data = j_list[index].find("strong").text
    jumsu_list.append(data)
print(len(jumsu_list))
print(jumsu_list)

title_list2 = tuple(title_list)
print(title_list2)
writer_list2 = tuple(writer_list)
print(writer_list2)
jumsu_list2 = tuple(jumsu_list)
print(jumsu_list2)

import mysql_movie.webtoon_crud as db

# 다수의 항목에 여러개 데이터를 넣으려면 zip함수 사용해야 함
# zip이 for문을 알아서 돌려서 list로 title, jumsu로 묶어줌
total = list(zip(title_list2, writer_list2, jumsu_list2))
print(len(total))
print(type(total))
print(total)
total2 = tuple(total)
print(total2)
print('----------------------------------')
db.create(total2)