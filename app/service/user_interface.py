from app.dao.user_interface_module import *
import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask import make_response
from app.utils.my_token import *
from app.app import app

app.app_context().push()


# 普通用户注册的封装方法
def common_Register(user):
    if user.get('telephone') and user.get('password') and user.get('nickname'):
        pf = generate_password_hash(user['password'], method='pbkdf2:sha1:1001', salt_length=8)
        user['password'] = pf
        nn = getUserByName(u['user_nickname'])
        if nn:
            return {"status_code": "10000", "status_text": "用户名已经存在"}
        rr = getUserByTel(user['telephone'])
        if rr:
            return json.dumps({"status_code": "10002", "status_text": "用户已经存在"})
        else:
            res = commonRegister(user)
            if res:
                token = createToken(user['telephone'])
                response = make_response()
                response.data = json.dumps(
                    {"status_code": "10003", "status_text": "登录成功", "token": token, "usermessage": res})
                response.status_code = 200
                return response
            else:
                return json.dumps({"status_code": "40004", "status_text": "系统错误"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


# 登录方法
def get_User(user):
    if user.get('telephone') and user.get('password'):
        rr = getUserByTel(user['telephone'])
        if rr:
            user_pwd = getPassword(user['telephone'])
            if user_pwd:
                if (check_password_hash(user_pwd['user_password'], user['password'])):
                    token = createToken(user['telephone'])
                    response = make_response()
                    response.data = json.dumps(
                        {"status_code": "10003", "status_text": "登录成功", "token": token, "usermessage": rr})
                    response.status_code = 200
                    return response
                else:
                    return json.dumps({"status_code": "10005", "status_text": "密码错误"})
            else:
                return json.dumps({"status_code": "40004", "status_text": "系统错误"})
        else:
            return json.dumps({"status_code": "10004", "status_text": "该用户不存在"})
    else:
        return json.dumps({"status_code": "40005", "status_text": "数据格式不合法"})


# 自动登录检查token
def check_Token(token):
    if token:
        res = checkToken(token)
        if res:
            res = getUserByTel(res)
            if res:
                return {"status_code": "10003", "status_text": "登录成功", "usermessage": res}
            else:
                return {"status_code": "40004", "status_text": "系统错误"}
        else:
            return {"status_code": "10006", "status_text": "登录过期"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 获取用户基本信息
def get_User_By_Id(id):
    if id['user_id']:
        res = getUserById(int(id['user_id']))
        if res:
            return res
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 关注的动态
def my_Dynamics(u):
    if u and u['user_id']:
        res = myDynamics(u['user_id'])
        if res == -1:
            return {"status_code": "40004", "status_text": "系统错误"}
        else:
            for i in res:
                c = getUserById(i['user_id'])
                if c:
                    i['user_message'] = c
                else:
                    return {"status_code": "40004", "status_text": "系统错误"}
                if i['id'] and i['t_name']:
                    j = {'user_id':u['user_id'],'other_id':i['id'],'type':i['t_name']}
                    # print(j)
                    col = view_Collections(j)
                    com = view_Compliment(j)
                    if col and com:
                        i['collection']=col
                        i['compliment']=com
                    else:
                        return {"status_code": "40004", "status_text": "系统错误"}
                else:
                    return {"status_code": "40005", "status_text": "数据格式不合法"}
            return res
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}

# 个人动态
def mine_Dy(u):
    if u and u['user_id']:
        res = mineDy(u['user_id'])
        if res == -1:
            return {"status_code": "40004", "status_text": "系统错误"}
        else:
            for i in res:
                if i['id'] and i['t_name']:
                    j = {'user_id':u['user_id'],'other_id':i['id'],'type':i['t_name']}
                    # print(j)
                    col = view_Collections(j)
                    com = view_Compliment(j)
                    if col and com:
                        i['collection']=col
                        i['compliment']=com
                    else:
                        return {"status_code": "40004", "status_text": "系统错误"}
                else:
                    return {"status_code": "40005", "status_text": "数据格式不合法"}
            return res
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}

# 单个动态
def get_Dy_By_Id(u):
    # 单个测评
    if u['id'] and u['type'] == 'test':
        u['uptype'] = 'commodity_test_main'
        res = getTestById(u)
    # 心情和日记
    elif u['id'] and (u['type'] == 'dynamic' or u['type'] == 'journal'):
        res = getDyById(u)
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}
    if res and res['user_id']:
        i = getUserById(res['user_id'])
        if i:
            res['user_message'] = i
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
        if res['id'] and u['type'] and u['user_id']:
            j = {'user_id': u['user_id'], 'other_id': res['id'], 'type': u['type']}
            col = view_Collections(j)
            com = view_Compliment(j)
            if col and com:
                res['collection'] = col
                res['compliment'] = com
            else:
                return {"status_code": "40004", "status_text": "系统错误"}
        else:
            return {"status_code": "40005", "status_text": "数据格式不合法"}
        return res
    else:
        return {"status_code": "40004", "status_text": "系统错误"}


