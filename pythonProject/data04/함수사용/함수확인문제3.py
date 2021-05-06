from 함수정의.문제함수 import *

# 문제7 : exam07()
missile_name = input('미사일 이름은>> ')
missile_start = int(input('미사일 시작값은>> '))
missile_move = float(input('미사일 움직이는 값은>> '))
missile(missile_name, missile_start, missile_move)

# 문제8 : exam08()
money = int(input('받은 돈>> '))
cost = int(input('상품의 총액>> '))

change(money, cost)

# 문제9 : exam09()
for x in range(1000):
    print('*', end='')