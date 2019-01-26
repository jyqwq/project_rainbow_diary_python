from . import POOL
import pymysql
from app.dao.sql.index_sql import index_sql


# 量身推荐
def recommendedVolume(skin):
    if skin:
        try:
            recommended_volume = None
            client = POOL.connection()
            cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
            sql = index_sql['recommendedVolume'].format(skinid=skin['skinid'])
            cursor.execute(sql)
            recommended_volume = cursor.fetchall()
            client.commit()
        except Exception as ex:
            client.rollback()
        finally:
            client.close()
            return recommended_volume
    else:
        return -1

# 热门动态
def hotDynamic():
    try:
        hot_dynamic = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = index_sql['hotDynamic']
        cursor.execute(sql)
        hot_dynamic = cursor.fetchall()
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return hot_dynamic



# 测评资讯
def evaluationInformation():
    try:
        evaluation_information = None
        client = POOL.connection()
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)
        sql = index_sql['evaluationInformation']
        cursor.execute(sql)
        evaluation_information = cursor.fetchall()
        client.commit()
    except Exception as ex:
        client.rollback()
    finally:
        client.close()
        return evaluation_information