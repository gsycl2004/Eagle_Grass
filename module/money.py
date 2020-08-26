import configparser
import time
ShopList =[('油炸心脏',7),
           ('脊椎炒饭',25),
           ('可磨冰木炭架',50),
           ('油炸布尔乔亚',50),
           ("《尖刺》",100),
           ('《狂欢节记录》典藏版',200),
           ('鸽子',400),
           ('老鹰',2000),
           ('鹰目jk照（无货，请勿购买，违者自负）',4000),
           ('红色水池',100),
           ("他妈的",1)
           ]




class money:
    #
    #
    #
    #油炸心脏 10
#   脊椎炒饭 50
#   油炸布尔乔亚 100
#   鸽子 400
#   老鹰 2000
#   鹰目jk照 2000
#   鹰目视频 10000
#   鹰目等身手办 980000


    def __init__(self,filename):
        self.path = filename
        self.__config = configparser.ConfigParser()
        self.__config.read(self.path,encoding='utf-8')
    def intalized_member(self,userid,money=10):
        # 检查是否存在section
        self.__config.add_section(str(userid))
        self.__config.set(str(userid),'money',str(money))
        self.__config.set(str(userid), 't',str(0))
        self.__config.write(open(self.path,'w+'))


    def getmoney(self,userid):
        s = self.__config
        s.read(self.path)
        try:
            return s[str(userid)]['money']
        except KeyError:
            self.intalized_member(userid,money=10)
            return s[str(userid)]['money']

    def changemoney(self,userid,num,u=False):

        f = int(self.__config[str(userid)]['money'])
        f = f + num
        self.__config.set(str(userid), 'money', str(f))
        self.__config.write(open(self.path, 'w+'))
        if u:
            self._updata_time(userid)
    def hasmember(self,user_id):
        if self.__config.has_section(str(user_id)):

            return True
        else:
            return False

    def get_date(self,user_id):
        return self.__config[str(user_id)]['t']
    def get_date2(self,user_id):
        return self.__config[str(user_id)]['t2']

    def _updata_time(self,user_id):
        self.__config.set(str(user_id), 't', str(time.localtime(time.time()).tm_mday))
        self.__config.write(open(self.path, 'w+'))
    def _updata_time2(self,user_id):
        self.__config.set(str(user_id), 't2', str(time.localtime(time.time()).tm_mday))
        self.__config.write(open(self.path, 'w+'))
    def MoneyList(self):
        return self.__config.sections()

    def Comp(self,compid,compname,user,lience='生草部'):

        self.__config.set(str(user), 'compname', str(compname))
        self.__config.set(str(user), 'lience', str(lience))
        self.__config.set(str(user), 'comapny', str(compid))

    def setitem(self,cid,user,status):
        s = list(enumerate(ShopList))
        flist = {}
        for h in s:
            flist[h[1][0]] = h[0]
        wads = self.getitem(user)
        fdict ={}
        try:
            for h in wads:
                print(h)
                e,f,c = h[0][0],h[0][1],h[1]
                fdict[e]=c
            f = status +fdict[cid]
            self.__config.set(str(user),str(flist[cid]),str(f))
            self.__config.write(open(self.path, 'w+'))
        except:
            self.__config.set(str(user), str(flist[cid]), str(f))
            self.__config.write(open(self.path, 'w+'))
    def getitem(self,uid):
        f = []
        s = self.__config
        s.read(self.path)
        if not s.has_section(str(uid)):
            return True
        for h in range(len(ShopList)):
            try:
                if int(s[str(uid)][str(h)]) > 0:
                    f.append([ShopList[h],int(s[str(uid)][str(h)])])

            except:
                pass
        return f

class shop():
    def __init__(self):
        self._My = money('Edata/物品数据.ini')
        self.item = ShopList
    def get_menu(self,group=None):
        msg = ''
        for a,b in ShopList:
            msg = msg + '物品：{a} 价格{b}\n'.format(a =a,b =b)
        return msg

    def setitem(self,cid,user,status):
        self._My.setitem(cid,user,status)
    def getitem(self,user):
       return self._My.getitem(user)


    def GetMyItem(self,uid):
        msg = ''
        s = self.getitem(uid)
        for h,_ in s:

            msg = msg +'{h}*{y}\n'.format(h=h[0],y =_)
            print(s)
        return msg


    def itemlist(self,uid):
        s = self.getitem(uid)
        dictfaa = {}
        for h in s:
            dictfaa[h[0][0]] = h[1]
        return dictfaa

if __name__ == '__main__':
    s= shop()

    #s.setitem()
    f = s.setitem('《狂欢节记录》典藏版',1728026105,-41)
    s = s.itemlist(1728026105)
    print(s)

