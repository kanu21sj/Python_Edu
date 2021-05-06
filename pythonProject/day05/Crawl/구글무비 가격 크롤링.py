from bs4 import BeautifulSoup
from urllib import request

movie_list = ['공상과학,판타지', '공포', '다큐멘터리', '드라마', '미스테리,서스펜스', '애니메이션', '액션,어드벤처', '코미디', '키즈']
code_list = ['13', '10', '7', '6', '11', '2', '1', '4', '8']

for index in range(len(code_list)):
    con = request.urlopen('http://play.google.com/store/movies/category/' + code_list[index])
    doc = BeautifulSoup(con, 'html.parser')

    movie_name = doc.select('div.WsMG1c.nnK0zc')
    movie_cost = doc.select('span.VfPpfd.ZdBevf.i5DZme')

    file = open(movie_list[index] + '.txt', 'w', -1, encoding='utf-8')
    for i in range(len(movie_name)):
        name = movie_name[i].text
        cost = movie_cost[i].text

        file.write(name + ' : ')
        file.write(cost + '\n')
    file.close()
    print(movie_list[index])
    print()
    print('--------------------------------')