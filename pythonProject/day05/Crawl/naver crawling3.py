# import bs4
from bs4 import BeautifulSoup
from urllib import request

name_list = ['삼성전자', '카카오', '현대자동차']
code_list = ['005930', '035720', '005380']
for index in range(len(code_list)):
    con = request.urlopen('https://finance.naver.com/item/main.nhn?code=' + code_list[index]) #연결부품 획득
# print('1. 연결 성공', con)
# name = '삼성전자'
    doc = BeautifulSoup(con, 'html.parser')
# print('2. 받은 것을 프린트 >> ', doc)
# doc안에는 naver.com에 첫페이지인 index.html 파일의 소스가 통째로 들어있음.
    span_code = doc.select('span.code') #검색의 결과를 리스트!!
# print('code의 개수 >> ', len(span_code))
    code = span_code[0].text
    print('code: ', code)

# div_today = doc.select('div.today') #검색의 결과를 리스트!!
# print(div_today[0])
# today1 = div_today[0].select('span.blind') #검색의 결과는 리스트!
# print(today1[0])
# print(today1[0].text)

    span_blind = doc.select('span.blind')
# print(len(span_blind))
# print(span_blind[0])
# print(span_blind[1])
# print(span_blind[2])

# for index in range(len(span_blind)):
#     print(index, ': ', span_blind[index].text)
# 전일, 고가, 시가, 저가
# yes, high, start, low

    yes = span_blind[15].text
    print('전일: ', yes)
    high = span_blind[16].text
    print('고가: ', high)
    start = span_blind[19].text
    print('시가: ', start)
    low = span_blind[20].text
    print('저가: ', low)

# all = doc.select('div.today span.blind') #div 안에 있는 것 중에 span을 찾아라
# print(len(all))
# print(all[0])

    file = open(name_list[index] + '.txt', 'w')
    file.write(code + '\n')
    file.write(yes + '\n')
    file.write(high + '\n')
    file.write(start + '\n')
    file.write(low + '\n')
    file.close()
    print(name_list[index])
    print()
    print('---------------------------------')