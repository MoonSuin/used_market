from datetime import datetime

from flask import request, render_template, redirect, session, Blueprint
from models import Board
from services import BoardService
import os

bp = Blueprint('board', __name__, url_prefix='/board')

service = BoardService()
locations = {1:'서울', 2:'경기', 3:'부산', 4:'대전', 5:'강원'}
@bp.route('/add')
def addForm():
    cate = service.cateList()
    return render_template('board/form.html', cate=cate, loc=locations)

@bp.route('/add', methods=['POST'])
def add():
    writer = request.form['writer']
    w_date = datetime.now()
    loc = locations[int(request.form['loc'])]
    p_cate_num = request.form['p_cate_num']
    price = request.form['price']
    title = request.form['title']
    content = request.form['content']
    b = service.addBoard(Board(writer=writer, w_date=w_date, loc=loc, p_cate_num=p_cate_num, price=price, title=title, content=content))
    num = b.num
    #디렉토리 생성후 이미지 업로드
    dir = 'static/img/prod_'+str(num)+'/'
    os.mkdir(dir)
    f=[]
    f.append(request.files['img1'])
    f.append(request.files['img2'])
    f.append(request.files['img3'])
    names=[]
    print(f)
    for i in range(0,len(f)):
        if f[i].filename == '':
            print('업로드안됨')
            names.append(None)
        else:
            arr = f[i].filename.split('.')
            file_type = arr[len(arr)-1]
            fname = dir +'p_'+str(i+1)+'.'+file_type
            f[i].save(fname)
            names.append('/'+fname) #db에 저장할 이름

    service.editImgs(Board(num=num, img1=names[0], img2=names[1], img3=names[2]))

    return redirect('/board/list')

@bp.route('/list')
def list():
    blist = service.getAll()
    return render_template('board/list.html', blist=blist)

@bp.route('/detail/<int:num>')
def detail(num):
    service.editCnt(num)
    b = service.getByNum(num)
    cate = service.getCate(b.p_cate_num)
    return render_template('board/detail.html', b=b, cate=cate)

@bp.route('/like/<int:bnum>')
def addLike(bnum):
    service.editLike(bnum)
    service.myLikeAdd(bnum)
    return redirect('/board/detail/'+str(bnum))

@bp.route('/like-list')
def likeList():
    llist = service.myLikeList()
    return render_template('board/likeList.html', llist=llist)

@bp.route('/edit')
def editBoard():
    title = request.form['title']
    price = request.form['price']
    content = request.form['content']
    service.editBoard()

@bp.route('/del/<int:num>')
def delBoard(num):
    service.delBoard(num)
    return redirect('/board/list')

@bp.route('')
def searchTitle():
    pass

@bp.route('')
def searchLoc():
    pass

@bp.route('')
def searchCate():
    pass

