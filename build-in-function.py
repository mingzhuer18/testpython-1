"""
enumerate
"""
from functools import reduce

ll = [1, 2, 3]
ret = enumerate(ll)
print(type(ret))
print(ret)
print(tuple(ret))

for index, item in enumerate(ll):
    print(index, item)

for item in enumerate(ll):
    print(item)

for index, item in enumerate(ll, 2):
    print(index, item)

dict_temp = dict(enumerate(ll, 2))
print(dict_temp)

"""
map(func,iterable[,...]
"""
set1 = {1, 2, 3, 4, 5}
ret = map(lambda x: x ** 2 + 1, set1)
print(type(ret))
print(isinstance(ret, map))
print(ret)

for item in ret:
    print(item)

list1 = [4, 7, 9, 23]
ret = map(lambda x, y: (x + y) ** 2 + 1, set1, list1)
print(list(ret))

"""
list.sort()
"""

list1 = ["strawberry", "apple", "banana", "cherry", "pear"]
# list1.sort(key=lambda x: len(x))  #可用
list1.sort(key=len)
print(list1)

"""
sorted()
"""
print(sorted(list1, key=len))
print(sorted(list1, key=len, reverse=True))

ss=range(10)
print(type(ss))
print(ss)
for item in ss:
    print(item)



"""
filter(func, iterable)
"""

list1=[1,2,3,4,5]
def func(x):
    if x%2==0:
        return 1
    else: return 0
# ret = filter(lambda x: x % 2 == 0, list1) ## 可用
ret = filter(func, list1)
print(type(ret))
print(list(ret))

"""
eval() vs repr()
"""
s = 'python'
a = str(s)
b = repr(s)

print(a)
print(b)
print(type(a))
print(type(b))
print(eval(b))
print("-" * 100)
print(a,b)
print(a == b)

print("-" * 100)
repr_list=repr(list1)
print(type(list1))
print(repr_list)
print(type(repr_list))
# repr_list.sort() ## cannot use sort() as it's not a list
eval_list=eval(repr_list)
print(eval_list)
print(type(eval_list))
eval_list.sort()

"""
reduce(func, iterable[, initial])
"""

list1=[1,2,3,4,5]
print(reduce(lambda x,y: (x+y)*2, list1))

"""
zip(*iterable)
return a iterator
"""
zz = zip([1,2,3,4,5],['a','b','c','d'])
print(zz)
for i in zz:
    print(i)


