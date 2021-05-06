food = ['아이스크림', '아이스아메리카노', '생수'] #list(목록)
# hobby = []
print(food[0])
print(food[1])
print(food[2])
#0부터 시작한 데이터 값을 프린트 0,1,2 숫자로 변환하여 출력

for i in range(0, len(food)): #목록의 개수를 세어주는 함수
    print(food[i], end=' ')
print()
# 0부터 시작하여 len으로 데이터의 개수를 확인, 데이터 숫자만큼
# 요소변수 i에 대입하고 반복하여 데이터 개수를 파악, end는 옆으로 나열하여 쓰는 것

for x in food: #for-each
    print(x, end=' ')
# food에 저장된 요수변수 x를 한번에 불러오는 것

###################
# 오늘 끝나고 나서, 할 일 5가지를 목록으로 만들어보세요.
# 2가지 방식으로 프린트
print()

today = ['저녁식사', '헬스장', '샤워', '복습', '잠자기']
for a in range(0, len(today)):
    print(today[a], end=' ')
print()
for b in today:
    print(b, end=' ')