#! usr/bin/env python3
# -*- coding: utf-8 -*-

"""
aiomysql_bug_in_ResultProxy.py
aiomysql的官方例子在python 3.7中的async for问题，例子会报错

aiomysql    0.0.20
源码：
ResultProxy
async __aiter__(..)
写法是 < 3.5.2 版本的， >= 3.5.2之后 __aiter__ 不用加 async
python3.7之前仍可以写async __aiter__
python3.7之后不可以加async，async __aiter__只能用来定义异步生成器方法（配合yield）

手动修改ResultProxy源码后可以对其对象使用async for:
    rs = await conn.execute()
    async for _ in rs

# table
USE test;
CREATE TABLE `tbl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `val` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

更多内容参考：
关于async for 和 __aiter__、__anext__
https://gist.github.com/huameicc/d48a1e8c4c57ab0c66d309fa16401254
"""

import asyncio
import sqlalchemy as sa

from aiomysql.sa import create_engine


metadata = sa.MetaData()

tbl = sa.Table('tbl', metadata,
               sa.Column('id', sa.Integer, primary_key=True),
               sa.Column('val', sa.String(255)))


async def go(loop):
    engine = await create_engine(user='root', db='test',
                                 host='127.0.0.1', password='admin123', loop=loop)
    async with engine.acquire() as conn:
        # SAConnection本身没有commit，如果要提交更改到数据库，必须通过cursor实现，或者开始一个事务。
        # trans = await conn.begin()
        await conn.execute(tbl.insert().values(val='abc'))      # await得到ResultProxy（内部cursor的代理）
        await conn.execute(tbl.insert().values(val='xyz'))

        # 官方用例, 无法使用
        # TypeError: 'async for' received an object from __aiter__ that does not implement __anext__: coroutine
        # async for row in  conn.execute(tbl.select()):
        #     print(row.id, row.val)

        # ---------- 非原例代码，修改源码后测试 start --------------
        # ResultProxy写法是 < 3.5.2 版本， >= 3.5.2之后 __aiter__ 可以不加 async, >=3.7之后必须不加
        async for row in await conn.execute(tbl.select()):
            print(row.id, row.val)

        res = await conn.execute(tbl.select())
        print(type(res))
        print(await res.fetchall())
        # ---------- 非原例代码，修改源码后测试 end --------------
        # await trans.commit()
    engine.close()
    await engine.wait_closed()

import sys
print(sys.prefix)
loop = asyncio.get_event_loop()
loop.run_until_complete(go(loop))
