from flask import Blueprint, request
from app.service.search_interface import *
import json

# 用参数name和import_name初始化名为search的蓝图
search = Blueprint('search', __name__)


# 搜索主页面
@search.route('/', methods=['GET'])
def search_index():
    if request.args.to_dict():
        u = request.args.to_dict()
        # 搜索方式判断
        # 普通搜索
        if u['method'] == '1':
            res = search_All(u)
        # 分类搜索
        elif u['method'] == '2':
            res = search_By_Product_Name(u)
        # -品牌分类搜索-
        elif u['method'] == '3':
            res = search_By_Product_Brand(u)
        # -品种分类搜索 -
        elif u['method'] == '4':
            res = search_By_Product_Varieties(u)
        # -标签分类搜索-
        elif u['method'] == '5':
            res = search_By_Product_Tags(u)
        # 心情
        elif u['method'] == '6':
            res = search_Dynamic(u)
        # 日记
        elif u['method'] == '7':
            res = search_Journal(u)
        # 测评
        elif u['method'] == '8':
            res = search_Test(u)
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
        if res:
            return json.dumps(res)
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


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

# 热搜关键字
@search.route('/search_index', methods=['POST'])
def search_fun():
    if request.is_json and request.get_json():
        u = request.get_json()
        # 实时热搜关键字排行
        if u['keyword'] and u['methods'] == 'search':
            res = hot_Keyword()
            return json.dumps(res)
        # 添加搜索关键字
        elif u['keyword'] and u['methods'] == 'add':
            res = record_Keyword(u)
            return json.dumps(res)
        else:
            return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})

# 单个产品
@search.route('/commodity', methods=['GET'])
def get_com():
    if request.args.to_dict():
        u = request.args.to_dict()
        res = search_Commodity(u)
        return json.dumps(res)
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})