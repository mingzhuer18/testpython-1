class A:
    var = 'haha'
    print(var)
    def __init__(self):
        self.x = 1
        print('__init__')

    def __new__(cls):
        print('__new__')
        return super().__new__(cls)


    def func(self):
        print('func')
        print(self.x)

aa=A()
print(aa.var)
print(aa.__class__)
print(aa.__module__)
print(aa.__doc__)
print(aa.__dict__)

# 动态给对象加上属性
aa.__dict__['y']=2
print(aa.__dict__)
print('------------')
print(A.__module__)
print(A.__name__)
print(A.__doc__)
print(A.__base__)
print(A.__dict__)
print('------------')
print(__name__)
print(__file__)

print("--------------------- get attribute -----------------------")
print(getattr(aa, "x", 10))
print(getattr(aa, "z", 10))
print(getattr(aa, "func"))
print("--------------------- set attribute -----------------------")
print(aa.__dict__)
aa.__setattr__('x', 15)
print(getattr(aa, "x"))
aa.__setattr__('another', 24)
print(getattr(aa, "another"))
print(aa.__dict__)
print(dir(aa))



