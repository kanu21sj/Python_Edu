import pymysql

def create(datas):
    # 1. mysql 스트림 연결
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    # 호스트 정보 가져오기
    print(con.get_host_info())

    # 2. 스트임안의 데이터를 컨트롤 하는 부품 cursor 가져오기
    cur = con.cursor()
    print(cur)

    # 3. sql 만들어서 전송
    # sql = 'insert into movie(jumsu) values (%s)'
    # sql = 'insert into movie(title) values (%s)'
    # 일부 칼럼만 넣고 싶으면 데이터명(칼럼명, 칼럼명) 넣으면 됨
    sql = 'insert into movie(title, jumsu) values (%s, %s)'

    # 많은 데이터를 가져올 땐, executemany 함수 사용
    result = cur.executemany(sql, datas)
    print('처리결과', result, '개')

    # 4. auto-commit 안되므로 수동으로 반영(실행시킴)
    con.commit()
    # 데이터베이스 사용 후 연결 종료
    con.close()