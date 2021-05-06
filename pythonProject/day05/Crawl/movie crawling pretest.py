from bs4 import BeautifulSoup
from urllib import request

movie_list = ['공상과학,판타지', '공포', '다큐멘터리']
code_list = ['13', '10', '7']

for index in range(len(code_list)):
    con = request.urlopen('https://play.google.com/store/movies/category/' + code_list[index]) #연결부품 획득
    doc = BeautifulSoup(con, 'html.parser')

    movie_name = doc.select('div.WsMG1c.nnK0zc')
    movie_cost = doc.select('span.VfPpfd.ZdBevf.i5DZme')

    name = movie_name.text
    cost = movie_cost.text
    print(name)
    print(cost)

    file = open(movie_list[index] + '.txt', 'w')
    file.write(name + ':')
    file.write(cost + '\n')
    file.close()
    print(movie_list[index])
    print()
    print('---------------------------------')
