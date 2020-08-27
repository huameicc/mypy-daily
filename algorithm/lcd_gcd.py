#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@file:lcd_gcd.py
@time:2020/08/27
@author:Jason

greatest common divisor
lowest common denominator
"""


def _gcd(a, b):
    while 1:
        m = a % b
        if m:
            a, b = b, m
        else:
            return b


# greatest common divisor
def gcd(a, *nums):
    for b in nums:
        a = _gcd(a, b)
    return a


# lowest common denominator
def lcd(a, *nums):
    __gcd = gcd(a, *nums)
    for b in nums:
        a = a * b / __gcd
    return int(a)


if __name__ == '__main__':
    print(gcd(4, 6))
    print(gcd(4, 6, 10))
    print(lcd(4, 10))
    print(lcd(4, 6, 10))
