import pymysql #alt+Enter

# DAO역할 모듈: CRUD(DML)

# 정형데이터 => mysql, oracle, sqlite3(관계형 데이터베이스 관리 시스템, RDBMS)

def create(id, pw, name, tel):

    # 데이터베이스 연결 순서
    # 1. mysql과 연결
    # connect를 통해 python <-> mysql 스트림(연결통로) 열음
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    # cursor: 스트림을 통해 주고받는 데이터를 컨트롤하는 부품
    cur = con.cursor()
    print(cur)

    # 3. sql문을 만들어서 전송함.
    sql = 'insert into member1 values ("' + id + '","' + pw + '","' + name + '","' + tel + '")'
    # 'sql문 "'+ 변수명 + '" sql문과 변수명 결합을 위한 +
    result = cur.execute(sql)
    print(result)

    # 4. auto-commit이 안된다. 수동으로 반영시켜야 한다.
    con.commit()
    con.close()  # 데이터베이스 사용 후 끝나면 끝내주는게 좋다!

def create2(data):
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into member1 values (%s, %s, %s, %s)'

    result = cur.execute(sql, data)
    print(result)

    con.commit()
    con.close()

def create3(datas):
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into member1 values (%s, %s, %s, %s)'

    result = cur.executemany(sql, datas)
    print(result)

    con.commit()
    con.close()

def read():
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = "select * from member1 where id = 'apple'"
    cur.execute(sql)

    # 하나만 가지올 때
    row = cur.fetchone()

    # cur.fetchall() : 조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(row)
    print(type(row))
    print(row[0])

    con.close()

def read2(id):
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = "select * from member1 where id = %s"
    cur.execute(sql, id)

    # 하나만 가지올 때
    row = cur.fetchone()

    print(row)
    print(type(row))
    print(row[0])

    con.close()

def read3():
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    cur = con.cursor(pymysql.cursors.DictCursor)
    print(cur)

    sql = "select * from member1"
    cur.execute(sql)

    # 조건에 맞는 목록을 모두 가지고 온다.
    rows = cur.fetchall()

    print(rows)
    print(type(rows))
    # print(rows[0])

    # for문을 돌려 세로로 정열해서 프린트
    for row in rows:
        print(row)

    con.close()

def update(id, tel):

    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = "update member1 set tel = %s where id = %s"
    # 파라메터 값, sql문 입력순서와 동일
    cur.execute(sql,(tel, id)) # tuple로 넣어주어야 한다.

    con.commit()
    con.close()

def delete(id):
    con = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='shop')
    print(con.get_host_info())

    curs = con.cursor()
    # rs.nextLine()과 동일, 한 줄 가져오는 것
    # 순차적으로 fetch해 처리하여 해당 결과 셋을 접근할 수 있게 도와줌

    print(curs)

    sql = 'delete from member1 where id= "' + id + '"'
    result = curs.execute(sql)
    print(result)

    con.commit()
    con.close() # 데이터베이스 사용 후 끝나면 끝내주는게 좋다!