#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
@file: inherit_set_kw.py
@time: 2020/05/08
@author: huameicc


"""


class A:
    def __init__(self, **kw):
        print(type(self))
        kw['a'] = 2
        print(id(kw), kw)

class B:
    def __init__(self, **kw):
        print(type(self))
        kw['b'] = 5
        print(id(kw), kw)

class Sub(A, B):
    def __init__(self, **kw):
        print(id(kw), kw)
        super().__init__(**kw)
        print(id(kw), kw)



if __name__ == '__main__':
    s = Sub()

