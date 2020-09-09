

def encode(b):
    h = ''
    s = [ord(h)+500 for h in b]
    f = [chr(h) for h in s]
    for ss in f:
        h +=ss
    return h


def decode(b):
    h = ''
    s = [ord(h)-500 for h in b]
    f = [chr(h) for h in s]
    for ss in f:
        h +=ss
    return h




if __name__ == "__main__":
    print(decode(encode("我是希果")))