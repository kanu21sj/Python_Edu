# 1. 사고 싶은 것 5개를 입력 받아서, 리스트에 넣으세요! (for문 사용!) 전체 프린트
buy = []
for _ in range(5): #index 없이 5번 반복만 할 경우 변수 없어도 됨
    # data = input('사고 싶은 것은?? ')
    buy.append(input('사고 싶은 것은?? '))
print(buy)

# 2. wish에 들어갈 입력을 다음과 같이 하나의 스트링으로 입력 받아서 리스트에 넣어보세요.
# 입력: 프로그래머,분석가,기획가,마케팅전문가
# 나는 프로그래머가 되고 싶어요! 나는 분석가 되고 싶어요! 나는 기획가가 되고 싶어요! 나는 마케팅전문가가 되고 싶어요!
wish = list()
data = input()
data2 = data.split(',')
for x in data2:
    print('나는 ' + x + '가 되고 싶어요')
    continue
