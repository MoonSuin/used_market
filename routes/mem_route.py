from datetime import datetime

from flask import redirect, render_template, request, Blueprint
from services import MemService
from models import Member

service = MemService()

bp = Blueprint('member', __name__, url_prefix='/member')

@bp.route('/join')
def joinForm():
    return render_template('member/join.html')

@bp.route('/join', methods=['POST'])
def join():
    id = request.form['id']
    pwd = request.form['pwd']
    tel = request.form['tel']
    email = request.form['email']
    create_date = datetime.now()
    service.join(Member(id=id, pwd=pwd, tel=tel, email=email, create_date=create_date))
    return render_template('member/login.html')


@bp.route('/login')
def loginForm():
    return render_template('member/login.html')


@bp.route('/login', methods=['POST'])
def login():
    id = request.form['id']
    pwd = request.form['pwd']
    service.login(id, pwd)
    return render_template('index.html')


@bp.route('/myInfo')
def myInfo():
    m = service.getInfo()
    return render_template('member/detail.html', m=m)

@bp.route('/edit', methods=['POST'])
def edit():
    pwd = request.form['pwd']
    tel = request.form['tel']
    email = request.form['email']
    service.editInfo(Member(tel=tel, pwd=pwd, email=email))
    return redirect('/')

@bp.route('/logout')
def logout():
    service.logout()
    return redirect('/')

@bp.route('/out')
def out():
    service.out()
    return redirect('/')


























