from app.dao.search_interface_module import *


# 根据产品名搜索的封装方法
def search_By_Product_Name(name):
    pass


# 根据成分产品名搜索的封装方法
def search_By_Component(component):
    pass


# 根据功能搜索的封装方法
def search_By_Function(func):
    pass


# 根据肤质搜索的封装方法
def search_By_Skin(skin):
    pass


# 根据动态标签搜索的封装方法
def search_By_Dynamic(dynamic):
    pass


# 实时热搜排行
def hot_Search():
    res = hotSearch()
    if res:
        return res
    else:
        return {"status_code": "40004", "status_text": "系统错误"}


# 热门日记排行
def hot_Dairy():
    res = hotDairy()
    if res:
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