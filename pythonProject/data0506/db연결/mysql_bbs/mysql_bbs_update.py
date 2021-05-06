import mysql_bbs_crud사용.bbs_dao as db

id = input('수정할 아이디를 입력하세요>>')
product = input('수정할 제품명을 입력하세요>>')

db.update(id, product)
