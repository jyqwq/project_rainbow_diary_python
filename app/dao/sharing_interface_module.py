from . import POOL
import pymysql
from app.dao.sql.sharing_sql import *


# 发布心情的源码
def graphicDy(con):
    try:
        dy = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sharing_sql['graphicDy'].format(user_id=con['user_id'],content=con['content'],img=con['img'],tags=con['tag'])
        dy = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        print(ex)
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
        sql = sharing_sql['graphicDairy'].format(user_id=con['user_id'],title=con['title'],content=con['content'],img=con['img'],tags=con['tag'])
        dairy = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return dairy

# 发布测评的源码
def graphicTest(con):
    try:
        test = None
        test_id = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql1 = sharing_sql['graphicTest1'].format(main_title=con['title'],main_content=con['content'],user_id=con['user_id'],tags=con['tag'],img=con['img'])
        cursor.execute(sql1)
        test_id = cursor.lastrowid
        sql2 = sharing_sql['graphicTest2'].format(title1=con['title1'],content1=con['content1'],title2=con['title2'],content2=con['content2'],test_id=test_id)
        test = cursor.execute(sql2)
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return test

# 获取标签id的源码
def getTag(tag):
    try:
        tag_id = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sharing_sql['getTag'].format(tag_name=tag)
        cursor.execute(sql)
        tag_id = cursor.fetchone()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return tag_id

# 获取产品id的源码
def getCom(com):
    try:
        com_id = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = sharing_sql['getCom'].format(com_name=com)
        cursor.execute(sql)
        com_id = cursor.fetchone()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return com_id

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
        print(ex)
        client.rollback()
    finally:
        client.close()
        return eva_content