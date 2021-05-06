member = ['a110','b230','c340']

print('리스트의 개수 >> ', len(member))

# 1.리스트에서 요소를 하나씩 꺼내주어야 함
# 2.꺼낸 요소 중 부서와 직급을 다시 추출해야함.

for code in member: ##for index in range(len(member)) 동일
    dep = code[0]
    deg = code[1]
    result = '' #찍어줄 스트링!을 모아줄 변수!

    if dep == 'a':
        result = '기획부'
    elif dep == 'b':
        result = '개발부'
    elif dep == 'c':
        result = '인사부'
    else:
        print('\n해당 부서가 존재하지 않음.')

    if deg == '1':
        result = result + " " + "사장"
    elif deg == '2':
        result = result + " " + "팀장"
    elif deg == '3':
        result = result + " " + "사원"
    else:
        print('\n해당 직급이 존재하지 않음.')

    print('당신은', result)