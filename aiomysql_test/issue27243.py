#! usr/bin/env python3
# -*- coding: utf-8 -*-

"""
关于async for 和 __aiter__、__anext__

old __aiter__ protocol, reutrn awaitable.
In 3.5.2 __aiter__ protocol was updated to return asynchronous iterators directly.
In CPython 3.7, the old __aiter__ protocol will no longer be supported: a RuntimeError will be raised
if __aiter__ returns anything but an asynchronous iterator.
不过没搞懂，为什么3.7以后不再支持old __aiter__ protocol, 这造成了以前代码的兼容问题
OK,考虑了很久，大概是为了协议的唯一性之类，底层协议需要明确，避免以后带来更多复杂性。
而且之前的PEP 491是provisional, 所以可以进行更改，目前状态已经是Final.

总之现在3.7以后
__aiter__必须返回一个实现了async __anext__方法的对象。如不符合，尝试使用async for就会报错。
<1. async __aiter__ 本身就得是一个异步生成器方法 （必须有至少一个yield），调用不会返回一个coroutine.(异步生成器
是有async __anext__方法的。
 因此: async def __aiter__ 中就必须得用yield. 针对这个方式的定义：
 <a>使用了yield，语法上不允许再return一个值，None也不行.（无值的return作为结束是可以的，任何方法本身就有默认的return）
 <b>错误写法。不过从语法上来讲，没有yield时允许直接return一个值。调用返回一个coroutine.【使用 async for会报错】
<2. __aiter__直接return一个实现了async __anext__方法的对象

reference:
https://bugs.python.org/issue27243
https://www.python.org/dev/peps/pep-0492/#api-design-and-implementation-revisions
"""

import asyncio


# 异步生成器function
async def foo():
    await asyncio.sleep(0.5)
    yield 1
    await asyncio.sleep(0.5)
    yield 2


# 异步生成器class，在issue27243解决后可以实现了
# async __aiter__应可以看作是一个异步生成器method
class Foo:
    async def __aiter__(self):
        await asyncio.sleep(0.5)
        yield 1
        await asyncio.sleep(0.5)
        yield 2


# 3.7以后的写法2
class Goo:
    def __init__(self, n=3):
        self.n = n

    # if you add async, TypeError raised in async for.
    def __aiter__(self):
        return self

    async def __anext__(self):
        await asyncio.sleep(1)
        if self.n:
            _n = self.n
            self.n -= 1
        else:
            raise StopAsyncIteration
        return _n


# 3.7以后的错误写法
class Hoo:
    async def __aiter__(self):
        return


async def main(fcls):
    f = fcls()
    print(type(f), type(f).__bases__)
    # if fcls in (Goo, Foo):
    it = f.__aiter__()
    print('f.__aiter__() returned:', it, type(it))
    if asyncio.iscoroutine(it):
        await it
    try:
        async for el in f:
            print(el)
    except TypeError as e:
        # 由于async for在内部调用了Hoo.__aiter__，返回一个coroutine，所以会出现一个RuntimeWaring: ...never awaited
        print('Trpe Error:', e)
    print()


asyncio.run(main(foo))
asyncio.run(main(Foo))
asyncio.run(main(Goo))
asyncio.run(main(Hoo))
