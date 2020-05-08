#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
@file: inspecttest.py
@time: 2020/04/29
@author: huameicc
"""

import inspect

def f(a, b=2, *c, d, e=5, **f):
    pass


sig = inspect.signature(f)
print(sig)
print(type(sig))
params = sig.parameters
print(params)
print(type(params))
for name, para in params.items():
    print(name, para)
    print(type(name), type(para))