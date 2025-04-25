class A():
    # 类属性
    sentence = 'this is a learning testing'

    # 普通方法（实例方法）
    def normalMethod(self):
        print(self.sentence)

    # 类方法
    @classmethod
    def classMethod(cls, sentence):
        print(sentence)
        print(cls.sentence)


    # 静态方法
    @staticmethod
    def staticMethod(sentence):

        print(A.sentence)
        A.classMethod("heihie")
        print(sentence)

a=A()
b=A()
print("a --",a.sentence)
print("b --",b.sentence)
print("A --",A.sentence)
print("----------below to update by A-----------")
A.sentence = 'this is a learning testing - A update'
print("a --",a.sentence)
print("b --",b.sentence)
print("A --",A.sentence)
print("update by A will cause a b A .sentence changed")
print("----------below to update by a-----------")
a.sentence = 'this is a learning testing - a update'
print("a --",a.sentence)
print("b --",b.sentence)
print("A --",A.sentence)
a.normalMethod()
b.normalMethod()
print("----------below to update by a again-----------")
a.sentence = 'this is a learning testing - a update again'
print("a --",a.sentence)
print("b --",b.sentence)
print("A --",A.sentence)
print("----------below to update by b-----------")
b.sentence = 'this is a learning testing - b update'
print("a --",a.sentence)
print("b --",b.sentence)
print("A --",A.sentence)
a.normalMethod()
b.normalMethod()

print("----------below to update by A again -----------")
A.sentence = 'this is a learning testing - A update again'
print("a --",a.sentence)
print("b --",b.sentence)
print("A --",A.sentence)
a.normalMethod()
b.normalMethod()
c=A()
print("c --",c.sentence)

print("-------------- class method ------------")
A.classMethod("hhhh")
a.classMethod("mmmmm")

print("-------------- static method ------------")
A.staticMethod("hhhhhhhhhhhh")
a.staticMethod("mmmmmmmmmmmmmmm")


print("---------------------------- extend class --------------------------")
class XX:
    def __init__(self, h, k):
        self.h = h
        self.k = k
        self._m='mmm'
        self.__n='nnn'

    def method(self):
        print("get public attribute k", self.k )
        print("get public attribute h", self.h)
        print("get protected attribute", self._m)
        print("get private attribute", self.__n)

    def __private_method(self):
        print("**** this is private method, only can be called externally after naming mangling ****" )

class YY(XX):
    def __init__(self, h, k):
        super().__init__(h, k)
        self.b="bbbb"

    def sub_method(self):
        print("get public attribute k", self.k )
        print("get public attribute h", self.h)
        print("get protected attribute", self._m)
        print("get public attribute b", self.b)
        # in child class cannot get parent's private attribute
        #print("get private attribute", self.__n)
        print("Cannot get parent's private attribute self.__n")



print("-------------- diff type of attributes of class in instance method ------------")
x1=XX(33, 55)
x1.method()
# AttributeError: x1.__private_method()
x1._XX__private_method()

print("get public attribute h by instance", x1.h)
print("get protected attribute _m by instance", x1._m)
print("cannot get private attribute __n by instance")
print("get private attribute _XX__n by instance", x1._XX__n)

print("----------------------------- child class ----------------------------")
y1=YY(31, 51)
print("----- child class call parent's public method and attribute ----")
y1.method()
print("----- child class call parent's private method ----")
y1._XX__private_method()

print("----- child class call its own method and attribute, and parent's attribute ----")
y1.sub_method()



