# 传入字符串找出其中所有数字返回数组
def strToNum(str):
    import re
    res = re.findall(r"\d", str)
    num = []
    for i in res:
        i = int(i)
        num.append(i)
    return num

# 传入数组,转成用逗号分隔的字符串
def toStr(u):
    str = ''
    j = 1
    for i in u:
        if j == 1:
            str = str + i
            j += 1
        else:
            str = str + ',' + i
    return str

if __name__ == '__main__':
    u = ['a','b','c']
    a = toStr(u)
    print(a)