# 기본 라이브러리(표준 라이브러리)
import math
import random

print(math.sqrt(9.0)) #sqrt = 루트
print(random.randint(1, 100)) #1~99사이의 랜덤한 숫자 생성

# 연산자
# 산술, 대입, 비교, 논리

# 산술연산자
x = 100
y = 333
print(x + y)
print(x - y)
print(x * y)
print(x % y) #나머지 추출
print(x / y)
print(x // y) #나누기 하였을 때 소수점 없이 정수부분만 추출 => //

# 대입연산자(=할당연산자)
# auto-typing: 파이썬에서는 변수의 생성과 타입이 값을 대입할 때 결정된다.

# 비교연산자 => 비교의 결과가 논리형
print(x == y)
print(x != y)

a = 10
a *= 10 # a = a * 10, *위치에 연산자 넣을 수 있음
print(a)

# 논리연산자: and(자바 = &&), or, not
id = 'root'
pw = '1234'
print(id == 'root' and pw == '1234')
print(id == 'root' or pw == '1222')

# 멤버쉽 연산자: in(~안애)
member = ['홍길동','김길동','송길동']
print('정길동' in member) #정길동이 포함되어 있니?
print('홍길동' not in member) #홍길동이 포함되어 있지 않니?