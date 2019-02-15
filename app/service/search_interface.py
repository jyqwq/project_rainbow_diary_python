from app.dao.search_interface_module import *


# 根据产品搜索的封装方法
def search_By_Product_Name(k):
    if k and k['search'] and k['condition']:
        res = searchByProductName(k)
        if res:
            for i in res:
                i['commodity_date'] = str(i['commodity_date'])
            return res
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}

# 关键字搜索
def search_All(k):
    if k and k['search']:
        res = searchAll(k)
        if res:
            for i in res:
                i['commodity_date'] = str(i['commodity_date'])
            return res
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
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



if __name__ == '__main__':
    u = {'search':'大宝','condition':4}
    res = search_By_Product_Name(u)
    print(res)