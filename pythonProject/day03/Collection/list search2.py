# 순차문의 구조: 입력--> 처리--> 출력
while True:
# 입력단계
# 파이썬에서는 들여쓰기로 포함관계를 나타낸다.
    code = input('본인의 사원번호를 입력하세요. (종료x) >> ')
    if code == 'x':
        print('시스템을 종료합니다.')
        break #break: 현재 반복문을 끝내

    # a110 : a는 부서를 나타냄, 1:직급(2번째 숫자직급), 10:내 번호
    # 부서가 a:기획부 b:개발부, c:인사부
    # 직급이 1:사장, 2:팀장, 3:사원

    # 처리단계
    # 1.입력한 데이터 중에서 부서와 직급을 추출한다.
    # 2.부서의 값에 따라서 부서를 판별
    # 3.직급의 값에 따라서 직급을 판별
    # 스크립트! (코딩전 스크립트 써보는거 중요)
    #a110, b230, c340
    dep = code[0] #부서
    deg = code[1] #직급
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