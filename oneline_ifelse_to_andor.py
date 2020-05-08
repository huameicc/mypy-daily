#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
oneline_ifelse_to_andor.py
oneline if-else can be replaced by and/or
1. a if a else b  ->  a or b
2. f if a else g  -> a and f or g
"""

def f():
    return 'f()'

def g():
    return 'g()'


if __name__ == '__main__':
    print('f if a else g  -> a and f or g')
    for a in (1, 0):
        print(f'a={a}, {a and f() or g()}')
