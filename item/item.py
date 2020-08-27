#coding utf-8
#物品管理器 by SN
import configparser
ENUMITEMList =list(enumerate(['油炸心脏',
           '脊椎炒饭',
           '可磨冰木炭架',
           '油炸布尔乔亚',
           "《尖刺》",
           '《狂欢节记录》典藏版',
           '鸽子',
           '老鹰',
           '鹰目jk照（无货，请勿购买，违者自负）',
           '红色水池',
           "他妈的",


           ]))
ITEMLIST = []

class ITEM():
    def __init__(self,id):
        self.iid = id
        self.Name = dict(ENUMITEMList)[id]
        pass

for a,b in ENUMITEMList:
    ITEMLIST.append(ITEM(a))

class ITEMControl():
    def __init__(self, filename):
        self.path = filename
        self.__config = configparser.ConfigParser()
        self.__config.read(self.path, encoding='utf-8')

    def INIT_ITEM(self,uid):
        if not self.__config.has_section(uid):
            self.__config.add_section(uid)
            self.set(uid,'thing','')

    def Add_Item(self,uid,id):
        self.INIT_ITEM(uid)
        self.__config.read(self.path,encoding='utf-8')
        s = self.__config[str(uid)]['thing'].split(',').remove('')
        f = s + id
        NMINFO = ','.join(f)
        self.__config.set(uid,'thing',NMINFO)
        self.__config.write(open(self.path,'w+'))
    def get_ITEM(self,uid):
        self.INIT_ITEM(uid)
        self.__config.read(self.path, encoding='utf-8')
        s = self.__config[str(uid)]['thing'].split(',').remove('')
        return s
if __name__ == '__main__':
    print(ITEMLIST[1].Name)