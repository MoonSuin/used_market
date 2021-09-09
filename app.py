from flask import Flask, request, render_template, redirect, session
from models import db, migrate  #모델 파일에 만든 객체 불러옴
import routes.mem_route as mr
import routes.board_route as br
import routes.msg_route as msgr

from datetime import datetime
import config

#플라스크 객체 생성
app = Flask(__name__)

#시크릿 키 생성
app.secret_key = 'asdf'

#플라스크 컨피그에 사용자정의 컨피그 추가
app.config.from_object(config)

#blueprint등록
app.register_blueprint(mr.bp)
app.register_blueprint(br.bp)
app.register_blueprint(msgr.bp)

# ORM을 위한 설정
db.init_app(app)
migrate.init_app(app, db)


@app.route('/')
def root():
    if 'flag' not in session.keys():
        session['flag'] = False
    return render_template('index.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('testing.html')


if __name__ == '__main__':
    app.run()#flask 서버 실행