"""
搜索从父类所继承属性的操作是深度优先、从左至右, 有重复取末次匹配到的class
"""

# multiple parent class， 用super()调用父类初始化函数， super会自动根据mro查找父类
# all 'self' in 4 classes are D的实例
# 按照 mro 顺序，先找到哪个类的方法就用那个方法， 不继续往下找了
class A:
    def __init__(self):
        print("A : __init__")
        # self.x="aaa"

    def method(self):
        print("A : method")

class B(A):
    def __init__(self):
        print("B : __init__")
        self.x = "bbb"
        super().__init__()

    def method(self):
        print("B : method")

# ?????????????? 为什么用下面的B 就不能访问到C和A的init了？
# class B:
#     def __init__(self):
#         print("B : __init__")
#         self.x = "bbb"
#
#     def method(self):
#         print("B : method")


class C(A):
    def __init__(self):
        print("C : __init__")
        super().__init__()

    def method(self):
        print("C : method")

class D(B,C):
    def __init__(self):
        print("D : __init__")
        super().__init__()

    def method(self):
        print("D : method")

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
dd = D()
print(dd.x)
dd.method()




class E:
    def __init__(self):
        print("E : __init__")

class F:
    def __init__(self):
        print("F : __init__")

class G(B,C,E,F):
    def __init__(self):
        print("G : __init__")
        super().__init__()

gg = G()
print(G.__mro__)
# (<class '__main__.G'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>)


