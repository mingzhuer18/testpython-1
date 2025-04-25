import subprocess
from functools import reduce


def fibb(n):
    a = 0
    b = 1
    for i in range(n):
        yield b
        a, b = b, a + b


ff = fibb(10)
# print(next(ff))
for i in ff:
    print(i)

'''
------------------------------------------------------------
'''


def fun(a, b, c='hello', /, d='world'):
    print(a, b, c, d)


# fun(1,2,c='3',d='4')  # error because positional-only symbol is defined, all left arguments should be positional arg
fun(1, 2, '3', '4')  # right

'''
------------------------------------------------------------
'''


def fun2(a, b, c, d='world', *, e, f='dd'):
    print(a, b, c, d, e, f)


# fun2(1,2,'3','4', '5','6')  ## * 后面要关键字方式传参，否则报错
fun2(1, 2, '3', '4', e='5', f='6')
fun2(b=1, a=2, d='hh', c=6, e=7, f='88')

import random

print(random.gauss(mu=0, sigma=1))

# random.seed(42) # if use seed, one seed number will mapping to a group of fixed number below
print(random.randint(1, 100))  # Always the same output when rerun with the same seed
print(random.randint(2, 6), random.random(), random.uniform(1.0, 5.0))
print(random.randint(2, 6), random.random(), random.uniform(1.0, 5.0))
print(''.join([str(x) for x in random.sample(range(10), 7)]))
print(''.join([str(x) for x in random.sample(range(10), 7)]))
print(random.randrange(11, 32, 3))
print(random.randrange(10))
print(random.choice(['a', 'n', 't', 'rt']))
print(''.join([str(x) for x in random.sample(range(10), 8)]))


def outer(cls):
    def inner(*args, **kwargs):
        if not hasattr(cls, '__instance'):
            instance = cls(*args, **kwargs)
            setattr(cls, '__instance', instance)
        return cls.__instance

    return inner


@outer
class AAA:
    def __init__(self, a):
        self.a = a


a1 = AAA(1)
print(id(a1))
print(a1.a)

a2 = AAA(2)
print(id(a2))
print(a2.a)

# def func(a,b):
#     if b==0: raise ZeroDivisionError("除数不能为0")
#     return a/b
#
# func(2,0)


"""
面试题
"""
ss = ("Hello, this is a good cat, do you think so? ")
print(len(ss))
print(ss.split(','))
print(len(ss.strip()))
print(len(ss.lstrip()))
print('-'.join(ss))

ss1 = ss[:]
print(id(ss1))
print(id(ss))

ss = "jdsdf"
print(id(ss1))
print(id(ss))

ll = ['a', 'b', 'c', {'z': 1, 'c': 'zz'}]
ll1 = ll[:]
print(ll, ll1)
print(id(ll), id(ll1))
print('列表第一个元素（不可变）', id(ll[0]), id(ll1[0]))
print('列表第4个元素（可变）', id(ll[3]), id(ll1[3]))
print(ll1[3]['z'])
ll1[3]['z'] = '4'  # 改变可变参数的值，影响原对象
print(ll1[3]['z'])
print('修改可变元素后 列表第4个元素（可变）同时修改', id(ll[3]), id(ll1[3]))
print(ll, ll1)
ll[1] = 'aaa'  # 改变不可变参数的值，影响原对象
print("修改不可变后，原对象和副本的id不同", id(ll[1]), id(ll1[1]))

print(ss1)
print(ss1[::-1])
print(ll[::-1])
print(ll1[-1])
print(ll1[-3:])

print(7 // 23)
print(27 // 7)  # 整除取整
print(27 % 7)
print(2 * 10)
print(2 ** 10)  # 2的10次方

mydict = {'a': 1, 'b': 2, 'c': 3, 'e': 5}
print(list(mydict.keys()))

mytuple = 1, 2, 3
print(mytuple)
a, b, c = mytuple
print(a, b, c)
a, *b = mytuple
print(a, b)

ss = 'azdelserijne'


def func(ss, start, stop):
    ss_new = ss[start:stop]
    print(ss_new)
    print(sorted(ss_new))


func(ss, 3, 8)

ret = map(lambda x, y: x + y + 'a', ['a', 'b', 'c', 'd', 'e'], ['1', '2', '3', '4', '5'])
print("show the list", list(ret))

ret = reduce(lambda x, y: (x + y) * 2, [1, 2, 3, 4])
print(ret)
# func(1,2)->6->func(6,3)->18->func(18,4)->44

ll = list(range(100))
print(reduce(lambda x, y: x + y, list(range(100))))
print(sum(ll))

p = subprocess.Popen('ping localhost', stdout=subprocess.PIPE, shell=True)

print(p.stdout.read())

"""
去重
"""
ll = [1, 2, 3, 4, 4, 2, "b", 34, 3, 23, 1, "a"]
print("无序", list(set(ll)))
newll = []
for i in ll:
    if i not in newll:
        newll.append(i)
print("有序", newll)
newll1 = []
print("有序", list(dict.fromkeys(ll)))

#有对兔子，从出生后的第3个月起每个月都生一对兔子。 小兔子长到第3个月后每个月又生一对兔子， 假设所有的兔子都不死，问30个月内每个月的兔子总对数为多少?

#问题分析：根据推导，每个月兔子总数为：1、1、2、3、5、8、13···，可以得到其就是斐波那契数列，是典型的迭代循环。
#注意第一个月和第二个月都是1对，所以30个月内实际是29个月，并且不包括第一个月

def generate_fibonacci(limit):
    a, b = 0, 1
    for i in range(limit):
        a, b = b, a + b
        yield a

total=0
count=0
gg=generate_fibonacci(30)
for i in gg:
    print(i, end=' ')

print("\n")


fib1 = 1
fib2 = 1
for i in range(3, 31):
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    i += 1
    print(fib, end=' ')
print("\n")
print(f"总和是{fib}")

def binary_search(gg,target):
    low,high=0,len(gg)-1
    while low<=high:
        mid=(low+high)//2
        if gg[mid]==target:
            return mid
        elif gg[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1 # 未找到目标

gg=[2,5,8,23,56,67,78,84,85]
print(binary_search(gg,78))

str_tem="1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229"
#str_tem=str_tem.replace(' ', ',')
print([int(x) for x in str_tem.split(' ')])

for i in range(1,10):
    for j in range(1,10):
        if i!=j:
            k=1100*i+11*j
            m = 30
            while m<100:
                if m*m==k:
                    print(m,k)
                m+=1


i=0
for A in range(5):
    for B in range(5):
        for C in range(5):
            if A!=B and B!=C and C!=A:
                print(A,B,C,end='|')
                i+=1
print("\nthere are {0} ways".format(i))

for a in range(20):
    for b in range(33):
        for c in range(100):
            if a+b+c==100 and a*5+b*3+c/3==100:
                print(a,b,c,end='|')






