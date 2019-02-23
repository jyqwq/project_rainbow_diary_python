from flask import Blueprint, request
from app.service.user_interface import *
import json

# 用参数name和import_name初始化名为user的蓝图
user = Blueprint('user', __name__)


# 用户主页面
@user.route('/')
def search_index():
    return 'welcome to page user!'


# 个人操作管理
@user.route('/person', methods=['POST', 'GET'])
def person():
    # post请求
    if request.method == 'POST':
        if request.is_json and request.get_json():
            u = request.get_json()
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
        # 个人主页
        if u['methods'] == 'get':
            res = get_User_By_Id(u)
            return json.dumps(res)
        # 我的动态
        elif u['methods'] == 'mydy':
            res = mine_Dy(u)
            return json.dumps(res)
        # 所有动态
        elif u['methods'] == 'dy':
            res = my_Dynamics(u)
            return json.dumps(res)
        # 我的收藏
        elif u['methods'] == 'mycol':
            res = mine_Collections(u)
            return  json.dumps(res)
        # 更新个人信息
        elif u['methods'] == 'update':
            res = update_User_Message(u)
            return json.dumps(res)
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
    # get请求
    elif request.method == 'GET':
        if request.args.to_dict():
            u = request.args.to_dict()
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
        # 评论相关
        if request.args.get('comment'):
            if request.args.get('method'):
                # 查看评论
                if u['method'] == 'check':
                    res = view_Comment(u)
                    return json.dumps(res)
                # 添加评论
                elif u['method'] == 'add':
                    res = increase_Comment(u)
                    return json.dumps(res)
                else:
                    return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
            else:
                return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
        # 单个动态
        elif request.args.get('type') and request.args.get('id'):
            res = get_Dy_By_Id(u)
            return json.dumps(res)
        # 个人操作相关
        elif request.args.get('user_id') and request.args.get('other_id'):
            if request.args.get('type'):
                if request.args.get('judge'):
                    # 点赞相关
                    if u['judge'] == 'compliment':
                        # 查看是否点赞
                        if u['method'] == 'check':
                            res = view_Compliment(u)
                            return json.dumps(res)
                        # 添加点赞
                        elif u['method'] == 'add':
                            res = increase_Compliment(u)
                            return json.dumps(res)
                        # 删除点赞
                        elif u['method'] == 'delete':
                            res = delete_Compliment(u)
                            return json.dumps(res)
                        else:
                            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
                    # 收藏相关
                    elif u['judge'] == 'collections':
                        # 查看是否收藏
                        if u['method'] == 'check':
                            res = view_Collections(u)
                            return json.dumps(res)
                        # 添加收藏
                        elif u['method'] == 'add':
                            res = increase_Collection(u)
                            return json.dumps(res)
                        # 删除收藏
                        elif u['method'] == 'delete':
                            res = delete_Collection(u)
                            return json.dumps(res)
                        else:
                            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
                else:
                    return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
            else:
                # 查看是否关注
                if u['method'] == 'check':
                    res = view_Concern(u)
                    return json.dumps(res)
                # 添加关注
                elif u['method'] == 'add':
                    res = increase_Concerns(u)
                    return json.dumps(res)
                # 删除关注
                elif u['method'] == 'delete':
                    res = delete_Concerns(u)
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
