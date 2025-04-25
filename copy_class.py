import copy
"""
deep copy: 
完全复制新的副本，互相独立不影响； 
速度慢，占用内存多
shallow copy: 
复制原始对象的第一层对象的引用，修改不可变类型对象，会创建新的对象和内存id，并改变引用到新对象，原始对象的对应内容改变，副本对象的引用仍热执行旧对象；
修改可变类型对象，指向它的引用不受影响，因此原始对象和副本对象的值都会被修改
速度快，占内存少
"""
print("------------------------- deep copy ------------------------------")
from copy import deepcopy
a=[1,'er', True, {'ka':'va'},[2,3]]
b=deepcopy(a)
print("a is", a)
print("a id is",id(a))
print("b is",b)
print("b id is",id(b))
print("a[1] id is",id(a[1]))
print("b[1] id is",id(b[1]))
print("a[3] id is",id(a[3]))
print("b[3] id is",id(b[3]))

print("--- update a's first item's value(immutable), only impact a ---")
a[0]=4
print("a is", a)
print("a id is",id(a))
print("b is", b)
print("b id is",id(b))

print("---- update a's dict value, only impact a ----")
a[3]['ka']='V-UPDATE'
print("a is", a)
print("a id is",id(a))
print("b is", b)
print("b id is",id(b))

print("---- if set new list to a, a's id is changed ----")
a=[3,4,5,'ss']
print("a is", a)
print("a id is",id(a))
print("b is", b)
print("b id is",id(b))


print("------------------------- shallow copy ------------------------------")
c=[1,'djs', True, {'ka':'va'},[2,3]]
d=copy.copy(c)
print("c is", c)
print("d is", d)
print("c id is",id(c))
print("d id is",id(d))
print("c[1] id is",id(c[1]))
print("d[1] id is",id(d[1]))
print("c[2] id is",id(c[2]))
print("d[2] id is",id(d[2]))
print("c[3] id is",id(c[3]))
print("d[3] id is",id(d[3]))
print("c[4] id is",id(c[4]))
print("d[4] id is",id(d[4]))

print("----- update c's second item's value(immutable), only impact c ---")
c[1]='UPDATE'
print("c is", c)
print("c id is",id(c))
print("d is", d)
print("d id is",id(d))
print("c[1] id is",id(c[1]))
print("d[1] id is",id(d[1]))

print("---- update c's dict item's value(mutable), will impact both c and d ----")
c[3]['ka']='V-UPDATE'
print("c is", c)
print("c id is",id(c))
print("d is", d)
print("d id is",id(d))

print("---- update c's forth item's value, will impact both c and d ----")
c[4][1]=0
print("c is", c)
print("c id is",id(c))
print("d is", d)
print("d id is",id(d))
print("c[4] id is",id(c[4]))
print("d[4] id is",id(d[4]))

print("---- update c's third whole item(first layer), only impact c ----")
dict_temp={'g':'g','j':'j'}
c[3]=dict_temp
print("c is", c)
print("c id is",id(c))
print("d is", d)
print("d id is",id(d))

lll1=[1,2,3]
lll2=list(lll1)
print("lll1 id is",id(lll1))
print("lll2 id is",id(lll2))

lll1.append([3,4,5])
print("lll1 id is",id(lll1))
print("lll2 id is",id(lll2))
print("lll1 is", lll1)
print("lll2 is", lll2)

lll1[0]=[6,7]
print("lll1 id is",id(lll1))
print("lll2 id is",id(lll2))
print("lll1 is", lll1)
print("lll2 is", lll2)

lll3=[1,2,[3,4]]
lll4=list(lll3)
print("---相同index的元素地址相同0", id(lll3[0]), id(lll4[0]))
print("---相同index的元素地址相同1", id(lll3[1]), id(lll4[1]))
print("---相同index的元素地址相同2", id(lll3[2]), id(lll4[2]))
print("lll3 id is",id(lll3))
print("lll4 id is",id(lll4))

lll3[2][1]=5
print("lll3 id is",id(lll3))
print("lll4 id is",id(lll4))
print("lll3 is", lll3)
print("lll4 is", lll4)

# rr=(3,4,[2,3])
# sc=copy.copy(rr)
# dc=copy.deepcopy(rr)
# print("rr id is", id(rr))
# print("rr shallow copy id is", id(sc))
# print("rr deep copy id is", id(dc))
# print(dc)



