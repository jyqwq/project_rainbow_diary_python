from . import POOL
import pymysql
from app.dao.sql.search_sql import *


# 根据产品搜索的源码
def searchByProductName(k):
    try:
        client = POOL.connection()
        res = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchByProductName'].format(keyword=k['keyword'],category_id=k['condition'])
        cursor.execute(sql)
        res = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return res

# 品牌+功能
def searchByProductBrands(k):
    try:
        client = POOL.connection()
        res = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchByProductBrands'].format(etp=k['etp'],keyword=k['keyword'],condition=k['condition'])
        cursor.execute(sql)
        res = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return res

# 品牌
def searchByProductBrand(k):
    try:
        client = POOL.connection()
        res = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchByProductBrand'].format(etp=k['etp'],keyword=k['keyword'])
        cursor.execute(sql)
        res = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return res

# 品种
def searchByProductVarieties(k):
    try:
        client = POOL.connection()
        res = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchByProductVarieties'].format(condition=k['condition'],keyword=k['keyword'])
        cursor.execute(sql)
        res = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return res

# 标签
def searchByProductTags(k):
    try:
        client = POOL.connection()
        res = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchByProductTags'].format(etp=k['etp'],keyword=k['keyword'],condition=k['condition'])
        cursor.execute(sql)
        res = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return res

def searchByProductTag(k):
    try:
        client = POOL.connection()
        res = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchByProductTag'].format(keyword=k['keyword'], condition=k['condition'])
        cursor.execute(sql)
        res = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return res

# 搜索综合
def searchAll(k):
    try:
        client = POOL.connection()
        res = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchAll'].format(keyword=k['keyword'])
        cursor.execute(sql)
        res = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return res

# 查找心情
def searchDynamic(k):
    try:
        client = POOL.connection()
        res = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchDynamic'].format(keyword=k['keyword'])
        cursor.execute(sql)
        res = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return res

# 查找日记
def searchJournal(k):
    try:
        client = POOL.connection()
        res = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchJournal'].format(keyword=k['keyword'])
        cursor.execute(sql)
        res = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return res

 # 查找测评
def searchTest(k):
    try:
        client = POOL.connection()
        res = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchTest'].format(keyword=k['keyword'])
        cursor.execute(sql)
        res = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return res

# 实时热门排行
def hotSearch():
    try:
        client = POOL.connection()
        hot_search = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['hotSearch']
        cursor.execute(sql)
        hot_search = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return hot_search

# 热门日记排行
def hotDairy():
    try:
        client = POOL.connection()
        hot_dairy = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['hotDairy']
        cursor.execute(sql)
        hot_dairy = cursor.fetchall()
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return hot_dairy

# 热门妆品排行
def hotCosmetics():
    try:
        client = POOL.connection()
        hot_cosmetics = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['hotCosmetics']
        cursor.execute(sql)
        hot_cosmetics = cursor.fetchall()
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return hot_cosmetics


def getUserName(id):
    try:
        client = POOL.connection()
        username = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['getUserName'].format(user_id=id)
        cursor.execute(sql)
        username = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return username

# 热搜关键字排行获取
def hotKeyword():
    try:
        client = POOL.connection()
        keyword = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['hotKeyword']
        cursor.execute(sql)
        keyword = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return keyword

# 记录搜索关键字
def recordKeyword(k):
    try:
        client = POOL.connection()
        keyword = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['recordKeyword'].format(keyword=k['keyword'],user_id=k['user_id'])
        keyword = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return keyword

# 查询单个商品
def searchCommodity(id):
    try:
        client = POOL.connection()
        com = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchCommodity'].format(id=id)
        cursor.execute(sql)
        com = cursor.fetchone()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return com

# 查询单个商品评论
def commodityComment(id):
    try:
        client = POOL.connection()
        com = -1
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['commodityComment'].format(id=id)
        cursor.execute(sql)
        com = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return com