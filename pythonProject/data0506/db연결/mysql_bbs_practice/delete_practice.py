import mysql_bbs_crud사용.bbs_dao_practice as db

id = input('삭제할 아이디를 입력하세요>> ')

db.delete(id)