from app.app import app
from app.route.route_sharing import sharing
from app.route.route_search import search
from app.route.route_user import user
from flask import Blueprint,request
from app.service.index_interface import *
import json

# 构建蓝图
app.register_blueprint(sharing, url_prefix='/sharing')
app.register_blueprint(search, url_prefix='/search')
app.register_blueprint(user, url_prefix='/user')

#网站主页路由
@app.route('/index',methods=['POST'])
def index():
    if request.is_json and request.get_json():
        u = request.get_json()
        # 量身推荐接口
        if u['skinid']:
            res=recommended_Volume(u)
            return json.dumps(res)
        # 热门动态
        elif u['hot_thing']:
            res=hot_Dynamic()
            return json.dumps(res)
        # 测评资讯
        elif u['evaluation_information']:
            res=evaluation_Information()
            return json.dumps(res)
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


#404错误路由
@app.errorhandler(404)
def miss(e):
    return '该页面不存在', 404


#500错误路由
@app.errorhandler(500)
def error(e):
    return '服务器正在维护...', 500
