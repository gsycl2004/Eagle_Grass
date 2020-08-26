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

class ITEM():
    def __init__(self,id):
        self.iid = id
        self.Name = dict(ENUMITEMList)[id]
        pass



class ITEMControl():
    def __init__(self, filename):
        self.path = filename
        self.__config = configparser.ConfigParser()
        self.__config.read(self.path, encoding='utf-8')

    def INIT_ITEM(self,uid):
        self.__config.add_section(uid)





if __name__ == '__main__':
    print(ITEM(2).Name)