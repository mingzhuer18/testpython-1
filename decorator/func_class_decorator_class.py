

print('%%%%%%%%%%%%%%%%%%%%%%%% 函数装饰器 - 装饰类 %%%%%%%%%%%%%%%%%%%%%%%%%')
"""
装饰器传入参数为被装饰类名
装饰器内定义一个包装类，被装饰参数作为初始化方法的参数，被赋值给一个包装类变量，必须重写所有被装饰类内的方法
没有被重写的函数被调用时会报错 -- 使用__getattr__方法处理所有没有被重写的方法可以避免报错，只有被装饰类调用了不存在（没有被重写）的方法才会触发这个__getattr__()
"""
def decorate_function(cls, *a, **k):
    class WrapClass:
        def __init__(self, *a, **k):
            self.wrappedClassInst=cls(*a, **k)
            print("init's param is", a, k)

        def fun1(self,*a, **k):
            print("准备调用被装饰类的方法fun1")
            print("func1's param is", a, k)
            self.wrappedClassInst.fun1(*a, **k)
            print("调用被装饰类的方法fun1完成")

        def __getattr__(self, name):
            print("get attr is overwrited, only when the func is not exist in wrapclass, this func will be called")
            print("getattr's param is", name)
            resp = getattr(self.wrappedClassInst, name)
            print("resp is", resp)
            return resp

    return WrapClass

@decorate_function
class WrappedClass:
    def __init__(self ,*a, **k):
        print("我是被装饰类的构造方法")
        if a:print("构造方法存在位置参数：",a)
        if k:print("构造方法存在关键字参数：",k)
        print("被装饰类构造方法执行完毕")

    def fun1(self,*a, **k):
        print("我是被装饰类的fun1方法")
        if a:print("fun1存在位置参数：",a)
        if k:print("fun1存在关键字参数：",k)
        print("被装饰类fun1方法执行完毕")

    def fun2(self,*a, **k):
        print("我是被装饰类的fun2方法")


c1 = WrappedClass('testPara',a=1,b=2)
c1.fun1()
# 我是被装饰类的构造方法
# 构造方法存在位置参数： ('testPara',)
# 构造方法存在关键字参数： {'a': 1, 'b': 2}
# 被装饰类构造方法执行完毕
# init's param is ('testPara',) {'a': 1, 'b': 2}
# 准备调用被装饰类的方法fun1
# func1's param is () {}
# 我是被装饰类的fun1方法
# 被装饰类fun1方法执行完毕
# 调用被装饰类的方法fun1完成

c1.fun2()
# ------no over write -------
# Traceback (most recent call last):
#   File "C:\Users\ZMing-Zhu\PycharmProjects\testpython-1\class_decorator_function_class.py", line 42, in <module>
#     c1.fun2() # error
# AttributeError: 'WrapClass' object has no attribute 'fun2'
# ------no over write -------

# ------ over write -------
# get attr is overwritten, only when the func is not exist in wrapclass, this func will be called
# getattr's param is fun2
# resp is <bound method WrappedClass.fun2 of <__main__.WrappedClass object at 0x00000268644BB430>>
# 我是被装饰类的fun2方法
# ------ over write -------