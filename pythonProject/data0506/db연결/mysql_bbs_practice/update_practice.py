import mysql_bbs_crud사용.bbs_dao_practice as db

id = input('수정할 아이디를 입력하세요>>')
ceo = input('수정할 ceo명을 입력하세요>>')

db.update(id, ceo)