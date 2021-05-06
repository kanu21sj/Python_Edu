# 기본형 4가지
# 정수, 실수
age = 100 #정수(int)
weight = 99.9 #실수(float)

sum2 = age + weight #더하기 연산자
print(sum2)

# sum은 기본적으로 list에 있는 값들을 더해줌(오류발생)
# sum보다 sum2처럼 변수를 다르게 설정하는것이 좋음
# result = sum(age2)
# print(result)

temp = input('현재 온도는>> ') #'22.2' 입력받은 값은 모두 str
print(type(temp)) #type(): 입력된 값의 type을 확인해주는 함수

temp2 = float(temp)
print(type(temp2))

if temp2 > 20:
    print('너무 더워요..')
else:
    print('아직 안더워요')

# 타입을 변경하는 것: 형변환(casting, 캐스팅)
# 문자로 변경하는 것: str()
# 정수로 변경하는 것: int()
# 실수로 변경하는 것: float()

# 문자
# string을 의미, char를 포함하는 의미!
company = '메가'
print(company, end=' ') #프린트 후, 마지막에 엔터 적용
print('우리 회사는', company)

# 논리
food = True #False
food2 = 1 #True = 1, False = 0

# food 기본적으로 True 설정되어있으므로 if food == True: 할 필요 없음
if food == food2: # == 비교 연산자
    print('배가 부르시겠군요!')
else:
    print('배가 고파요')