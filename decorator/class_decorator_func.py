print('%%%%%%%%%%%%%%%%%%%%%%%% 类装饰器 %%%%%%%%%%%%%%%%%%%%%%%%%')
print('-------------------- 无参类装饰器 --------------------------')
print('func is passed to __init__')
class DecoratedClass:
    def __init__(self, func):
        self.func = func
        print('this is init from', self.__class__.__name__, "the func is", self.func.__name__)

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)
        print('this is call from', self.__class__.__name__, "the func is", self.func.__name__)



@DecoratedClass
def func_test():
    print('this is func_test')


@DecoratedClass
def func_test_1(a, b):
    print('this is func_test_1')
    print(a * b)

def func_test_2():
    print('this is func_test_2')


print(func_test)
# <__main__.DecoratedClass object at 0x000001D9AA50B250>
print(func_test_2)
# <function func_test at 0x000001D9AA507EE0>
func_test()
func_test_1(3,6)
func_test_2()

print('-------------------- 有参类装饰器 --------------------------')
print('func is passed to __call__')
print("decorator's parameters are passed to __init__")
class DecoratedClassWithParams:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        print('this is init from', self.__class__.__name__)
        print('param1 is', self.param1, 'param2 is', self.param2)


    def __call__(self, func):
        print('this is call from', self.__class__.__name__)
        print('func is', func.__name__)

        def wrapper(*args, **kwargs):
            print('execute', func.__name__)
            if self.param1 == 1 and self.param2 == 1:
                func(*args, **kwargs)
                print('execute finished', func.__name__)
            else:
                print("no need to execute", func.__name__)


        return wrapper

@DecoratedClassWithParams(1,2)
def func_test_2():
    print('this is func_test_2')

func_test_2()


def type_check(*arg_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, arg_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {arg} is not of type {expected_type}")
                return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def multiply(x, y):
    return x * y

print(multiply(2, 3))


class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)






