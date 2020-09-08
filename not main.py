from aiocqhttp import CQHttp, Event
import random
import asyncio
import time
import re
from module.translator import *

import text.danger
import module.money as money

api_root = "http://127.0.0.1:5700/"
bot = CQHttp(api_root=api_root)


async def main():
    s = await bot.get_group_member_list(group_id=1043617974)
    f = await bot.get_group_member_list(group_id=1022645297)
    h = [h['user_id'] for h in s]
    l = [h['user_id'] for h in f]

    s = [eee for eee in h if eee in l]
    print(s)


asyncio.run(main())
