# __new__
class AA:
    def __init__(self, name):
        print('this is AA')
        self.name = name


class Hello1:
    __namingdecoration='hello1attr'
    def __init__(self, name, age=30):
        self.name = name
        self.age = age
        print(type(self))
        print('__init__ func')

    def __new__(cls, *args, **kwargs):
        print('args is', args)
        inst = super().__new__(cls)
        print('__new__ func')
        return inst

class Hello2:
    def __init__(self, name, age=30):
        self.name = name
        self.age = age
        print("__init__ of", self.__class__.__name__)

    def __call__(self, *args, **kwargs):
        print('in __call__ args is', args)

    def __new__(cls, *args, **kwargs):
        inst = super().__new__(cls)
        print('in __new__ args is', args)
        return inst

class Hello3:
    def __init__(self):
        print("Hello3 init")

    def __new__(cls, *args, **kwargs):
        inst = Hello2('anni')
        return inst

if __name__ == '__main__':
    h1 = Hello1("hello1", 22)
    # hh = Hello1()
    print(h1.age)
    print(callable(h1))
    print(callable(Hello1))


    print('---------------------------------')
    h2=Hello2("hello2", 23)
    print(h2.name)
    # print(callable(h2))
    # print(callable(Hello2))
    h2('callable', city='shanghong')

    print("-------------if return other class instance in __new__, will call other class's __init__ -----------")
    h3=Hello3()
    h3()

    print(dir(Hello1))