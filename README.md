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



## 2. GoF Design Pattern Types

GoF Design Patterns are divided into three categories:

1. **Creational (创建型)**: The design patterns that deal with the creation of an object.
   
   This category includes below 5 types:
   - Singleton 单例模式
   
   - Factory 工厂方法模式
   
   - Abstract Factory 抽象工厂模式
   
   - Builder 创建者模式
   
   - Prototype 原型模式
2. **Structural (结构型)**: The design patterns in this category deals with the class structure such as Inheritance and Composition.
   
   This category includes below 7 types:
   - Adapter 适配器模式
   
   - Composite 复合模式/组合模式
   
   - Proxy 代理模式
   
   - Flyweight 享元模式
   
   - Facade 外观模式
   
   - Bridge 桥模式
   
   - Decorator 装饰模式
3. **Behavioral (行为型)**: This type of design patterns provide solution for the better interaction between objects, how to provide lose coupling, and flexibility to extend easily in future.
   
   This category includes below 11 types:
   - Template Method 模版模式
   
   - Mediator 中介模式
   
   - Chain of Responsibility 责任链模式
   
   - Observer 观察者模式
   
   - Strategy 策略模式
   
   - Command 命令模式
   
   - State 状态模式
   
   - Visitor 访问者模式
   
   - Interpreter 解释器模式
   
   - Memento 备忘录模式
   
   - Iterator 迭代器模式

### 3. GoF Design Pattern Summary



### 3.1 Creational Design Patterns

| Pattern Name            | Description                                                                                                                 |
|:----------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Singleton 单例模式          | The singleton pattern restricts the initialization of a class to ensure that only one instance of the class can be created. |
| Factory 工厂方法模式          | The factory pattern takes out the responsibility of instantiating a object from the class to a Factory class.               |
| Abstract Factory 抽象工厂模式 | Allows us to create a Factory for factory classes.                                                                          |
| Builder 创建者模式           | Creating an object step by step and a method to finally get the object instance.                                            |
| Prototype 原型模式          | Creating a new object instance from another similar instance and then modify according to our requirements.                 |



### 3.2 Structural Design Patterns

| Pattern Name      | Description                                                                                                                                     |
|:-----------------:| ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Adapter 适配器模式     | Provides an interface between two unrelated entities so that they can work together.                                                            |
| Composite 复合/组合模式 | Used when we have to implement a part-whole hierarchy. For example, a diagram made of other pieces such as circle, square, triangle, etc.       |
| Proxy 代理模式        | Provide a surrogate or placeholder for another object to control access to it.                                                                  |
| Flyweight 享元模式    | Caching and reusing object instances, used with immutable objects. For example, string pool.                                                    |
| Facade 外观模式       | Creating a wrapper interfaces on top of existing interfaces to help client applications.                                                        |
| Bridge 桥模式        | The bridge design pattern is used to decouple the interfaces from implementation and hiding the implementation details from the client program. |
| Decorator 装饰器模式   | The decorator design pattern is used to modify the functionality of an object at runtime.                                                       |



### 3.3 Behavioral Design Patterns



| Pattern Name                  | Description                                                                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Template Method 模版方法模式        | used to create a template method stub and defer some of the steps of implementation to the subclasses.                                           |
| Mediator 中介者模式                | used to provide a centralized communication medium between different objects in a system.                                                        |
| Chain of Responsibility 责任链模式 | used to achieve loose coupling in software design where a request from the client is passed to a chain of objects to process them.               |
| Observer 观察者模式                | useful when you are interested in the state of an object and want to get notified whenever there is any change.                                  |
| Strategy 策略模式                 | Strategy pattern is used when we have multiple algorithm for a specific task and client decides the actual implementation to be used at runtime. |
| Command 命令模式                  | Command Pattern is used to implement lose coupling in a request-response model.                                                                  |
| State 状态模式                    | State design pattern is used when an Object change it’s behavior based on it’s internal state.                                                   |
| Visitor 访问者模式                 | Visitor pattern is used when we have to perform an operation on a group of similar kind of Objects.                                              |
| Interpreter 解释器模式             | defines a grammatical representation for a language and provides an interpreter to deal with this grammar.                                       |
| Iterator 迭代器模式                | used to provide a standard way to traverse through a group of Objects.                                                                           |
| Memento 备忘录模式                 | The memento design pattern is used when we want to save the state of an object so that we can restore later on.                                  |
