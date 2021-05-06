import db연결.mysql연결모듈 as db

# vo역할, 여러개 데이터를 가져오기 위한 tuple 사용
# tuple 사용이유, 메모리 효율성 향상!(read only 이기 때문)
data1 = ("data3", "data3", "data3", "data3")
data2 = ("data4", "data4", "data4", "data4")
datas = (data1, data2) # tuple의 tuple을 만들어준다.
print('입력된 데이터들,', datas)
db.create3(datas)
