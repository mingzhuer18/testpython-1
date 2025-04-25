# This is a sample Python script.
# from copy_class import dict_temp
import random
import sys


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    pass
    # my_list = [1, 2, 3]
    # my_list.reverse()
    # print(my_list)

    print("for-else 语法 -- 如果不执行break， 则会执行到else")
    target = 12
    my_list = [1, 2, 3, 5, 7, 12, 65]
    for item in my_list:
        if item == target:
            print(f"find the number {target}")
            break
    else:
        print(f"cannot find the number {target}")

    # print(r'''hello,\n
    # world''')
    # print('''hello,\n
    # world''')
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # a = 3
    # b = a if a > 1 else 2
    # print("b is %d, a is %d" % (b, a))
    # print(a, b)
    #
    # name = "Alice"
    # age = 30
    # print("Name:", name, "Age:", age)
    # print(f"Name: {name}, Age: {age}")
    # print("name:{}, age:{}".format(name, age))
    # print("name is %s, age is %s" % (name, age))
    #
    # print(5 / 2)
    # print(5 // 2)
    #
    # aa = 'helloworld'
    # print(aa[0:4])
    # print(aa[1:4])
    # print(aa[4:-1])
    # print(aa[4:])
    # print(aa[0:-1])
    # print(aa[1:-2])
    # print(aa[1:-2] * 2)
    # print(aa[1:8:2])  # 第2个和第9个字母中间，每隔2个取一个字母，不能取第9个
    # print(aa[-1::-1])  # 反转整个字符串
    #
    # aa = ['abcd', 786, 2.23, 'runoob', 70.2]
    # print(aa[0:4])
    # print(aa[1:4])
    # print(aa[3:4])
    # print(aa[0:4:2])  # 第1个和第5个字母中间，每隔2个取一个字母，不能取第5个
    # print(aa[-1::-1])
    #
    # aa = True
    # print(aa)
    # print(type(aa))
    # print(int(aa))
    # print(1 + aa)
    #
    # # input_var = input("enter:")
    # # print(input_var)
    #
    # a = set('abracadabra')
    # b = set('alacazam')
    # print(a - b)  # a 和 b 的差集
    # print(b - a)
    # print(a | b)  # a 和 b 的并集
    #
    # print(a & b)  # a 和 b 的交集
    #
    # print(a ^ b)  # a 和 b 中不同时存在的元素
    #
    # ss = {3, 4, 6}
    # print(type(ss))
    # ss = {4, 3, 56, 343, 3}
    # print(ss)
    #
    # a = 'ABC'
    # b = a
    # a = 'XYZ'
    # print(a)
    # print(b)
    #
    # count = 0
    # for x in range(101):
    #     count += x
    # print(count)
    # d = {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Emoy': ['111', '222']}
    # if 'Bob1' in d:
    #     print('yes')
    # for x in d.items():
    #     print(x)
    #
    # print(test(3, 4))
    #
    # shallow_copied = d.copy()
    # # 修改嵌套对象
    # d['Emoy'][0] = '333'
    #
    # print("Original:", d)  # {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Emoy': ['333', '222']}
    # print("Shallow Copied:", shallow_copied)  # {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Emoy': ['333', '222']}
    #
    # xx = {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Emoy': ['111', '222']}
    # e = xx.copy()
    # xx['Bob'] = 50
    # print(xx)
    # print(e)
    # vv=xx.items()
    # for ii,kk in xx.items():
    #     print(ii,kk)
    # print(vv)
    #
    # e['Emoy'][0] = '550'
    # print(xx)
    # print(e)
    #
    # e['Annie'] = 45
    # print(xx)
    # print(e)
    #
    # print(findMinAndMax([4, 7, 1.9, 3.5, 6.5, 6, 7, 14, 2]))
    #
    # tt = (x * x for x in range(1, 11))
    # print(next(tt))
    # print(next(tt))
    # print(next(tt))
    #
    # print(list(tt))
    #
    # ll = [x * x for x in range(1, 11)]
    # print(ll)
    # print("is list iterable?")
    # print(isinstance(ll, Iterable))
    # print(isinstance(ll, Iterator))
    # i_ll = iter(ll)
    # print(isinstance(i_ll, Iterator))
    # while True:
    #     try:
    #         print(next(i_ll))
    #     except StopIteration:
    #         break
    #
    # ll1 = [x * x if x % 2 == 1 else x + 1 for x in range(1, 11)]
    # print(ll1)
    #
    # ll2 = [x.lower() for x in ['ADBDdd', 'ddfaA', 34, 4, '33Ad'] if isinstance(x, str)]
    # print(ll2)
    #
    # fb(13)
    #
    # print(random.randint(10, 15))

    # print('--------------------------')
    # gg = gen_fb(7)
    # print(type(gg))
    # print(next(gg))
    # print(next(gg))


