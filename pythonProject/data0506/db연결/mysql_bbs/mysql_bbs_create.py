import mysql_bbs_crud사용.bbs_dao as db

#vo역할, 여러개 데이터를 가져오기 위한 tuple 사용
# tuple 사용이유, 메모리 효율성 향상!(read only 이기 때문)
data1 = ("professor", "apple", "mac", "olleh")
data2 = ("baseball", "bat", "ssg", "choo")
datas = (data1, data2) # tuple의 tuple을 만들어준다.
print('입력된 데이터는 ', datas)
db.create(datas)