# 增加关注的封装方法
def increase_Concerns(u):
    if u and u['user_id'] and u['other_id']:
        if u['user_id'] == u['other_id']:
            return {"status_code":"10022","status_text":"不能关注自己"}
        res = increaseConcerns(u)
        if res:
            return {"status_code": "10009", "status_text": "关注成功"}
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 删除关注的封装方法
def delete_Concerns(u):
    if u and u['user_id'] and u['other_id']:
        res = deleteConcerns(u)
        if res:
            return {"status_code": "10010", "status_text": "删除成功"}
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 查看是否关注的封装方法
def view_Concern(u):
    if u and u['user_id'] and u['other_id']:
        res = viewConcern(u)
        if res:
            if res == -1:
                return {"status_code": "40004", "status_text": "系统错误"}
            elif type(res) == type({"1": "1"}):
                return {"status_code": "10011", "status_text": "已关注"}
        else:
            return {"status_code": "10012", "status_text": "未关注"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 更新用户信息
def update_User_Message(u):
    if u and u['user_id'] and u['user_nickname'] and u['user_phone'] and u['user_age'] and u[
        'user_autograpgh']:
        nn = getUserByName(u['user_nickname'])
        if int(nn['user_id']) == int(u['user_id']):
            pass
        else:
            return {"status_code": "10000", "status_text": "用户名已经存在"}
        rr = getUserById(u['user_id'])
        if rr:
            if rr['user_phone'] == u['user_phone']:
                res = updateUserMessage(u)
            else:
                mm = getUserByTel(u['user_phone'])
                if mm:
                    return {"status_code": "10002", "status_text": "用户已经存在"}
                else:
                    res = updateUserMessage(u)
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
        if res:
            return {"status_code": "10014", "status_text": "更新成功"}
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 增加收藏的封装方法
def increase_Collection(u):
    if u and u['user_id'] and u['other_id'] and u['type']:
        if u['type'] == 'test':
            u['uptype'] = 'commodity_test_main'
        elif u['type'] == 'journal':
            u['uptype'] = 'journal'
        elif u['type'] == 'dynamic':
            u['uptype'] = 'dynamic'
        res = increaseCollection(u)
        if res == 1:
            return {"status_code": "10015", "status_text": "收藏成功"}
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 删除收藏的封装方法
def delete_Collection(u):
    if u and u['user_id'] and u['other_id'] and u['type']:
        if u['type'] == 'test':
            u['uptype'] = 'commodity_test_main'
        elif u['type'] == 'journal':
            u['uptype'] = 'journal'
        elif u['type'] == 'dynamic':
            u['uptype'] = 'dynamic'
        res = deleteCollection(u)
        if res == 1:
            return {"status_code": "10010", "status_text": "删除成功"}
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 查看收藏的封装方法
def view_Collections(u):
    if u and u['user_id'] and u['other_id'] and u['type']:
        res = viewCollections(u)
        if res:
            if res == -1:
                return {"status_code": "40004", "status_text": "系统错误"}
            elif type(res) == type({"1": "1"}):
                return {"status_code": "10016", "status_text": "已收藏"}
        else:
            return {"status_code": "10017", "status_text": "未收藏"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 增加点赞的封装方法
def increase_Compliment(u):
    if u and u['user_id'] and u['other_id'] and u['type']:
        if u['type'] == 'test':
            u['uptype'] = 'commodity_test_main'
        elif u['type'] == 'journal':
            u['uptype'] = 'journal'
        elif u['type'] == 'dynamic':
            u['uptype'] = 'dynamic'
        res = increaseCompliment(u)
        if res == 1:
            return {"status_code": "10018", "status_text": "赞成功"}
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 删除点赞的封装方法
def delete_Compliment(u):
    if u and u['user_id'] and u['other_id'] and u['type']:
        if u['type'] == 'test':
            u['uptype'] = 'commodity_test_main'
        elif u['type'] == 'journal':
            u['uptype'] = 'journal'
        elif u['type'] == 'dynamic':
            u['uptype'] = 'dynamic'
        res = deleteCompliment(u)
        if res == 1:
            return {"status_code": "10010", "status_text": "删除成功"}
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 查看点赞的封装方法
def view_Compliment(u):
    if u and u['user_id'] and u['other_id'] and u['type']:
        res = viewCompliment(u)
        if res:
            if res == -1:
                return {"status_code": "40004", "status_text": "系统错误"}
            elif type(res) == type({"1": "1"}):
                return {"status_code": "10019", "status_text": "已赞"}
        else:
            return {"status_code": "10020", "status_text": "未赞"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 添加评论
def increase_Comment(u):
    if u and u['user_id'] and u['other_id'] and u['type'] and u['content']:
        if u['type'] == 'test':
            u['uptype'] = 'commodity_test_main'
        elif u['type'] == 'journal':
            u['uptype'] = 'journal'
        elif u['type'] == 'dynamic':
            u['uptype'] = 'dynamic'
        res = increaseComment(u)
        if res == 1:
            return {"status_code": "10021", "status_text": "评论成功"}
        else:
            return {"status_code": "40004", "status_text": "系统错误"}
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}

# 删除评论
def delete_Comment(u):
    pass

# 查看评论
def view_Comment(u):
    if u and u['id'] and u['type']:
        if u['type'] == 'test':
            u['uptype'] = 'commodity_test_main'
        elif u['type'] == 'journal':
            u['uptype'] = 'journal'
        elif u['type'] == 'dynamic':
            u['uptype'] = 'dynamic'
        res = viewComment(u)
        if res == -1:
            return {"status_code": "40004", "status_text": "系统错误"}
        else:
            if res:
                for i in res:
                    c = getUserById(i['user_id'])
                    if c:
                        i['user_message'] = c
                    else:
                        return {"status_code": "40004", "status_text": "系统错误"}
            return res
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}


# 查看我的收藏
def mine_Collections(u):
    if u and u['user_id']:
        res = mineCollections(u['user_id'])
        if res == -1:
            return {"status_code": "40004", "status_text": "系统错误"}
        else:
            for i in res:
                c = getUserById(i['user_id'])
                if c:
                    i['user_message'] = c
                else:
                    return {"status_code": "40004", "status_text": "系统错误"}
                if i['id'] and i['t_name']:
                    j = {'user_id':u['user_id'],'other_id':i['id'],'type':i['t_name']}
                    # print(j)
                    col = view_Collections(j)
                    com = view_Compliment(j)
                    if col and com:
                        i['collection']=col
                        i['compliment']=com
                    else:
                        return {"status_code": "40004", "status_text": "系统错误"}
                else:
                    return {"status_code": "40005", "status_text": "数据格式不合法"}
            return res
    else:
        return {"status_code": "40005", "status_text": "数据格式不合法"}

# 添加计时化妆品的封装方法
def add_Time_Cosmetics():
    pass


# 商家企业入驻申请的封装方法
def application_For_Residence():
    pass


# 申请名人认证的封装方法
def celebrity_Certification():
    pass


# 肤质测试的封装方法
def skin_Test():
    pass


# 删除日志动态的封装方法
def delete_Dynamics():
    pass


# 更改日志动态的封装方法
def update_Dynamics():
    pass


# 关键字查询自己的动态的封装方法
def view_My_Dynamics():
    pass


if __name__ == '__main__':
    user = {"telephone": "13812383824", "password": "123456", "nickname": "JyQQ", 'user_id': 21}
    u = {'user_id': 21, 'user_nickname': 'yy', 'user_phone': '12345645666', 'user_sex': 2, 'user_age': 12,
         'user_autograpgh': '个性签名'}
    a = {'user_id':1,'other_id':11,'type':'test'}
    c = {'id':1,'type':'test'}
    aa = {'user_id':1,'other_id':1,'type':'test','content':'123456789'}
    # res=common_Register(user)
    # res = my_Dynamics(user)
    # res = get_User(user)
    # res = get_Dy_By_Id({'type': 'journal', 'id': 1})
    # res = view_Concern({'user_id':21,'other_id':2})
    # res = update_User_Message(u)
    res = mine_Collections(aa)
    print(res)
