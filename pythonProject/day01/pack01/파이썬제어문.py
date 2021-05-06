food = input('먹고 싶은 음식은?: ')
print('당신이 입력한 먹고 싶은 음식은', food)

if food == '우동':
  print('우산을 들고간다')
  print('돈 들고 간다.')
  print('우동집으로 간다.')
elif food == '자장면':
  print('중국집으로 간다.')
elif food == '라면': #if 뒤에는 반드시 조건을 쓴다.
  print('분식집으로 간다.')
else: #else 뒤에는 조건을 쓰지 않는다.
  print('위의 것이 아니면 집에서 드세요.') #pass

start = 0 #시작값 / 숫자를 입력하면 그 자체가 int로 인식, 그러나 '100'으로 입력일 경우 str 으로 인식
while start < 10: #True, 조건식
  print(start, '> 내가 반복')
  start = start + 1 #증감식

for x in range(10): #0~9까지 범위, 기본값이 1씩 증가!
  print(x, '나도 반복')

time = int(input('지금 시각은? >> '))
print('현재 시각은', time)

if time <= 11:
  print('굿모닝')
elif time <= 15: #True
  print('굿에프터눈') #break, cpu처리 여기서 끝!
elif time <= 20:
  print('굿이브닝')
else:
  print('굿나잇')

month = int(input('이번달은? >> '))
print('이번달은', month)

if 3<= month <=5:
  print('봄')
elif 6<= month <=8:
  print('여름')
elif 9<= month <=11:
  print('가을')
else:
  print('겨울')