from datetime import datetime

from flask import request, render_template, redirect, session, Blueprint
from models import Msg
from services import MsgService

bp = Blueprint('msg', __name__, url_prefix='/msg')

service = MsgService()

@bp.route('/list/<int:b_num>')
def list(b_num):
    mlist = service.getByBNum(b_num)
    return  render_template('msg/list.html', mlist=mlist)

@bp.route('/add', methods=['POST'])
def add():
    b_num = request.form['b_num']
    like_id = request.form['like_id']
    tel = request.form['tel']
    content = request.form['content']
    service.addMsg(Msg(b_num=b_num, like_id=like_id, tel=tel, content=content))
    return redirect('/board/list')

@bp.route('/get/<int:num>')
def get(num):
    msg = service.getByNum(num)
    return render_template('msg/detail.html', msg=msg)




