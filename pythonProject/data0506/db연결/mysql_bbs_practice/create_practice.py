import mysql_bbs_crud사용.bbs_dao_practice as db

# vo역할, 여러개 데이터 가져오려면 tuple 사용
# tuple, read only이고 데이터 효율성이 높아 사용

data1 = ("b1", "banana", "yellow", "nana")
data2 = ("c1", "spring_onion", "green", "ddubi")
datas = (data1, data2) # tuple안의 tuple 만들어준다.
print('입력된 데이터는 ', datas)
db.create(datas)
