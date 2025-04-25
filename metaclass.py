# 元类是类的类，就像类是对象的模板一样，元类是类的模板。在 Python 中，一切皆对象，类也是对象。当我们定义一个类时，Python 会在后台使用元类来创建这个类。默认情况下，Python 使用内置的type元类来创建类
print("------------ meta type: type -------------")


class A: pass



print(A)
print(type(A))
print("By default the metaclass is", type(A))

print("------------ meta type: sub type -------------")


class MyType(type):
    def __init__(cls, name, bases, attrs):
        # super().__init__(name,bases,attrs)
        super().__init__(name, bases, attrs)
        print(cls)
        print(bases)

    def __new__(cls, name, bases, attrs):
        print("sub meta type: __new__")
        print("the class {} has attributes".format(cls), attrs)
        if name[0].isupper():
            return super().__new__(cls, name, bases, attrs)
        else:
            raise TypeError("the class name {} is invalid, should start with capital letter".format("'" + name + "'"))

    def __call__(cls, *args, **kwargs):
        super().__call__(*args, **kwargs)


class B(metaclass=MyType): pass


print(B)
print("Explicitly define metaclass 'MyType', the meta class is not type, it's changed to ", type(B))
print(
    "-------------------- create a class and the class name donot start with capital, it shows errors -------------------")


# class hello(metaclass=MyType): pass  #this code show error
class Hello(metaclass=MyType):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def sayHello(self):
        print("Hello, my name is {} and my age is {}".format(self.name, self.age))


hello = Hello('Ann', 34)
