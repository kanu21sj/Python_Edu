hobby = []
hobby.append('코딩')
print('개수>> ', len(hobby))
hobby.append('등산')
print('개수>> ', len(hobby))
# hobby가 불분명할 경우, hobby.append 사용하여 하나씩 기입

for _ in range(3):
    data = input('당신의 새로운 취미는 >> ')
    hobby.append(data)
# 새로운 데이터의 개수를 for 문에 (00) 설정, 데이터를 input 한 후, append(data)값을 출력

print('개수>> ', len(hobby))
# hobby.append + input된 데이터의 개수가 몇개인지 알려주는것

for x in hobby:
    print(x)
#hobby 저장된 데이터 요소변수 x전체를 불러오는 것