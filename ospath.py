#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
@file: ospath.py
@time: 2020/04/30
@author: MBT102 - jibo

1. os.path.abspath会把路径的 / [Linux] 转换为 \ [Windows]
2. os.path.dirname不会进行 slash 到 backslash 的转换，但可以嵌套 abspath 来实现

"""

import os

print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))

print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'))
