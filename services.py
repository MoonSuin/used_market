from flask import request, session
from flask_sqlalchemy import SQLAlchemy

from models import Member, Prod_cate, Prod_like, Board, Msg, db

class MemService:
    def join(self, m):
        db.session.add(m)
        db.session.commit()

    def login(self, id, pwd):
        mem = Member.query.get(id)
        if mem is not None:
            if mem.pwd == pwd:
                session['login_id'] = id
                session['flag'] = True
                return True
        return False

    def logout(self):
        session.pop('login_id') #key자체를 삭제
        session['flag'] = False

    def out(self):
        id =session['login_id']
        m = Member.query.get(id)
        db.session.delete(m)
        db.session.commit()
        self.logout()

    def getInfo(self): # 현재 로그인한 id로 검색한 결과 반화 (Member객체)
        return Member.query.get(session['login_id'])

    def editInfo(self, m):
        mm = self.getInfo()
        mm.pwd = m.pwd
        mm.tel = m.tel
        mm.email = m.email
        db.session.commit()

class BoardService:
    def cateList(self):
        return Prod_cate.query.order_by(Prod_cate.num.asc())

    def getCate(self, cnum):
        return Prod_cate.query.get(cnum)

    def addBoard(self, b):  # b: writer, w_date, loc, p_cate_num, price, title, content, img
        db.session.add(b)
        db.session.commit()
        return b

    def editImgs(self, b):
        bb = self.getByNum(b.num)
        bb.img1 = b.img1
        bb.img2 = b.img2
        bb.img3 = b.img3
        db.session.commit()

    def getByNum(self, num):

        return Board.query.get(num)

    def getByTitle(self, title):
        return Board.query.filter(Board.title.like('%'+title+'%')).all()

    def getByCate(self, cate_num):
        return Board.query.filter(Board.p_cate_num==cate_num).all()

    def getByLoc(self, loc):
        return Board.query.filter(Board.loc(loc)).all()

    def getAll(self):
        return Board.query.order_by(Board.num.desc())

    def getByWriter(self, writer):
        return Board.query.filter(Board.writer==writer).order_by(Board.num.asc())

    def editBoard(self, b): #제목,가격,내용,사진
        bb = Board.query.get(b.num)
        bb.title = b.title
        bb.price = b.price
        bb.content = b.content
        db.session.commit()

    def delBoard(self, num):
        b = Board.query.get(num)
        db.session.delete(b)
        db.session.commit()

    def editCnt(self, num):
        b = self.getByNum(num)
        b.cnt += 1
        db.session.commit()

    def editLike(self, num):
        b = self.getByNum(num)
        b.like += 1
        db.session.commit()

    def editState(self, num):
        b = self.getByNum(num)
        if b.state:
            b.state = False
        else:
            b.state = True

    def myLikeAdd(self, b_num):
        id = session['login_id']
        db.session.add(Prod_like(id=id, b_num=b_num))
        db.session.commit()

    def myLikeList(self):
        id = session['login_id']
        return Prod_like.query.filter(Prod_like.id == id).order_by(Prod_like.num.desc())














