#!usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: MBT102 - jibo
@file: metaclass_look.py
@time: 2020/04/24/26

Metaclass
1. 定义一个元类应继承自type或其子类，并按需实现__new__方法
2. 一个类的定义中，使用了metaclass参数，运行时就会调用对应元类的__new__方法来真正创建这个类
  【默认metaclass=type, 如果没有定义或者为type，会去找父类的metaclass】 具体如何有时间要去研究下元类的内部机制

mcs:  元类本身     <class '__main__.ListMetaclass'>
name: 定义的类名    MyList
bases: 基类元组     (<class 'list'>,)
attrs: 一个字典，包含要定义的类的__module__、__qualname__、方法、属性、...等信息
                    {'pr': <function MyList.pr at 0x0038E420>, '__module__': '__main__',
                    '__qualname__': 'MyList', 'ps': <staticmethod object at 0x003894B0>}

可见，元类的作用，可以用来为新类动态增加方法、属性、基类
# 甚至改变类名(不建议，仍是按照MyList来使用，不过有些地方可能会出现被改变后的类名)
   [MyList.__name__='GGG', MyList__qualname__='MyList']
"""

class SayMixin:
    def say(self):
        print('say')


class ListMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        print('\n----------------meta begin---------------')
        print(mcs, name, bases, attrs, sep='\n')
        # attrs.pop('pr')
        attrs['add'] = lambda self, value: self.append(value)
        # 试着把mcs改为type,一样有效
        print('----------------meta return---------------')
        # return type.__new__(mcs, 'GGG', (*bases, SayMixin), attrs)
        return super().__new__(mcs, 'GGG', (*bases, SayMixin), attrs)

class MyList(list, metaclass=ListMetaclass):
    """ MyList doc """
    good = 10

    def __init__(self):
        print('init begin')
        super().__init__()
        self.aaa = 12
        print('init over')

    def pr(self):
        print('pr')

    @classmethod
    def pc(cls):
        print('pc')

    @staticmethod
    def ps():
        print('ps')

    print('MyList')


print('\n1. test MyList')
li = MyList()
li.add(2)
print(li.aaa)
print(li)
li.pr()
#
print('\n2. 测试在元类增加基类')
print(MyList.__bases__)
li.say()
# 很遗憾，虽然可以调用，但dict里没有say
print('say' in MyList.__dict__)
print(MyList.__dict__)
#
print('\n3. 不要改变name')
print(MyList.__name__, MyList.__qualname__, type(li), sep=' -- ')


print("\n4. metaclass of B is type")

class B(MyList, metaclass=type):
    def pr(self):
        print('pr')

print(B.pr)
print(B().pr)
