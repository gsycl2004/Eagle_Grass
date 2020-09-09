# coding: utf-8
# 快速生草辅助装置：用于处理文章段落，使之可以骗过谷歌娘的token识别机制


# 段落处理函数
def deal_para(string):
    new = ''
    symbols = ['，', '。', '.', '?', '!', ';', '？', '！', '…', '—', '；', '\n']
    # 将所有symbols全换成半角逗号
    for i in string:
        if i in symbols:
            new += ','
        else:
            new += i
    # 如果两个逗号之间字符串长度小于等于7，则删除后面的逗号
    str_list = new.split(',')
    real = ''
    for element in str_list:
        if len(element) <= 7:
            real += element
        else:
            real += element + ','
    return real


# 文章处理函数：依据换行符，将文章分段
def deal_essay(essay):
    # 首先可以确定一点，essay是一种神奇的字符串
    paragraphs = essay.split('\n')
    # 去除空行
    for i in paragraphs:
        if i == '':
            paragraphs.remove(i)
    return paragraphs


if __name__ == '__main__':
    with open('essay.txt', mode='r', encoding='utf-8') as fp:
        data = fp.read()
    print(deal_essay(data))
    print('23'[::-2])

