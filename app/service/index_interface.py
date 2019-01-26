from app.dao.index_interface_module import *
import json

# 量身推荐
def recommended_Volume(skin):
    if skin:
        res=recommendedVolume(skin)
        if res and res == -1:
            return {"status_code":"40005","status_text":"数据格式不合法"}
        elif res:
            return res
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code":"40005","status_text":"数据格式不合法"}

# 热门动态
def hot_Dynamic():
    res=hotDynamic()
    if res:
        return res
    else:
        return {"status_code": "40004", "status_text": "系统错误"}

# 测评资讯
def evaluation_Information():
    res=evaluationInformation()
    if res:
        return res
    else:
        return {"status_code": "40004", "status_text": "系统错误"}

if __name__ == '__main__':
    skin = {'skinid': 1}
    print(hot_Dynamic())