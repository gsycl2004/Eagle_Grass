# coding: utf-8
# 快速生草核心装置：用于实现与谷歌娘的正常通信
# 导入浏览器头和语言字典
# 参考：https://blog.csdn.net/fengyulinde/article/details/86632837
from module.heads import HEADER
import requests
import execjs  # 用来跑js
import json
from urllib.parse import quote
from module.paragraph import deal_para
# 杀死多余进程
s = requests.session()
s.keep_alive = False


# 连接网页（请在联网状态下使用）
def check_list(url, head):
    # 连接网页
    response = requests.get(url, headers=head)
    # 设置编码
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    # 返回连接的文本
    return response.text


# 找谷歌娘要token
class Py4Js:
    def __init__(self):
        self.ctx = execjs.compile(""" 
            // 翻译内容输出, 并得到token
            function TL(a) { 
                var k = ""; 
                var b = 406644; 
                var b1 = 3293161072;       
                var jd = "."; 
                var $b = "+-a^+6"; 
                var Zb = "+-3^+b+-f";    
                for (var e = [], f = 0, g = 0; g < a.length; g++) { 
                    var m = a.charCodeAt(g); 
                    128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
                    e[f++] = m >> 18 | 240, 
                    e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
                    e[f++] = m >> 6 & 63 | 128), 
                    e[f++] = m & 63 | 128) 
                } 
                a = b; 
                for (f = 0; f < e.length; f++) a += e[f], 
                a = RL(a, $b); 
                a = RL(a, Zb); 
                a ^= b1 || 0; 
                0 > a && (a = (a & 2147483647) + 2147483648); 
                a %= 1E6; 
                return a.toString() + jd + (a ^ b) 
            };      
            // token接受
            function RL(a, b) { 
                var t = "a"; 
                var Yb = "+"; 
                for (var c = 0; c < b.length - 2; c += 3) { 
                    var d = b.charAt(c + 2), 
                    d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
                    d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
                    a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
                } 
                return a 
            }
        """)

    # 获得翻译的token
    def get_tk(self, text):
        return self.ctx.call("TL", text)


# 建立传送门，传入参数：文本，谷歌娘识别用的token，以及目标语言符号（默认简体中文）
def build_url(text, tk, tl='zh-CN'):
    return 'https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=' + tl + \
           '&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&source=btn&ssel=0&tsel=0&kc=0&tk=' \
           + str(tk) + '&q=' + quote(text, encoding='utf-8')


# 核心功能：翻译, 传入javascript代码，翻译文本以及目标语言（简体中文）
def translate(js, text, tl='zh-CN'):
    # 搭建传送门，进入翻译界面
    url = build_url(text, js.get_tk(text), tl)
    # 连接到谷歌娘, 返回连接源代码
    response = check_list(url, HEADER)
    # 用json解析连接的结果
    result = json.loads(response)
    # 返回解析结果
    return result


# 提取翻译结果: 传入解析过的html，整合成返回翻译结果
def extract(result):
    # 首先应当过滤不可能有下标的元素(不可迭代)
    for i in result:
        if isinstance(i, str) or isinstance(i, float) or i == []:
            result.remove(i)
    # 如果不是None加入新的列表
    new_list = list(filter(None, result))[0][:-1]
    new_string = ''
    # 提取字符串连成句子
    for l in new_list:
        new_string += l[0]
    return new_string


# 绑定：翻译单元函数, 传入文本和目标语言（单次翻译，只针对一段）
def google_trans(text, tl):
    # 单次翻译之前先处理字符串
    text = deal_para(text)
    result = extract(translate(js=Py4Js(), text=text, tl=tl))
    return result, text


if __name__ == '__main__':
    with open('text.txt', mode='r', encoding='utf-8') as fps:
        data = fps.read()
    res = google_trans(text=data, tl='en')
    print('原文：{}'.format(res[1]))
    print('Google：{}'.format(res[0]))
