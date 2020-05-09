#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
@file: inherit_set_kw.py
@time: 2020/05/08
@author: huameicc

1. 传参时**kw解析得到一系列 keyword-arguments
2. 进入方法后又被包装为一个新的 dic, 对这个dic的操作不会反应到上一级方法！！！！
"""


class A:
    def __init__(self, **kw):
        super().__init__(**kw)
        kw['a'] = 2
        print('A', id(kw), kw)

class B:
    def __init__(self, **kw):
        kw['b'] = 5
        print('B', id(kw), kw)

class Sub(A, B):
    def __init__(self, **kw):
        print(id(kw), kw)
        super().__init__(**kw)
        print(id(kw), kw)


class A1:
    def __init__(self, kw):
        super().__init__(kw)
        kw['a'] = 2
        print('A1', id(kw), kw)

class B1:
    def __init__(self, kw):
        kw['b'] = 5
        print('B1', id(kw), kw)

class Sub1(A1, B1):
    def __init__(self, kw):
        print(id(kw), kw)
        super().__init__(kw)
        print(id(kw), kw)


if __name__ == '__main__':
    s = Sub(k=99)
    print()
    s = Sub1(dict(k=99))

