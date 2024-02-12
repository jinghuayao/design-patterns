# coding: utf-8
# author: ztypl
# date:   2018/12/26


# 代理模式
#
# - 内容：
#     为其他对象提供一种代理以控制对这个对象的访问
#
# - 应用场景：
#     - 远程代理：为远程的对象提供代理
#     - 虚代理：根据需要创建很大的对象
#     - 保护代理：控制对原始对象的访问，用于对象有不同访问权限时
#
# - 角色：
#     - 抽象实体(Subject)
#     - 实体(RealSubject)
#     - 代理(Proxy)
#
# - 优点：
#     - 远程代理：可以隐藏对象位于远程地址空间的事实
#     - 虚代理： 可以进行优化，例如根据要求创建对象
#     - 保护代理： 允许在访问一个对象时有一些附加的内务处理

# 打印cwd, 这样保证后续文件读取路径正确
import os
print(f"Current working directorey:{os.getcwd()}")

from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, mode='r', encoding='utf-8')
        print("读取文件内容")
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding="utf-8")
        f.write(content)
        f.close()





class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()


    def set_content(self, content):
        if not subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)



class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError("无写入权限")



# subj = RealSubject("test.txt")
# subj.get_content()

# subj = VirtualProxy("test.txt")
# subj.get_content()

subj = ProtectedProxy("test.txt")
print(subj.get_content())
# subj.set_content("abc")