def fb(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


def gen_fb(max):
    n, a, b = 0, 0, 1
    while n < max:
        print("before")
        yield b
        print("after")
        a, b = b, a + b
        n = n + 1


def test(x, n):
    total = 1
    i = 0
    while i < n:
        total = x * total
        i = i + 1
    return total


def findMinAndMax(L):
    a = L[0]
    b = L[0]
    for item in L:
        if item > a:
            a = item
        if item < b:
            b = item
    return (a, b)


def sum_func():
    # range(n) return a iterator
    print(list(range(101)))
    print(sum(range(101)))


aa_1 = 'aa1'
aa_2 = 'aa2'
aa_3 = 'aa3'


def update_global_var(var):
    # the updates for global var(aa_1) will take effect out of this function
    # aa_2, var(aa_3) will only be updated in the function
    global aa_1
    aa_1 = 'update_aa1'
    aa_2 = 'update_aa2'
    var = 'update_aa3'
    print(aa_1, aa_2, var)


def settolist():
    list_tem = [2, 5, 6, 45, 676, 33, 2, 67, 44, 77, 45]
    print(list_tem)
    set_tem = set(list_tem)
    print(set_tem)


def comprehension():
    print([x for x in range(2, 10)])
    print({('key%d' % x): x for x in range(2, 10) if x % 2 == 0})
    print({(x * x) for x in [3, 6, 12, 45, 90, 142, -1] if (100 > x > 0)})
    print(((x * x) for x in [3, 6, 12, 45, 90, 142, -1] if (100 > x > 0)))


def generator_1():
    print("create generator -1 by comprehension")
    return ((x * x) for x in [3, 6, 12, 45, 90, 142, -1] if (100 > x > 0))


def generator_2():
    print("create generator 2 by yield")
    yield '111'
    print("第二次")
    yield '222'
    print("第三次")
    yield '333'


def generator_3(max):
    n = 0
    while n < max:
        yield '这是第%d次调用' % (n + 1)
        n += 1
        if n == 3:
            return  # return can help to quit the generator


def test_generator_1():
    gen = generator_1()
    print(next(gen))
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(next(gen))
    print(gen.__next__())  # raise StopIteration exception
    #     Traceback(most recent call last):
    #     File "C:\Users\ZMing-Zhu\PycharmProjects\testpython-1\main.py", line 262, in < module >
    #     print(next(gen))
    # StopIteration


def test_generator_2():
    print(generator_2())
    for x in generator_2():
        print(x)
        print("--------分割线--------")


def test_generator_3():
    for x in generator_3(5):
        print(x)
        print("--------分割线--------")


def generator_4():
    for i in range(10):
        yield i


def test_generator_4():
    g = generator_4()
    print(g.__next__())
    print(g.send('send1'))
    print(g.send('send2'))
    print(g.send('send3'))


def filter_duplicate():
    ll = [3, 6, 89, 6, 3, 45, 9]
    ss = set(ll)
    print(ss)

    ll = [3, 6, 89, 6, 3, 45, 9]
    ll_new = []
    [ll_new.append(i) for i in ll if i not in ll_new]
    print(ll_new)

    dict_temp = {}
    print(list(dict_temp.fromkeys(ll)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    ss="hello world"
    reversed_ss=reversed(ss)
    print(reversed_ss)
    print(''.join(reversed_ss))
    ll=list(reversed(ss))
    print(''.join(ll))

    print('the char count is ',ss.count('l'))

    with open('test.txt','r') as f:
        # print(f.read())
        print('-----------------')
        print(len(f.readlines()))

    with open('test.txt','a') as f:
        f.write('hello world1 \n')
        f.write('hello world2 \n')
        f.write('hello world3 \n')
        f.write('hello world4 \n')


    s = {"a": 1, "b": 2, "c": 3}
    print(list(s.keys()))  # ['a', 'b', 'c']
    print(list(s))  # ['a', 'b', 'c']

    dic = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
    print(dic.items())
    for i in dic.items():
        print(i[0])
        print(i[1])
    ll = sorted(dic.items(), key=lambda x: x[0])
    print(ll)

    l1 = [1, 2, 3, 4, 5]
    l1.extend([2, 2, 2])  # [1, 2, 3, 4, 5, 2, 2, 2]
    print(l1)
    l2 = [1, 2, 3, 4, 5]
    l2.append([2, 2, 2])  # [1, 2, 3, 4, 5, [2, 2, 2]]
    print(l2)

    a=1.345654
    print(float("%.02f"%a)) # 1.35
    print(round(a,1))  # 1.3 round-四舍五入

    aa=(i for i in range(10))
    print(type(aa))

    # print_hi('PyCharm')

    # print(sys.path)

    # sum_func()

    # update_global_var(aa_3)
    # print(aa_1, aa_2, aa_3)

    # settolist()

    # comprehension()

    # test_generator_2()
    # test_generator_1()
    # test_generator_3()
    # test_generator_4()

    # logging
    # from logging_demo.logging_test1 import do_some
    # do_some()

    # 去重
    # filter_duplicate()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
