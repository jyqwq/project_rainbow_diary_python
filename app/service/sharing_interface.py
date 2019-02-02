from app.dao.sharing_interface_module import *


# 发布心情的封装方法
def graphic_Dy(con):
    if con.get('content') and con.get('img') and con.get('tag'):
        res = graphicDy(con)
        if res:
            return {"status_code":"10008","status_text":"发布成功"}
        else:
            return {"status_code":"40004","status_text":"系统错误"}
    else:
        return {"status_code":"40005","status_text":"数据格式不合法"}

# 发布日记的封装方法
def graphic_Dairy(con):
    if con.get('title') and con.get('content') and con.get('img') and con.get('tag'):
        res = graphicDairy(con)
        if res:
            return {"status_code":"10008","status_text":"发布成功"}
        else:
            return {"status_code":"40004","status_text":"系统错误"}
    else:
        return {"status_code":"40005","status_text":"数据格式不合法"}

# 发布测评的封装方法
def graphic_Test(con):
    if con.get('title') and con.get('content') and con.get('img') and con.get('tag') and con.get('title1') and con.get('content1') and con.get('title2') and con.get('content2'):
        res = graphicTest(con)
        if res:
            return {"status_code":"10008","status_text":"发布成功"}
        else:
            return {"status_code":"40004","status_text":"系统错误"}
    else:
        return {"status_code":"40005","status_text":"数据格式不合法"}

# 测评页面获取数据
def evaluation_Index():
    res=evaluationIndex()
    if res:
        return res
    else:
        return {"status_code":"40004","status_text":"系统错误"}