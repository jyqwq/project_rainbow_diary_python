from flask import Blueprint, request
from app.service.user_interface import *
import json


# 用参数name和import_name初始化名为search的蓝图
user = Blueprint('user', __name__)


# 用户主页面
@user.route('/')
def search_index():
    return 'welcome to page user!'


# 个人操作管理
@user.route('/person', methods=['POST', 'GET', 'PUT', 'DELETE'])
def person():
    # 获取用户信息
    if request.method == 'GET':
        return '获取用户信息'
    # 注册
    elif request.method == 'POST':
        if request.is_json and request.get_json():
            u = request.get_json()
            res = common_Register(u)
            return json.dumps(res)
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
    elif request.method == 'PUT':
        return '修改用户'
    elif request.method == 'DELETE':
        return '删除用户'


# 登录
@user.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            u = request.get_json()
            if u['token']:
                res = check_Token(u['token'])
            else:
                res = get_User(u)
            return json.dumps(res)
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
