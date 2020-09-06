from aiocqhttp import CQHttp, Event
import random
import asyncio
import time
import re
from module.translator import *

import text.danger
import module.money as money

# 引入
api_root = "http://127.0.0.1:5700/"
bot = CQHttp(api_root=api_root)

se3r = 0

# 机器人进群，协程
@bot.on_message('group')
async def main(event: Event):
    if 1 == 1:
        UID = event.user_id
        Message = event.message
        print(event.message_id)
        GID = event.group_id
        BanGroup = [207218691, 917328338, 1043617974]

        def at(who):
            return '[CQ:at,qq={who}]'.format(who=who)

        async def speak(n):
            await bot.send_group_msg(group_id=event.group_id, message=n)

        def CheckQQ(str):
            pattern = r"[1-9]\d{4,10}"
            res = re.findall(pattern, str, re.I)
            return res

        def CheckM(str):
            pattern = r"[1-9]\d{0,4}"
            res = re.findall(pattern, str, re.I)
            return res

        def PeopleFuc(data, numb):
            Mlist = data.MoneyList()
            MSG = ""
            Memeberlist = [int(data.getmoney(highjack)) for highjack in Mlist]
            Adict = dict(zip(Mlist, Memeberlist))
            r = sorted(Adict.items(), key=lambda kv: (kv[1], kv[0]))[::numb]
            for Fuck in range(0, 5):
                MSG += '{who}拥有{much}鹰草,是第{fuck}名\n'.format(who=at(r[[Fuck][0]][0]), much=str(r[Fuck][1]), fuck=Fuck + 1)
            return MSG

        def GiveMoney(event):
            s = event.message
            print(s)
            uid = CheckQQ(s.replace('转账', '').replace('.', ''))[0]
            qmy = int(s.replace('转账', '').replace('[CQ:at,qq={id}]'.replace('.', '').format(id=uid), ''))
            return uid, qmy

        # 查看数据库
        data = money.money('Edata/物品数据.ini')
        if '.生草开始' == event.message[0:5] and int(data.getmoney(UID)) >= 3:
            msg = Message
            msg2 = msg.replace('生草开始', '').replace('.', "")
            try:
                result = localRender(msg2)
                # 我就生个草尼玛还得投入“鹰草”
                await speak(result)
                # 生草鹰草生完了
                data.changemoney(UID, -1)
            except:
                await speak("生草失败{at}".format(at=at(UID)))
                await asyncio.sleep(3)
                # 生草事故返还鹰草停三秒
        elif '.生草开始' == event.message[0:5]:
            await speak("鹰草花光了{at}".format(at=at(UID)))

        if '.签到' == event.message[0:3]:
            if not data.hasmember(UID):
                data.intalized_member(UID)
            MDAY = time.localtime(time.time()).tm_mday
            if not data.get_date(UID) == str(MDAY):
                data.changemoney(UID, 20, u=True)
                await speak('签到成功获得20鹰草{at}'.format(at=at(UID)))
            else:
                await speak('{at}今天已经签到过了,请明天再来吧'.format(at=at(UID)))

        if '.查询余额' in event.message[0:5]:
            MONey = data.getmoney(UID)
            await speak("{at}的余额为:{no}鹰草".format(at=at(UID), no=MONey))

        if '.人民富豪' == event.message[0:5] and GID not in BanGroup:
            s = PeopleFuc(data, -1)
            await speak(s)
        if '.人民乞丐' == event.message[0:5] and GID not in BanGroup:
            s = PeopleFuc(data, 1)
            print(s)
            await speak(s)

        if '.鹰菜单' == event.message[0:4]:
            msg = ''
            Menulist = ['.生草开始', '.签到', '.人民富豪', '.人民乞丐', '.抽奖', '转账']
            for h in Menulist:
                msg += "[{f}]\n".format(f=h)
            await speak(msg)
            pass

        if '.抽奖' == event.message[0:3] and int(data.getmoney(UID)) >= 5 and GID not in BanGroup:
            Rand_result = random.randint(0, 100)

            def standard(e):
                return "{at}花费5鹰草获得{e}鹰草".format(e=str(e), at=at(UID))

            data.changemoney(UID, -5)
            if 90 <= Rand_result <= 100:
                if int(data.getmoney(UID)) <= 200:
                    data.changemoney(UID, 50)
                    await  speak(standard(50))
                else:  # 超过两百给25我觉得不是很过分
                    data.changemoney(UID, 25)
                    await speak(standard(25))
            elif 80 < Rand_result < 90:
                data.changemoney(UID, 15)
                await speak(standard(15))
            elif 45 < Rand_result < 70:
                d5_10 = random.randint(5, 10)
                data.changemoney(UID, d5_10)
                await speak(standard(d5_10))
            else:  # 小于45就得赔钱，算了我还是不玩了[doge]
                d0_5 = random.randint(0, 5)
                data.changemoney(UID, d0_5)
                await speak(standard(d0_5))
        elif '.抽奖' == event.message[0:3] and not int(data.getmoney(UID)) >= 5:  # 赔光了的倒霉孩子
            await speak("鹰草花光了" + at(UID))
        # elif UID  == 3267992149 and '.抽奖' == event.message[0:3]:
        #    await speak("小号检测发现你是用小号")

        if '.大抽奖' == event.message[0:4] and int(data.getmoney(UID)) >= 50 and GID not in BanGroup:
            Rand_result = random.randint(0, 100)
            data.changemoney(UID, -50)

            def standard(e):
                return "{at}花费50鹰草获得{e}鹰草".format(e=str(e), at=at(UID))

            if 95 <= Rand_result <= 100:
                if int(data.getmoney(UID)) <= 650:
                    data.changemoney(UID, 300)
                    await speak(standard(300))
                else:
                    data.changemoney(UID, 300)
                    await speak(standard(150))
            elif 80 < Rand_result < 95:
                data.changemoney(UID, 100)
                await speak(standard(100))
            elif 55 < Rand_result < 80:
                d5_7 = random.randint(5, 7)
                data.changemoney(UID, d5_7 * 10)
                await speak(standard(d5_7 * 10))
            else:
                # 做个人吧，这尼玛赔率直接过一半啊啊啊啊啊
                d0_4 = random.randint(0, 4)
                data.changemoney(UID, d0_4 * 10)
                await speak(standard(d0_4 * 10))
        elif '.大抽奖' == event.message[0:4]:
            await speak("鹰草少于50" + at(UID))

        if '转账' in event.message[0:2] and GID not in BanGroup:
            uid, moey = GiveMoney(event)
            if int(data.getmoney(UID)) >= moey >= 0 or UID == 1728026105:
                data.changemoney(UID, -moey)
                data.changemoney(uid, moey)
                await speak("转入[CQ:at,qq={uid}]{cmy}鹰草".format(uid=uid, cmy=moey))
            else:
                await speak("转账数额小于0或当前钱小于{qmy}".format(qmy=moey))

            # 查看商品列表
            if '.商品列表' in event.message[0:5] and GID not in BanGroup:
                MBFK = money.shop()
                await speak(MBFK.get_menu())

        if '.占卜' in event.message[0:3]:
            s = random.randint(1, 100)
            if 25 < s < 75:
                await speak("不能")
            else:
                await speak("能")
        for h in text.danger.e():
            if h in Message:
                await bot.set_group_ban(group_id=GID, user_id=UID, duration=60)
                print(True)

                # await speak("c")

                await bot.delete_msg(message_id=event.message_id)
                await bot.send_private_msg(user_id=UID, message="违反关键词:{m},请注意言行".format(m=h))

        if '查看鹰草' in event.message[0:4] and event.group_id != 917328338:
            if int(data.getmoney(UID)) >= 2:
                h = CheckQQ(event.message)[0]
                s = data.getmoney(h)
                data.changemoney(UID, -2)
                await speak('[CQ:at,qq={uid}]拥有{s}鹰草'.format(uid=h, s=s))
            else:
                await speak('余额不足')
        if '特大抽奖' == event.message[0:4] and int(data.getmoney(UID)) >= 500 and GID not in BanGroup:
            s = random.randint(0, 100)
            data.changemoney(UID, -500)

            def standard(e):
                return "{at}花费500鹰草获得{e}鹰草".format(e=str(e), at=at(UID))

            if s <= 100 and s >= 95 and int(data.getmoney(UID)) <= 650:
                data.changemoney(UID, 3000)
                await speak(speak(standard(3000)))
            elif s < 90 and s > 70:
                data.changemoney(UID, 1000)
                await speak(standard(1000))
            elif s < 70 and s > 50:
                s = random.randint(5, 7)
                data.changemoney(UID, s * 100)
                await speak(standard(s * 100))
            else:
                s = random.randint(1, 4)
                data.changemoney(UID, s * 100)
                await speak(standard(s * 100))
        elif '特大抽奖' == event.message[0:4] and not int(data.getmoney(UID)) >= 500:
            await speak("鹰草少于500" + '[CQ:at,qq=' + str(UID) + ']')

        if '购买' in event.message[0:2] and event.group_id != 917328338:
            f = money.shop()
            try:
                num = CheckM(event.message)[0]
            except:
                num = "1"
            sting = event.message.replace('购买', '').replace(' ', '').replace(num, '')

            hawa = dict(money.ShopList)[sting] * int(num)
            if int(data.getmoney(UID)) >= hawa:
                data.changemoney(UID, -hawa)
                data.setitem(sting, UID, int(num))
                await speak("已购买,收您{money}鹰草".format(money=hawa))
            else:
                await speak("鹰草不够需要{money}鹰草".format(money=hawa))

        if '物品栏' in event.message[0:3] and event.group_id != 917328338:
            f = money.shop()
            await speak("[CQ:at,qq={uid}]\n".format(uid=UID) + f.GetMyItem(UID) + "*")

        if '撤回索' in event.message[0:3] and UID == 1728026105:
            s = event.message_id
            while True:
                await bot.delete_msg(message_id=s)
                s = s - 1
                if s <= 0:
                    break

    #if '开' == Message:
        se3r = 1
    #if '关' == Message:
        se3r = 0
if __name__ == '__main__':
    bot.run(host='127.0.0.1', port=8081)
