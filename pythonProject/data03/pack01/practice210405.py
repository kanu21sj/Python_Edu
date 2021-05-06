num1 = input('숫자를 입력하세요>> ')
num2 = input('숫자를 입력하세요>> ')

print(int(num1) + int(num2))
print(int(num1) - int(num2))
print(int(num1) * int(num2))
print(int(num1) / int(num2))

print('=======================')

name = input('이름을 입력하세요>> ')
age = input('나이를 입력하세요>> ')

print('출력은 ' + name + '은 ' + age + '세입니다.')

if int(age) > 100:
    print('나이가 많으시군요!')
else:
    print('아직 어리시군요')

print('=======================')

hobby = '달리기'
time = 10
print(hobby + '를 ' + str(time) + '시간 했습니다.')

if hobby == '달리기' and time >= 10:
    print('오늘 ' + hobby +'는 충분')
elif hobby == '달리기' or time <= 10:
    print('어떤 운동이든 시작하세요!!')