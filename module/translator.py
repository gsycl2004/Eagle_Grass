# coding: utf-8
# 这是你的生草装置的核心，它的本质在于向百度翻译发送数据
import time
import requests
import random
import hashlib
import json

# 谷歌娘调教师友情赞助, 传参和命名方式和百度的保持一致
from module.translation import google_trans as single_trans_google


# 单次翻译的功能，拿出来，传入翻译字符串和目标语言
def single_trans_baidu(content, target):
    # 生成salt,0~1: 一步弄成字符串
    salt = str(random.random())
    # 加密对象，果然要尽量模仿人类完成数据上传。。。（类似之前搞谷歌娘的时候遇到的麻烦）
    m = hashlib.md5()
    s = '20200717000521168' + content + salt + 'LG0CvUHDMWRwziIw9k8S'
    # 标准访问配置操作
    m.update(s.encode())
    data = {
        'q': content.encode(encoding='utf-8'),
        'from': 'auto',
        'to': target,
        'appid': '20200717000521168',
        'salt': salt,
        'sign': m.hexdigest()
    }
    # 啊，你原来用的是百度翻译~，上交翻译的内容
    s = requests.post("http://api.fanyi.baidu.com/api/trans/vip/translate", data=data)
    # 获得翻译的结果，然后连过程带结果一步一步拼好，中间打回车
    f = json.loads(s.text)
    # 直接返回单次翻译的结果，到时候反复调用就ok
    #print(f)
    return f['trans_result'][0]['dst']


def localRender(name):
    result = name  # 准备一个结果空字符串，用于承接翻译的结果
    # 这是你的翻译顺序，应该是中->法->韩->德->中 (当然我又塞了英文，因为发现你的第一句和最后一句完全一致)
    trans_chain = ['zh', 'dan', 'est','ru', 'en']
    # 以下内容是为了实现语法而特有的百度翻译特有的配置，不用乱动
    for i in range(len(trans_chain)):
        # 百度
        if i % 2 == 0:
            result = single_trans_baidu(content=result, target=trans_chain[i])
            # 考虑到百度娘每次的延迟都似乎在增长，因此等待时间应当相应增长
            time.sleep(0.7+i/15)
        # 谷歌
        else:
          try:
            result = single_trans_google(text=result, tl=trans_chain[i])[0]
          except:
              result = single_trans_baidu(content=result, target=trans_chain[i])
        #print('稍微等会就完成了哦~{}/5'.format(i+1))

    # 好了现在开始治疗你的那个病了，尝试写个独立于循环的东西：所有的东西完全一致,
    # 略微处理字符串之后再次翻译（总之不能一样），稍微加个空字符
    result += ''
    result = single_trans_baidu(result, 'zh')
    # 返回翻译结果
    return result

def local(name):
    result = name
    trans_chain = ['zh', 'dan', 'est', 'ru', 'en']
    for i in range(len(trans_chain)):
        result = single_trans_baidu(content=result, target=trans_chain[i])
    result += ''
    result = single_trans_baidu(result, 'zh')
    return result
if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    #print('生草时间：{}'.format(end-start))
