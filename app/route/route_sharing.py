from flask import Blueprint, request
from app.service.sharing_interface import *
import json

# 用参数name和import_name初始化名为search的蓝图
sharing = Blueprint('sharing', __name__)


# 分享主页面
@sharing.route('/')
def sharing_index():
    pass

# 测评页面
@sharing.route('/evaluation',methods=['POST'])
def eva_index():
    if request.is_json and request.get_json():
        u = request.get_json()
        if u['evaluation']:
            res=evaluation_Index()
            return json.dumps(res)
        else:
            return json.dumps({"status_code":"40005","status_text":"数据格式不合法"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})

@sharing.route('/release',methods=['POST'])
def release_sharing():
    if request.is_json and request.get_json():
        u = request.get_json()
        if u['user_id']:
            # 心情写入
            if u['type'] == 'dy':
                res = graphic_Dy(u)
            # 日记写入
            elif u['type'] == 'dairy':
                res = graphic_Dairy(u)
            # 测评写入
            elif u['type'] == 'test':
                res = graphic_Test(u)
            else:
                return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
        return json.dumps(res)
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
