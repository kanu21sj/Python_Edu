# 문제1 : exam01
def login(x, y):
    print('아이디가 ' + x + '인 ' + y + '님이 로그인되었습니다.')

# 문제2 : exam02()
def add(x, y):
    print('두 수의 합은', x - y)
def minus(x, y):
    print('두 수의 차는', x + y)
def mul(x, y):
    print('두 수의 곱은', x * y)
def div(x, y):
    print('두 수의 나눗셈은', x / y)
def left(x, y):
    print('두 수의 나머지는', x % y)

# 문제3 : exam03()
def info(x, y):
    print(x + '님의 ' + '10년 후의 나이는 ' + y + '세입니다.')

# 문제4 : exam04()
def allowance(x):
    if x > 10000:
        print('용돈이 너무 많아요')
    else:
        print('용돈이 너무 적어요')

# 문제5 : exam05()
def odd(x):
    if x % 2 == 0:
        print('짝수')
    else:
        print('홀수')

# 문제6 : exam06()
def bonus(x):
    target = 1000
    bonus = 0.2
    won = "만원"

    if x > target:
        print('축하합니다. 실적을 달성하셨습니다.!')
        give = int(x * bonus)
        print('당신의 이번달 보너스는 ' + str(give) + won + '입니다.')

# 문제7 : exam07()
def missile(x, y, z):
    missile_moving = y + z
    print(x + ' 미사일이 ' + str(missile_moving) + '로 이동되었습니다.')

# 문제8 : exam08()
def change(x, y):
    vat = 0.1
    vat_p = int(y * vat)
    change = x - y

    print('받은 돈: ' + str(x))
    print('상품의 총액: ' + str(y))
    print('부가세: ' + str(vat_p))
    print('잔돈: ' + str(change))