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
    if con.get('com') and con.get('title') and con.get('content') and con.get('img') and con.get('tag') and con.get('title1') and con.get('content1') and con.get('title2') and con.get('content2'):
        # 转化标签名
        tag_id = get_Tag(con['tag'])
        con['tag_id'] = tag_id
        # 转化产品名
        com_id = get_Com(con['com'])
        con['com_id'] = com_id
        print(con)
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

# 获取标签id
def get_Tag(tags):
    tag_id = []
    for tag_name in tags:
        tagid = getTag(tag_name)
        if tagid:
            tag_id.append(tagid['tags_id'])
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    return tag_id

#获取产品id
def get_Com(com):
    com_id = getCom(com)
    if com_id:
        return com_id['id']
    else:
        return {"status_code": "40004", "status_text": "系统错误"}

if __name__ == '__main__':
    u = {'com':'大宝SOD','user_id':21,'title':'test','content':'this is test','title1':'title-1','content1':'content-1','title2':'title-2','content2':'content-2','img':'img/myimg.jpg','type':'test','tag':['保湿','提亮肤色']}
    # u = ['保湿','提亮肤色']
    # u = '大宝SOD'
    res=graphic_Test(u)
    print(res)