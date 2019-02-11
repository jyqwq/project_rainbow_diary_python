from . import POOL
import pymysql
from app.dao.sql.search_sql import *


# 根据产品名搜索的源码
def searchByProductName(name):
    pass


# 根据成分产品名搜索的源码
def searchByComponent(component):
    pass


# 根据功能搜索的源码
def searchByFunction(func):
    pass


# 根据肤质搜索的源码
def searchBySkin(skin):
    pass


# 根据动态标签搜索的源码
def searchByDynamic(dynamic):
    pass

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