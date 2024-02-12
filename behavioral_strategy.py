# coding: utf-8
# author: ztypl
# date:   2018/12/27

# 策略模式
#
# - 内容
#     定义一系列的算法，把它们一个个封装起来，并且使它们可以互相替换。本模式使得
#     算法可以独立于使用它的客户而变化。
#
# - 角色
#     - 抽象策略(Strategy)
#     - 具体策略(ConcreteStrategies)
#     - 上下文(Context)
#
# - 优点
#     - 定义了一系列可重用的算法
#     - 消除了一些条件语句
#     - 可以提供相同行为的不同实现
#
# - 缺点
#     - 客户必须了解不同的策略



from abc import ABCMeta,abstractmethod

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    def execute(self, data):
        print("用较快的策略处理%s" % data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的策略处理%s" % data)


class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


# Client

data = "[...]"
s1 = FastStrategy()
s2 = SlowStrategy()
context = Context(s1, data)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()
