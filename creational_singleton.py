#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/12/1

# 单例模式：
#
#     内容：保证一个类只有一个实例，并提供一个访问它的全局访问点。
#     角色：单例(singleton)
#     优点：
#         --- 对唯一实例的受控访问
#         --- 单例相当于全局变量，但防止了命名空间被污染


# 创建型模式小结：
#
# - 抽象工厂模式和建造者模式相比于简单工厂模式和工厂方法模式而言更灵活也更复杂
# - 通常情况下，设计以简单工厂模式或工厂方法模式开始。当你发现设计需要更大的灵活性时，
#   则向更复杂的设计模式演化。



from abc import abstractmethod, ABCMeta

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


a = MyClass(10)
b = MyClass(20)

print(a.a)
print(b.a)
print(id(a), id(b))
