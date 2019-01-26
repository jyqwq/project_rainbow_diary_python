import jwt
from app.config import SECRECT_KEY
def createToken(tel):
    import datetime
    import hashlib
    # 当前时间加上180秒，意味着token过期时间为3分钟以后
    datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(seconds=60*60*24)
    option = {
        'iss': 'rainbow_diary.com',  # token的签发者
        'exp': datetimeInt,  # 过期时间
        'iat': datetime.datetime.utcnow(),
        'aud': 'webkit',  # token的接收者，这里指定为浏览器
        'telephone': tel  # 放入用户信息，唯一标识，解析后可以使用该消息
    }
    # encoded2 = jwt.encode(payload=option,key= SECRECT_KEY, algorithm='HS256',options= {'verify_exp':True})
    # 这时token类型为字节类型，如果传个前端要进行token.decode()
    token = jwt.encode(option, SECRECT_KEY, 'HS256')
    return token.decode()
def checkToken(token):
    try:
        decoded = jwt.decode(token, SECRECT_KEY, audience='webkit', algorithms=['HS256'])
        return decoded['telephone']
    except jwt.ExpiredSignatureError as ex:
        return None