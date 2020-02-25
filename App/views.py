# 建立路由规则,定义视图函数
from flask import render_template, Blueprint

blue = Blueprint('_blue', __name__)


@blue.route('/')
def index():
    return 'hello flask'

@blue.route('/test/')
def test():
    return render_template('admin.html')