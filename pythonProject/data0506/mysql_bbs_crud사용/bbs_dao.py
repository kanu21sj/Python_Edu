import pymysql

# create 함수 정의
def create(datas):
    # 1. mysql 스트림 연결
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    # 호스트 정보 가져오기
    print(con.get_host_info())

    # 2. 스트임안의 데이터를 컨트롤 하는 부품 cursor 가져오기
    cur = con.cursor()
    print(cur)

    # 3. sql 만들어서 전송
    sql = 'insert into bbs1 values (%s, %s, %s, %s)'

    # 많은 데이터를 가져올 땐, executemany 함수 사용
    result = cur.executemany(sql, datas)
    print(result)

    # 4. auto-commit 안되므로 수동으로 반영(실행시킴)
    con.commit()
    # 데이터베이스 사용 후 연결 종료
    con.close()

def read():
    # 1. mysql 스트림 연결
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    # 호스트 정보 가져오기
    print(con.get_host_info())

    # 2. 스트임안의 데이터를 컨트롤 하는 부품 cursor 가져오기
    cur = con.cursor(pymysql.cursors.DictCursor) # 항목명 : 값으로 프린트
    print(cur)

    # 3. sql 만들어서 전송
    sql = "select * from bbs1"
    cur.execute(sql)

    # 조건에 맞는 목록을 모두 가지고 온다.
    rows = cur.fetchall()

    # for
    for row in rows:
        print(row)

    # 4. 데이터베이스 연결 종료
    # DB에서 처리 없이 데이터만 불러오기 때문에 commit사용 없음
    con.close()

def update(id, product):

    # 1. mysql 스트림 연결
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    # 호스트 정보 가져오기
    print(con.get_host_info())

    # 2. 스트임안의 데이터를 컨트롤 하는 부품 cursor 가져오기
    cur = con.cursor()
    print(cur)

    # 3. sql 만들어서 전송
    sql = "update bbs1 set product = %s where id = %s"
    # 파라메터 값, sql문 입력순서와 동일
    cur.execute(sql,(product, id)) # tuple로 넣어주어야 한다.

    # 4. auto-commit 안되므로 수동으로 반영(실행시킴)
    con.commit()
    con.close()

def delete(id):
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = "delete from bbs1 where id= %s"
    result = cur.execute(sql, id)
    print(result)

    con.commit()
    con.close()