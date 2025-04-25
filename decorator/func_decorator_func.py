print('%%%%%%%%%%%%%%%%%%%%%%%% 函数装饰器 - 装饰函数 %%%%%%%%%%%%%%%%%%%%%%%%%')
print('------------------ 装饰器（无参） --------------------------')
def hello1(func):
    test_var='hello'
    def just_test(*args, **kwargs):
        nonlocal test_var
        print("first",test_var)
        test_var=args[0]
        print('just_test - before')
        result = func(*args, **kwargs)
        print('just_test - after')
        print("in enclosure", test_var)
        return result
    print("out",test_var)
    return just_test


@hello1
def get_name(name, age):
    print(name, 'is', age, 'years old.')
    return name, age


# just_test - before
# Annie is 11 years old.
# just_test - after

# @hello1
# def show_something():
#     print('this is just show something')


# just_test - before
# this is just show something
# just_test - after


res = get_name("Annie", 11)
print('this is res', res)
get_name("BOB", 12)
# show_something()

import time
from random import randint


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start} seconds")
        return result

    return wrapper


@timer
def do_something(start, end):
    print('do_something - before')
    time.sleep(randint(start, end))
    print('do_something - after')


@timer
def do_something_1(start, end):
    print('do_something - before')
    time.sleep(randint(start, end))
    print('do_something - after')


do_something(2, 4)
do_something_1(1, 2)

# asd=timer(do_something)
# asd(1,3)


print('-------------------多层语法糖--------------------------')


def outter1(func1):
    print('加载了outter1, invoked func1 is', func1.__name__)

    def wrapper1(*args, **kwargs):
        print('start -- 执行了wrapper1, current func1 is', func1.__name__)
        res1 = func1(*args, **kwargs)
        print('end -- 执行了wrapper1, current func1 is', func1.__name__)
        return res1

    return wrapper1


def outter2(func2):
    print('加载了outter2, invoked func2 is', func2.__name__)

    def wrapper2(*args, **kwargs):
        print('start -- 执行了wrapper2, current func2 is', func2.__name__)
        res2 = func2(*args, **kwargs)
        print('end -- 执行了wrapper2, current func2 is', func2.__name__)
        return res2

    return wrapper2


def outter3(func3):
    print('加载了outter3, invoked func3 is', func3.__name__)

    def wrapper3(*args, **kwargs):
        print('start -- 执行了wrapper3, current func3 is', func3.__name__)
        res3 = func3(*args, **kwargs)
        print('end -- 执行了wrapper3, current func3 is', func3.__name__)
        return res3

    return wrapper3


@outter1  # index（outter1的内层函数名，一般最后一层我们使用跟功能函数同名的函数名 index） = outter1(wrapper2) ---------------wrapper1
@outter2  # wrapper2（outter2的内层函数名） = outter2(wrapper3)
@outter3  # wrapper3（outter3的内层函数名） =  outter3（index）
def index():
    print('from index')


index()  # 只要不调用被装饰的函数就不会执行装饰器内层函数

# 加载了outter3, invoked func3 is index
# 加载了outter2, invoked func2 is wrapper3
# 加载了outter1, invoked func1 is wrapper2
# 执行了wrapper1, current func1 is wrapper2
# 执行了wrapper2, current func2 is wrapper3
# 执行了wrapper3, current func3 is index
# from index


print('----------------------双层语法糖-----------------------------')
import time


def login_auth(func):
    def auth(*args, **kwargs):
        # username = input('username:').strip()
        # password = input('password:').strip()
        username = 'kevin'
        password = '123'
        if username == 'kevin' and password == '123':
            print('登录成功')
            time.sleep(2)
            res = func(*args, **kwargs)
            return res

        else:
            print('用户名密码错误')

    return auth


def all_time(func1):
    def time1(*args, **kwargs):
        start_time = time.time()
        res = func1(*args, **kwargs)
        stop_time = time.time()
        print('功能执行了%s秒' % (stop_time - start_time))
        return res

    return time1


@all_time  # 2. receive auth as its parameter, run nested function 'time1', the func1 is 'auth' in 'timer1', the func is 'index' in 'auth'
@login_auth  # 1. first run the closest decorator, the passed parameter to login_auth is index,  returned response function object auth is passed to all_time
def index():
    print('执行完成')


index()  # 最后一层就是 auth（）

# username:kevin
# password:123
# 登录成功
# 执行完成
# 功能执行了11.912482738494873秒

print('------------------ 装饰器（有参） --------------------------')


def repeat(is_re, count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            re_count = count if is_re else 1
            for i in range(re_count):
                print('****** NUMBER: %d ******' % (i+1))
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(True, 4)
def add(a, b):
    print('answer is', a + b)
    print('a is {}, b is {}, sum is {}'.format(a, b, a + b))


add(1, 2)

