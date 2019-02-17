from . import POOL
import pymysql
from app.dao.sql.user_sql import *


# 普通用户注册的源码
def commonRegister(user):
    try:
        user_id = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['commonRegister'].format(telephone=user['telephone'], password=user['password'],
                                                nickname=user['nickname'])
        user_id = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        if user_id == 1:
            user_id = getUserByTel(user['telephone'])
        client.close()
        return user_id


# 通过tel获取用户基本信息
def getUserByTel(tel):
    try:
        res_user = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['getUserByTel'].format(telephone=tel)
        cursor.execute(sql)
        res_user = cursor.fetchone()
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return res_user

# 通过Tel获取Password
def getPassword(tel):
    try:
        user_pwd = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['getPassword'].format(telephone=tel)
        cursor.execute(sql)
        user_pwd = cursor.fetchone()
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return user_pwd

# 通过id查找用户信息
def getUserById(id):
    try:
        user = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['getUserById'].format(user_id=id)
        cursor.execute(sql)
        user = cursor.fetchone()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return user

# 关注动态页面
def myDynamics(id):
    try:
        all_dy = -1
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['myDynamics'].format(user_id=id)
        cursor.execute(sql)
        all_dy = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return all_dy

# 获取单个动态
def getDyById(u):
    try:
        one_dy = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['getDyById'].format(tb=u['type'],id=u['id'])
        cursor.execute(sql)
        one_dy = cursor.fetchone()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return one_dy

# 单个测评
def getTestById(id):
    try:
        one_dy = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['getTestById'].format(id=id)
        cursor.execute(sql)
        one_dy = cursor.fetchone()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return one_dy

# 增加关注的源码
def increaseConcerns(u):
    try:
        myf = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['increaseConcerns'].format(user_id=u['user_id'], other_id=u['other_id'])
        myf = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myf


# 删除关注的源码
def deleteConcerns(u):
    try:
        myf = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['deleteConcerns'].format(user_id=u['user_id'], other_id=u['other_id'])
        myf = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myf


# 查看关注的源码
def viewConcern(u):
    try:
        myf = -1
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['viewConcerns'].format(user_id=u['user_id'], other_id=u['other_id'])
        cursor.execute(sql)
        myf = cursor.fetchone()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myf


# 商家企业入驻申请的源码
def applicationForResidence():
    pass


# 申请名人认证的源码
def celebrityCertification():
    pass


# 肤质测试的源码
def skinTest():
    pass


# 删除日志动态的源码
def deleteDynamics():
    pass


# 更改日志动态的源码
def updateDynamics():
    pass


# 关键字查询自己的动态的源码
def viewMyDynamics():
    pass


# 增加收藏的源码
def increaseCollection():
    pass


# 删除收藏的源码
def deleteCollection():
    pass


# 查看收藏的源码
def viewCollections():
    pass


# 增加点赞的源码
def increaseCompliment():
    pass


# 删除点赞的源码
def deleteCompliment():
    pass


# 查看点赞的源码
def viewCompliment():
    pass




# 添加计时化妆品的源码
def addTimeCosmetics():
    pass
