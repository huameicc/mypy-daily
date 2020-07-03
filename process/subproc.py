#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
@file: subproc.py
@time: 2020/07/03
@author: huameicc

# 设置了没用
WINDOWS CMD ENCODE:
chcp [code]
936 : gbk, default
65001: utf-8

Pycharm 执行CMD, 中文输出会变乱码
�ð�

使用命令行直接执行不会出现乱码 // python ./subproc.py
"好吧"

"""




import subprocess, sys
import os

# cmd = ['cmd', '/c', 'chcp']
cmd = ['cmd', '/k', 'date /t', '&', 'chcp']


os.system('cmd /k echo "好吧"')
# subprocess.Popen(cmd, stdin=sys.stdin, stdout=sys.stdout,stderr=sys.stderr)
