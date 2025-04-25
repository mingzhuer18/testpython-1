print("----------------------- *** use __new__ to create singleton *** --------------------------------------")
class Singleton1:
    __instance = None
    print("class level")
    def __init__(self):
        print("__init__")

    def __new__(cls, *args, **kwargs):
        print("__new__")
        print("before new", cls.__instance)
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        print("after new", cls.__instance)
        return cls.__instance

sing11 = Singleton1()
print(id(sing11))
print("----------------------")
sing12 = Singleton1()
print(id(sing12))

print("----------------------- use class decorator to create singleton --------------------------------------")
"""
when a class which is decorated is called when create the instance, __call__ in decorator class is invoked 
***** if there is a func in decorated class, don't know how to handle ***** 
"""

class WrapperClass:
    _instance = None
    _temp='33'
    # _passed_class=None
    print("define _instance")
    def __init__(self, *args, **kwargs):
        print("decorator __init__ (not init of decorated class)")



    def __call__(self, *args, **kwargs):
        print("__call__")
        print(self._temp)
        print("before call", self._instance)
        if not self._instance:
            self._instance = super().__new__(WrapperClass)
        print("after call", self._instance)
        self._temp='44'
        return self._instance

    # def func(self, *args, **kwargs):
    #     print("start func in wrapper")
    #     self._passed_class().func()
    #     print("finish func in wrapper")




@WrapperClass
class Singleton2:
    def __init__(self, *args, **kwargs):
        print("__init__ in sington2")
        pass

    # def func(self):
    #     print("func in sington2")

    def __call__(self, *args, **kwargs):
        print("__call__ in singleton2")


ss = Singleton2()
print(id(ss))
# ss.func()
dd = Singleton2()
print(id(dd))


print("----------------------- *** use function decorator to create singleton *** --------------------------------------")
"""
 below 3 type of decorator can be used to create singleton class 
"""
# def decorator_func(cls):
#     print("before wrapper")
#     instance= {}   # instance 的生命周期由闭包决定，与装饰后的类绑定。只有装饰不同的类时，才会生成新的 instance，多次调用同一个装饰类，instance的值会一直传递
#     def wrapper(*args, **kwargs):
#         print("decorator cls is", cls.__name__)
#         print("before invoke", instance.get(cls))
#         if cls not in instance:
#             instance[cls] = cls(*args, **kwargs)
#         print("after invoke", instance[cls])
#         return instance[cls]
#     print("after wrapper")
#     return wrapper

def decorator_func(cls):
    print("before wrapper")
    instance= None
    def wrapper(*args, **kwargs):
        nonlocal instance   ## instance is immutable, need to define again in internal func with nonlocal
        print("decorator cls is", cls.__name__)
        if not instance:
            instance= cls(*args, **kwargs)
        print("after invoke", instance)
        return instance
    print("after wrapper")
    return wrapper

# def decorator_func(cls):
#     def wrapper(*args, **kwargs):
#         if not cls._instance:
#             cls._instance = cls(*args, **kwargs)
#         return cls._instance
#     return wrapper


@decorator_func
class Singleton3:
    _instance = None
    def __init__(self, *args, **kwargs):
        pass

    def func(self, *args, **kwargs):
        print("func called in Singleton3")


aa = Singleton3()
print(id(aa))
aa.func()
bb = Singleton3()
print(id(bb))
bb.func()

@decorator_func
class Singleton33:
    pass

bb=Singleton33()
print(id(bb))

print("----------------------- *** 另一种方法 用装饰器use function decorator to create singleton *** --------------------------------------")
def outer(cls):
    def inner(*args, **kwargs):
        if not hasattr(cls, 'instance'):
            instance = cls(*args, **kwargs)
            setattr(cls, 'instance', instance)
        return cls.instance

    return inner
@outer
class AAA:
    def __init__(self, a):
        self.a = a

a1=AAA(1)
print(id(a1))
print(a1.a)

a2=AAA(2)
print(id(a2))
print(a2.a)


print("----------------------- use python module to create singleton --------------------------------------")
class Singleton4:
    def __init__(self, *args, **kwargs):
        pass

singleton = Singleton4()
print(id(singleton))

print("----------------------- use metaclass to create singleton --------------------------------------")

class MyMetaclass(type):
    def __init__(cls, name, bases, attrs):
        super(MyMetaclass, cls).__init__(name, bases, attrs)
        cls.__instance=None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(MyMetaclass, cls).__call__(*args, **kwargs)  # 这一步会去调用class的new和init方法

        print("__call__", id(cls.__instance))
        return cls.__instance

class Singleton5(metaclass=MyMetaclass):
    def __init__(self):
        super(Singleton5, self).__init__()

    def __new__(cls, *args, **kwargs):
        inst = super().__new__(cls)
        print("__new__", id(inst))
        return inst

ss5=Singleton5()
print(id(ss5))
ss6=Singleton5()
print(id(ss6))










