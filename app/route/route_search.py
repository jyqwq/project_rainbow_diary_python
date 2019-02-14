from flask import Blueprint, request
from app.service.search_interface import *
import json

# 用参数name和import_name初始化名为search的蓝图
search = Blueprint('search', __name__)


# 搜索主页面
@search.route('/')
def search_index():
    pass


# 热门搜索排行
@search.route('/rank', methods=['POST'])
def search_rank():
    if request.is_json and request.get_json():
        u = request.get_json()
        # 实时热搜排行
        if u['hot_search']:
            res = hot_Search()
            return json.dumps(res)
        # 热门日记排行
        elif u['hot_dairy']:
            res = hot_Dairy()
            return json.dumps(res)
        # 热门妆品排行
        elif u['hot_cosmetics']:
            res = hot_Cosmetics()
            return json.dumps(res)
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})

# 热门搜索排行
@search.route('/search_index', methods=['POST'])
def search_fun():
    if request.is_json and request.get_json():
        u = request.get_json()
        # 实时热搜排行
        if u['keyword']:
            res = hot_Keyword()
            return json.dumps(res)

        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})