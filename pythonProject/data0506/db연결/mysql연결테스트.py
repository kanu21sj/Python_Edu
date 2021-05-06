import pymysql #alt+Enter

con = pymysql.connect(host='localhost', user='root', password='1234',
                      port=3306, db='shop')
print(con.get_host_info())

curs = con.cursor()
# rs.nextLine()과 동일, 한 줄 가져오는 것
# 순차적으로 fetch해 처리하여 해당 결과 셋을 접근할 수 있게 도와줌

print(curs)

sql = 'insert into member1 values ("python1", "python1", "python1", "python1")'
result = curs.execute(sql)
print(result)

con.commit()