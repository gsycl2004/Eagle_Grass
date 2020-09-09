from aiocqhttp import CQHttp, Event
import random
import asyncio
import time
import re
from module.translator import *

import text.danger
import module.money as money

api_root = "http://192.168.1.45:5700/"
bot = CQHttp(api_root=api_root)


async def main():
    s = await bot.get_group_member_list(group_id=917328338)

    f = [(h['card'],h['user_id']) for h in s if h['card'] != '' and h['card'] != '我爱鹰目sama' ]
    s = [e['card'] for e in s]

    hh = list(set(s))
    hh.remove('')
    print(hh)
    for eee in hh:
       lj =  local(eee)
       print(f"{eee}翻译为:{lj}")

    #for a1,a2 in f:
    #    se = local(a1)
    #    print(f"{a1}的结果为：{se}")





asyncio.run(main())
