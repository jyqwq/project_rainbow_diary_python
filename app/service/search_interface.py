from app.dao.search_interface_module import *


# 根据产品搜索的封装方法
def search_By_Product_Name(k):
    if k and k['keyword'] and k['condition']:
        res = searchByProductName(k)
        if res:
            for i in res:
                i['commodity_date'] = str(i['commodity_date'])
            return res
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}

# 根据品牌搜索
def search_By_Product_Brand(k):
    if k['keyword'] and k['etp'] and k['condition']:
        res = searchByProductBrands(k)
    elif k['keyword'] and k['etp']:
        res = searchByProductBrand(k)
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}
    if res:
        for i in res:
            i['commodity_date'] = str(i['commodity_date'])
        return res
    else:
        return {"status_code": "40004", "status_text": "系统错误"}

# 品种
def search_By_Product_Varieties(k):
    if k and k['keyword'] and k['condition']:
        res = searchByProductVarieties(k)
        if res:
            for i in res:
                i['commodity_date'] = str(i['commodity_date'])
            return res
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}

# 标签
def search_By_Product_Tags(k):
    if k['keyword'] and k['etp'] and k['condition']:
        res = searchByProductTags(k)
    elif k['keyword'] and k['condition']:
        res = searchByProductTag(k)
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}
    if res:
        for i in res:
            i['commodity_date'] = str(i['commodity_date'])
        return res
    else:
        return {"status_code": "40004", "status_text": "系统错误"}

# 综合搜索
def search_All(k):
    if k and k['keyword']:
        res = searchAll(k)
        if res:
            for i in res:
                i['commodity_date'] = str(i['commodity_date'])
            return res
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}

# 查找心情
def search_Dynamic(k):
    if k and k['keyword']:
        res = searchDynamic(k)
        if res == -1:
            return {"status_code": "40004", "status_text": "系统错误"}
        else:
            return res
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}

# 查找日记
def search_Journal(k):
    if k and k['keyword']:
        res = searchJournal(k)
        if res == -1:
            return {"status_code": "40004", "status_text": "系统错误"}
        else:
            return res
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}

 # 查找测评
def search_Test(k):
    if k and k['keyword']:
        res = searchTest(k)
        if res == -1:
            return {"status_code": "40004", "status_text": "系统错误"}
        else:
            return res
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}

# 实时热搜排行
def hot_Search():
    res = hotSearch()
    if res:
        for i in res:
            if i['user_id']:
                u = get_User_Name(i['user_id'])
                if u and u[0]['user_nickname']:
                    i['user_name'] = u[0]['user_nickname']
                else:
                    return {"status_code": "40004", "status_text": "系统错误"}
            else:
                return {"status_code": "40005", "status_text": "数据格式不合法"}
        return res
    else:
        return {"status_code": "40004", "status_text": "系统错误"}


# 热门日记排行
def hot_Dairy():
    res = hotDairy()
    if res:
        for i in res:
            if i['user_id']:
                u = get_User_Name(i['user_id'])
                if u and u[0]['user_nickname']:
                    i['user_name'] = u[0]['user_nickname']
                else:
                    return {"status_code": "40004", "status_text": "系统错误"}
            else:
                return {"status_code": "40005", "status_text": "数据格式不合法"}
        return res
    else:
        return {"status_code": "40004", "status_text": "系统错误"}


# 热门妆品排行
def hot_Cosmetics():
    res = hotCosmetics()
    if res:
        return res
    else:
        return {"status_code": "40004", "status_text": "系统错误"}

# 根据userid找到username
def get_User_Name(id):
    if id and type(id)==type(1):
        res = getUserName(id)
        if res:
            return res
        else:
            return -1
    else:
        return None

# 热搜关键字
def hot_Keyword():
    res=hotKeyword()
    if res:
        return res
    else:
        return {"status_code": "40004", "status_text": "系统错误"}

# 记录搜索关键字
def record_Keyword(k):
    res=recordKeyword(k)
    if res:
        return {"status_code":"10013","status_text":"记录成功"}
    else:
        return {"status_code": "40004", "status_text": "系统错误"}


# 单个产品
def search_Commodity(u):
    if u['id']:
        res = searchCommodity(u['id'])
        if res:
            com = commodityComment(u['id'])
            if com == -1:
                return {"status_code": "40004", "status_text": "系统错误"}
            else:
                res['comment'] = com
            return res
        else:
            return {"status_code": "40004", "status_text": "系统错误"}

if __name__ == '__main__':
    # -普通搜索 -
    a = {'keyword': '大宝', 'method': 1}

    # 带按钮的
    b = {'keyword': '大宝', 'method': 2,'condition':'护手霜'}

    # -品牌分类搜索 -
    c = {'keyword': '大宝', 'condition': '', 'etp': 's', 'method': 3}

    # -品种分类搜索 -
    g = {'keyword': '大宝', 'condition': 's%a', 'method': 4}

    # -标签分类搜索 -
    j = {'keyword': '大宝', 'condition': 's', 'etp': '', 'method': 5}
    res = searchCommodity(3)
    print(res)