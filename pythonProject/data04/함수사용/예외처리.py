try:
    me_file = open("me.txt", "r", encoding='utf-8') # r: 읽는용
    print(me_file.readline())
    lines = me_file.readlines()
    print('읽어온 내용', lines)
    print(type(lines))
    me_file.close()
except IOError: # 파일을 읽고 쓸 때 생기는 에러
    print('파일을 읽는 중 에러발생!!!')
finally:
    print('나는 예외처리를 꼭 해줌..')
print('내가 실행이 되는가...')