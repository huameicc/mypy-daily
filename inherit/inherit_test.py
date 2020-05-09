"""
---以下说法有误, 实际上需要A\B有super(), 具体有关 mro, 较新的例子里有说明 ----
单继承写法：
    super().__init__(a)
    super().pr()

多继承写法 self不可省略
    A.__init__(self, a)
    A.pr(self)
------------

"""


class A:
    def __init__(self, a):
        print(type(self))
        self.a = a

    def pr(self):
        print('A', self.__dict__.values())

    def __pa(self):
        print('APA', self.a)

    @classmethod
    def from_db(cls):
        return cls(1, 2)


class B:
    def __init__(self, b):
        print(type(self))
        self.b = b

    def pr(self):
        print('B', self.__dict__.values())


class Sub(A, B):
    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b)

    def pr(self):
        B.pr(self)
        A.pr(self)
        print('C', self.__dict__.values())


class A1(A):
    def __init__(self, a, a1):
        super().__init__(a)
        self.a1 = a1

    @classmethod
    def from_dbs(cls):
        return super().from_db()


if __name__ == '__main__':
    ia = A(21)
    ia1 = A1(22, 23)
    print()

    ins = Sub(19, 32)
    ins.pr()
    # ins._A__pa()
    # ins.__pa()  # __内部属性、方法名称会改变，外部不能直接访问

    print('\n子类继承父类类方法，从子类方法进入父类时cls不会被改写[仍是A1]')
    print(A1.from_dbs())
    print(A1(2, 0))

