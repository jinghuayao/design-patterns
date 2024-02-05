Design Patterns Demonstrated by Python
upstream setup





# 1. SOLID Principles

`SOLID` stands for:

- S: Single-Responsibility Principle (单一职责原则)
  
  一个类只处理一个任务

- O: Open-Closed Principle (开闭原则)
  
  对扩展开放，对修改封闭

- L: Liskov Substitution Princile (李氏替换原则)
  
  一个函数或者方法可以作用于父类Object, 则其应可以作用于子类Object.
  
  或者说一个地方可以pass父类Object, 则其应可以pass子类Object.

- I: Interface Segregation Principle (接口分离原则)
  
  使用多个专门的接口，而不是使用单一的总结口。即：客户端/高层代码不应依赖于那些它不需要的接口。

- D: Dependency Inversion Principle (依赖倒置原则)
  
  高层模块不应依赖底层模块，二者都应该依赖于其抽象；抽象不应该依赖于细节，细节应该依赖于抽象。即：要针对接口编程，而不是针对实现编程。
