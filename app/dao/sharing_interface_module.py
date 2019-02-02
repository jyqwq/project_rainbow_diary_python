from . import POOL
import pymysql
from app.dao.sql.sharing_sql import *


# 发布心情的源码
def graphicDy(con):
    try:
        dy = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sharing_sql['graphicDy']
        dy = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return dy

# 发布日记的源码
def graphicDairy(con):
    try:
        dairy = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sharing_sql['graphicDairy']
        dairy = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return dairy

# 发布测评的源码
def graphicTest(con):
    try:
        test = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sharing_sql['graphicTest']
        test = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return test

# 测评页面
def evaluationIndex():
    try:
        client = POOL.connection()
        eva_content = None
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sharing_sql['evaluationIndex']
        cursor.execute(sql)
        eva_content = cursor.fetchall()
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return eva_content