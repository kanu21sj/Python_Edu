# 문자열 포맷팅

#s에 이름, d에 나이 들어감
p = '이름: %s, 나이: %d' % ('홍길동', 100)
print(p)

# X = 소수점 세자리 반올림, Y = 소수점 두자리 반올림
p2 = 'X = %0.3f, Y= = %10.2f' % (3.1456, 555.666)
print(p2)

s = "이름: {0}, 나이: {1}"
sf = s.format("최선종", 300)
print(sf)

s2 = "이름: {name}, 나이: {age}"
sf2 = s2.format(name = "최선종", age = 300)
print(sf2)

data = (10, 20, 30)
s3 = "길이: {d[0]}, 높이: {d[1]}, 면적: {d[2]},"
sf3 = s3.format(d = data)

# 문자열 추출: indexing(인덱싱) => slicing(슬라이싱)
name = '홍길동'
print(name[0])
print(name[1])
print(name[2])
print(name[0:2]) #0~1까지 가져옴
print(name[0:]) #0부터 끝까지 가져옴
print(name[1:]) #1부터 끝까지 가져옴
print(name[:2]) #시작부터 1까지 가져옴
print(type(name))
print(type(name[0]))

hobby = '달리기,등산,자전거,코딩'
result = hobby.split(',')
print(result)
print(type(result))
print(result[0])
print(result[3])
