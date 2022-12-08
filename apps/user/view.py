from flask import Blueprint, request, render_template

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


@user_bp.route('/center')
def center():
    users = User.query.all()
    return render_template('user/center.html', users=users)


@user_bp.route('/login')
def login():
    return 'denglu'


@user_bp.route('/update')
def update():
    return 'gengxin '


@user_bp.route('/delete')
def delete():
    return 'gengxin '


@user_bp.route('/search')
def search():
    return 'search'