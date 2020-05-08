import asyncio


async def fun(n):
    print('fun', n)
    if n == 0:
        print('end fun', n)
        raise ValueError('n<1')
        # return ValueError('N<1')
    await asyncio.sleep(n)
    if n == 3:
        print('end fun', n)
        raise ValueError('N>=3')
    print('end fun', n)
    await asyncio.sleep(0.001)
    return n


async def main():
    # t0 = asyncio.create_task(fun(0))
    t1 = asyncio.create_task(fun(2))
    t2 = asyncio.create_task(fun(3))
    try:
        genco = asyncio.wait({t1, t2, fun(3), fun(3),fun(4)}, return_when=asyncio.FIRST_EXCEPTION)
        d, p = await genco
        print(*d, '', *p, sep='\n')
        # for _d in d:
        #     print(_d.result())
    except:
        print('gggggg')
    # print(await asyncio.wait(p))


lp = asyncio.get_event_loop()
lp.run_until_complete(main())       # blocked os-thread
# lp.close()
print('hello')