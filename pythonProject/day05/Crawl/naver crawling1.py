# import bs4
from bs4 import BeautifulSoup
from urllib import request

con = request.urlopen('http://www.naver.com') #연결부품 획득
print('1. 연결 성공', con)

doc = BeautifulSoup(con, 'html.parser')
# print('2. 받은 것을 프린트 >> ', doc)
# doc안에는 naver.com에 첫페이지인 index.html 파일의 소스가 통째로 들어있음.
a_nav = doc.select('a.nav') #검색의 결과를 리스트!!
print(len(a_nav))
print(a_nav[0])
print(a_nav[0].text)





