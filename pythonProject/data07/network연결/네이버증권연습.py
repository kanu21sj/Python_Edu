import requests #alt + enter하면 설치됨
import pandas as pd
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.nhn"
result = requests.get(url)

content = BeautifulSoup(result.content, "html.parser")

# content

com_list = content.findAll("a", {"class": "tltle"})
# print(com_list[0].text)
p_list = content.findAll("td", {"class": "number"})
# print(p_list[1].text)


company_list = []
for index in range(len(com_list)):
    data = com_list[index].text
    company_list.append(data)
print(len(company_list))
print(company_list)

price_list = []
for index in range(1, len(p_list), 10):
    data = p_list[index].text.replace(",","")
    price_list.append(data)
print(len(price_list))
print(price_list)

company_list2 = tuple(company_list)
print(company_list2)
price_list2 = tuple(price_list)
print(price_list2)

import mysql_movie.trade_crud as db

# 다수의 항목에 여러개 데이터를 넣으려면 zip함수 사용해야 함
# zip이 for문을 알아서 돌려서 list로 title, jumsu로 묶어줌
total = tuple(list(zip(company_list2, price_list2)))
print(total)
print('----------------------------------')
# db.create(total)