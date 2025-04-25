"""
迭代器是一种访问集合元素的方式,它实现了迭代协议，能够逐个获取集合元素，这些值不是从已有的数据集合中读取，而是边生成边读取，因此可以节省大量地内存空间
we can use dir() to check if a object contain __iter__ method and __next__ method
"""
from collections.abc import Iterator, Iterable

print(" ------------------ change a list to a iterator -----------------------")

my_list = [1, 2, 3]
my_iter = iter(my_list)
print("my_iter's type is ",my_iter)
print(next(my_iter))
print(next(my_iter))

# for 循环可以捕获stopIteration异常
for item in my_iter:
    print(item)

print(" ------------------ use generator to create a iterator -----------------------")
def my_generator():
    num = 1
    while num < 10:
        yield num*2
        num += 1

my_iter = my_generator()
print(next(my_iter))
print(next(my_iter))
for item in my_iter:
    print(item)

print(" ------------------ create a iterator class with __iter__() and __next__() -----------------------")
"""
迭代器协议
迭代器对象必须实现 __iter__() 和 __next__() 这两个方法。
__iter__() 方法返回迭代器对象本身。
__next__() 方法返回容器的下一个元素。如果没有更多元素，则抛出 StopIteration 异常。

"""
class MyIter(object):
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        # print("__iter__")
        return self

    def __next__(self):
        # print("__next__")
        if self.index < len(self.iterable):
            i = self.iterable[self.index]
            self.index += 1
            return i
        else:
            raise StopIteration


my_iter = MyIter(['1','2','3','4'])
print(next(my_iter))
for item in my_iter:  ## call __iter__() and __next__() to get an item in iterable obj
    print(item)

my_iter = MyIter('Hello world')
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
for item in my_iter:
    print(item)

print(" ------------------ for方法根据当前迭代器的__iter__()返回的对象来决定访问的是哪里的__next__() -----------------------")
class TestIter1(object):
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # print("other iterator's __next__")
        if self.index < len(self.iterable):
            i = self.iterable[self.index]
            self.index += 1
            return 'TestIter1-%d'%i
        else:
            raise StopIteration

my_iter1 = TestIter1([1,2,3])


class TestIter2:
    def __init__(self):
        self.index = 0
        self.my_list =[7,8,9]

    def __iter__(self):
        print("__iter__")
        return my_iter1

    def __next__(self):
        print("__next__")
        if self.index < len(self.my_list):
            i = self.my_list[self.index]
            self.index += 1
            return i*2
        else:
            raise StopIteration

my_iter = TestIter2()

print("----for loop of TestIter2's instance: get TestIter1's data -------")
for item in my_iter:
    print(item)

print("----use next for TestIter2's instance: get TestIter2's data -------")
print(next(my_iter))
print(next(my_iter))

print(dir([1,2,3]))
print(isinstance(my_iter, Iterator))
print(isinstance(my_iter, Iterable))
print(isinstance([1,2,3], Iterator))
print(isinstance([1,2,3], Iterable))





