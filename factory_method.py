#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/12/1

# 工厂方法模式
#
# - 内容：
#     定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类。
#
# - 角色：
#     - 抽象工厂角色(Creator)
#     - 具体工厂角色(Concrete Creator)
#     - 抽象产品角色(Product)
#     - 具体产品角色(Concrete Product)


from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print("花呗支付%d元." % money)
        else:
            print("支付宝余额支付%d元." % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." % money)


class BankPay(Payment):
    def pay(self, money):
        print("银行卡支付%d元." % money)


class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)


class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


# client

pf = HuabeiFactory()
p = pf.create_payment()
p.pay(100)
