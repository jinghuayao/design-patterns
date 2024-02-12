#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/12/1


# 适配器模式：
#
#     内容： 将一个类的接口转换成客户希望的另一个接口。适配器模式使得原来由于接口不兼容
#           而不能一起工作的那些类可以一起工作。
#
#     两种实现方式：
#         类适配器：使用多继承
#         对象适配器：使用组合
#
#
#     注：复用其他类的代码有两种常见方式：（多）继承，组合

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d元." % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." % money)



class BankPay:
    def cost(self, money):
        print("银联支付%d元." % money)


class ApplePay:
    def cost(self, money):
        print("苹果支付%d元." % money)


# # 类适配器
# class NewBankPay(Payment, BankPay):
#     def pay(self, money):
#         self.cost(money)


# 对象适配器
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p = PaymentAdapter(BankPay())
p.pay(100)


# 组合

# class A:
#     pass
#
# class B:
#     def __init__(self):
#         self.a = A()
