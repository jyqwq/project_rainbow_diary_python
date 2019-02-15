from . import POOL
import pymysql
from app.dao.sql.search_sql import *


# 根据产品搜索的源码
def searchByProductName(k):
    try:
        client = POOL.connection()
        res = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchByProductName'].format(keyword=k['search'],category_id=k['condition'])
        cursor.execute(sql)
        res = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return res

def searchAll(k):
    try:
        client = POOL.connection()
        res = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = search_sql['searchAll'].format(keyword=k['search'])
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