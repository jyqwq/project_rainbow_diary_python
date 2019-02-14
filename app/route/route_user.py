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
@user.route('/person', methods=['POST'])
def person():
    if request.is_json and request.get_json():
        u = request.get_json()
        if u['methods'] == 'get':
            res = get_User_By_Id(u)
            return json.dumps(res)
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})

# 注册
@user.route('/register', methods=['POST'])
def register():
    if request.is_json and request.get_json():
        u = request.get_json()
        res = common_Register(u)
        return res
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})

# 登录
@user.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        if request.is_json and request.get_json():
            u = request.get_json()
            if u['token']:
                res = check_Token(u['token'])
                return json.dumps(res)
            else:
                res = get_User(u)
                return res
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
