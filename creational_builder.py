#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/12/1


# 建造者模式
#
# - 建造者模式与抽象工厂模式相似，也用来创建复杂对象。主要区别在于建造者模式着重于一步步
#   构造一个复杂的对象，而抽象工厂模式着重于多个系列的产品对象。
#
# - 优点
#     - 隐藏了一个产品的内容结构和装配过程
#     - 将构造代码与表示代码分开
#     - 可以对构造过程进行更精细的控制
    




from abc import ABCMeta, abstractmethod

class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s, %s, %s, %s" % (self.face, self.body, self.arm, self.leg)


class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


class SexyGirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "漂亮脸蛋"

    def build_body(self):
        self.player.body = "苗条"

    def build_arm(self):
        self.player.arm = "漂亮胳膊"

    def build_leg(self):
        self.player.leg = "大长腿"


class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "怪兽脸"

    def build_body(self):
        self.player.body = "怪兽身材"

    def build_arm(self):
        self.player.arm = "长毛的胳膊"

    def build_leg(self):
        self.player.leg = "长毛的腿"


class PlayerDirector: # 控制组装顺序
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# client

# builder = Monster()
builder = SexyGirlBuilder()
director = PlayerDirector()
p = director.build_player(builder)
print(p)
