import requests #alt + enter하면 설치됨
import pandas as pd
from bs4 import BeautifulSoup

# 크롤링 하려는 url 불러오기
url = "https://movie.naver.com/movie/running/current.nhn"
result = requests.get(url)
# print(result.content)

# url 가져온 결과값 html로 파싱(데이터를 분석하여 원하는 형태로 조립하고 빼내는 것)
content = BeautifulSoup(result.content, "html.parser")

# content

# 가져오려는 jsp 태그의 클래스명
dt_list = content.findAll("dt", {"class": "tit"})
# dt_list: ResultSet class의 객체, LIST의 상속!
# 인덱싱과 슬라이싱이 된다.

print(type(dt_list)) #ResultSet 클래스의 객체
# print(dt_list) 전체 목록 프린트
print('리스트의 개수>> ', len(dt_list)) #리스트의 개수
print(dt_list[0])
tag = dt_list[0].find("a") #a태그 안에 있는 값을 가져옴
print(tag)
print(type(tag))
print(tag.text) #태그 안에 있는 텍스트 가져옴

num_list = content.findAll("span", {"class": "num"})
# dt_list: ResultSet class의 객체, LIST의 상속!
# 인덱싱과 슬라이싱이 된다.

print(num_list)
print('num_list의 개수>> ', len(num_list))
print(num_list[0])
tag2 = num_list[0]
print(type(tag2))
print(tag2.text)
print('-----------------------------')


test_list = [1, 2, 3, 4]
for item in test_list:
    print(item)

for index in range(0, len(test_list)): #0~2, 인덱싱 주고 리스트 돌릴때
    print(test_list[index])
print('-----------------------------')

for index in range(0, len(num_list), 2):
    print(num_list[index].text) # 2개씩 점프한 값(평점)의 숫자만 가져오기(.text)
print('-----------------------------')


title_list = []
for tag in dt_list:
    print(tag.find('a').text) # dt_list의 a태그 안, 텍스트 가져오기
    data = tag.find('a').text
    title_list.append(data) # 데이터를 title_list에 계속 누적 시킴
print(len(title_list))
print(title_list)

jumsu_list = []
for index in range(0, 145):
    data = num_list[index].text
    jumsu_list.append(data)
print(len(jumsu_list))
print(jumsu_list)

# tuple의 tuple로 바꿔주면 데이터를 insert하기 쉬움
title_list2 = tuple(title_list)
print(title_list2)

jumsu_list2 = tuple(jumsu_list)
print(jumsu_list2)

import mysql_movie.movie_crud as db

# 다수의 항목에 여러개 데이터를 넣으려면 zip함수 사용해야 함
# zip이 for문을 알아서 돌려서 list로 title, jumsu로 묶어줌
total = list(zip(title_list2, jumsu_list2))
print(len(total))
print(type(total))
print(total)
total2 = tuple(total)
print(total2)
print('----------------------------------')
db.create(total2)