from flask import Blueprint, request, render_template, redirect, url_for
from sqlalchemy.sql.elements import or_

from apps.user.models import User
from exts import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            user = User()
            user.password = password
            user.username = username
            user.phone = phone
            db.session.add(user)
            db.session.commit()
    return render_template('user/register.html')


@user_bp.route('/center', endpoint='user_center')
def center():
    users = User.query.filter(User.is_del == False).all()
    return render_template('user/center.html', users=users)


@user_bp.route('/login')
def login():
    return 'denglu'


@user_bp.route('/update')
def update():
    return 'gengxin '


@user_bp.route('/delete', endpoint='del')
def user_delete():
    # 逻辑删除
    id = request.args.get('id')
    user = User.query.get(id)
    user.is_del = True
    db.session.add(user)
    db.session.commit()

    # 物理删除
    # db.session.delete(user)
    # db.session.commit()
    # return redirect('/center')
    return redirect(url_for('user.user_center'))


@user_bp.route('/search')
def search():
    search = request.args.get('search')
    user_list = User.query.filter(or_(User.username.contains(search), User.phone.contains(search)))
    return render_template('user/center.html', users=user_list)
