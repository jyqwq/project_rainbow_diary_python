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
                                                nickname=user['nickname'],data=user['data'])
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


# 通过nickname获取用户id
def getUserByName(name):
    try:
        res_user = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['getUserByName'].format(name=name)
        cursor.execute(sql)
        res_user = cursor.fetchone()
        client.commit()
    except Exception as ex:
        print(ex)
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

# 个人动态
def mineDy(id):
    try:
        all_dy = -1
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['mineDy'].format(user_id=id)
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
        sql1 = user_sql['updateClick'].format(id=u['id'], tp=u['type'])
        cursor.execute(sql1)
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
def getTestById(u):
    try:
        one_dy = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['getTestById'].format(id=u['id'])
        sql1 = user_sql['updateClick'].format(id=u['id'],tp=u['uptype'])
        cursor.execute(sql1)
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
        sql = user_sql['increaseConcerns'].format(user_id=u['user_id'], other_id=u['other_id'],data=u['data'])
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

# 更新用户信息
def updateUserMessage(u):
    try:
        myM = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['updateUserMessage'].format(user_id=u['user_id'], user_nickname=u['user_nickname'],user_phone=u['user_phone'],user_sex=u['user_sex'],user_age=u['user_age'],user_autograpgh=u['user_autograpgh'])
        myM = cursor.execute(sql)
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myM


# 增加收藏的源码
def increaseCollection(u):
    try:
        myf = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        cursor1 = client.cursor(cursor=pymysql.cursors.DictCursor)
        cursor2 = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['increaseCollection'].format(user_id=u['user_id'], other_id=u['other_id'], tp=u['type'],data=u['data'])
        sql1 = user_sql['updateCollection1'].format(user_id=u['user_id'])
        sql2 = user_sql['updateCollection11'].format(tp=u['uptype'],id=u['other_id'])
        myf = cursor.execute(sql)
        cursor1.execute(sql1)
        cursor2.execute(sql2)
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myf


# 删除收藏的源码
def deleteCollection(u):
    try:
        myf = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        cursor1 = client.cursor(cursor=pymysql.cursors.DictCursor)
        cursor2 = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['deleteCollection'].format(user_id=u['user_id'], other_id=u['other_id'], tp=u['type'])
        sql1 = user_sql['updateCollection0'].format(user_id=u['user_id'])
        sql2 = user_sql['updateCollection00'].format(tp=u['uptype'], id=u['other_id'])
        myf = cursor.execute(sql)
        cursor1.execute(sql1)
        cursor2.execute(sql2)
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myf


# 查看收藏的源码
def viewCollections(u):
    try:
        myf = -1
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['viewCollections'].format(user_id=u['user_id'], other_id=u['other_id'], tp=u['type'])
        cursor.execute(sql)
        myf = cursor.fetchone()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myf


# 增加点赞的源码
def increaseCompliment(u):
    try:
        myf = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['increaseCompliment'].format(user_id=u['user_id'], other_id=u['other_id'], tp=u['type'],data=u['data'])
        sql1 = user_sql['updateCompliment1'].format(user_id=u['user_id'])
        sql2 = user_sql['updateCompliment11'].format(tp=u['uptype'], id=u['other_id'])
        myf = cursor.execute(sql)
        cursor.execute(sql1)
        cursor.execute(sql2)
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myf


# 删除点赞的源码
def deleteCompliment(u):
    try:
        myf = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        cursor1 = client.cursor(cursor=pymysql.cursors.DictCursor)
        cursor2 = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['deleteCompliment'].format(user_id=u['user_id'], other_id=u['other_id'], tp=u['type'])
        sql1 = user_sql['updateCompliment0'].format(user_id=u['user_id'])
        sql2 = user_sql['updateCompliment00'].format(tp=u['uptype'], id=u['other_id'])
        myf = cursor.execute(sql)
        cursor1.execute(sql1)
        cursor2.execute(sql2)
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myf


# 查看点赞的源码
def viewCompliment(u):
    try:
        myf = -1
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['viewCompliment'].format(user_id=u['user_id'], other_id=u['other_id'], tp=u['type'])
        cursor.execute(sql)
        myf = cursor.fetchone()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myf

# 增加评论
def increaseComment(u):
    try:
        myf = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['increaseComment'].format(user_id=u['user_id'], other_id=u['other_id'],type=u['type'],content=u['content'],data=u['data'])
        sql1 = user_sql['updateComment1'].format(other_id=u['other_id'],tp=u['uptype'])
        sql2 = user_sql['updateComment11'].format(user_id=u['user_id'])
        myf = cursor.execute(sql)
        cursor.execute(sql1)
        cursor.execute(sql2)
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myf

# 删除评论
def deleteComment(u):
    pass

# 查看评论
def viewComment(u):
    try:
        myf = -1
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['viewComment'].format(type=u['type'],tp=u['uptype'],id=u['id'])
        cursor.execute(sql)
        myf = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myf


# 查看我的收藏
def mineCollections(id):
    try:
        myf = -1
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = user_sql['mineCollections'].format(id=id)
        cursor.execute(sql)
        myf = cursor.fetchall()
        client.commit()
    except Exception as ex:
        print(ex)
        client.rollback()
    finally:
        client.close()
        return myf

# 添加计时化妆品的源码
def addTimeCosmetics():
    pass


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
def selectMyDynamics():
    pass
