import pymysql

# CRUD 구현
# 정형데이터 => mysql, oracle, sqlite3(관계형 데이터베이스 관리 시스템, RDBMS)
def create(datas):
    # 1. mysql 연결
    # 스트림 열기
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    # 2. cursor 획득(스트림안 데이터 다루는 역할)
    cur = con.cursor()
    print('커서획득', cur)

    # 3. sql문 만들어 전송
    sql = 'insert into bbs1 values (%s, %s, %s, %s)'

    # 여러개 데이터 전송할 때는 excutemany 함수 사용 및 sql문과 데이터 파라메터(datas)보내야 함
    result = cur.executemany(sql, datas)
    print('데이터 보내기 성공', result)

    # db 데이터 처리를 위한 commit
    con.commit()
    # 데이터베이스 사용 후 항상 종료!
    con.close()

def read():
    # 1. mysql 연결
    # 스트림 열기
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    # 2. cursor 획득(스트림안 데이터 다루는 역할)
    cur = con.cursor()
    print('커서획득', cur)

    sql = "select * from bbs1"
    # 읽어와야 하는 값이 id 이므로 파라메터 값으로 id 입력
    cur.execute(sql)

    # 모든 데이터 가져올때
    rows = cur.fetchall()

    print('가져온 데이터는', rows)
    print('데이터 타입은 ', type(rows))
    # print(row[0])

    # for문을 돌려 세로로 정열해서 프린트
    for row in rows:
        print('정렬해서 가져온 데이터는 ', row)

    # read 함수는 데이터처리 할게 없이 읽어오기만 하면 되므로 close만 사용
    con.close()

def update(id, ceo):
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    cur = con.cursor()
    print('커서획득', cur)

    sql = "update bbs1 set ceo = %s where id = %s"
    # 파라메터 값, sql문 입력순서와 동일
    cur.execute(sql,(ceo, id)) # tuple로 넣어주어야 한다.

    con.commit()
    con.close()

def delete(id):
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    cur = con.cursor()
    print('커서획득', cur)

    sql = "delete from bbs1 where id = %s"
    # 파라메터 값, sql문 입력순서와 동일
    cur.execute(sql, id) # tuple로 넣어주어야 한다.

    # 데이터 찾아서 삭제 해야 하므로 처리 필요
    con.commit()
    # 데이터사용 후 종료
    con.close()