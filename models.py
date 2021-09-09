from flask import session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate() #Migrate 객체 생성

#멤버(회원관리)
class Member(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    pwd = db.Column(db.String(20), nullable=False)
    tel = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

#게시판 데이블
class Board(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    writer = db.Column(db.String(20), db.ForeignKey('member.id', ondelete='CASCADE'))
    w_date = db.Column(db.DateTime(), nullable=False)
    loc = db.Column(db.String(50), nullable=False)
    p_cate_num =db.Column(db.Integer, db.ForeignKey('prod_cate.num', ondelete='SET NULL'))
    price = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    img1 = db.Column(db.String(100))
    img2 = db.Column(db.String(100))
    img3 = db.Column(db.String(100))
    cnt = db.Column(db.Integer, nullable=False, default=0)
    like = db.Column(db.Integer, nullable=False, default=0)
    state = db.Column(db.Boolean, default=False)

#상품카테고리
class Prod_cate(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

#찜한 상품
class Prod_like(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(20), db.ForeignKey('member.id', ondelete='CASCADE'))
    b_num = db.Column(db.Integer, db.ForeignKey('board.num', ondelete='CASCADE'))

#메세지
class Msg(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    b_num = db.Column(db.Integer, db.ForeignKey('board.num', ondelete='CASCADE'))
    board = db.relationship('Board', backref=db.backref('msg_set'))
    like_id = db.Column(db.String(20), db.ForeignKey('member.id', ondelete='CASCADE'))
    tel = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(100))
    checked = db.Column(db.Boolean, default=False)

