from singleton import singleton
def get_singleton1():
    print('this is call_singleton1')
    print(id(singleton))

from module_singleton import ms
def get_age1():
    ms.count+=1
    ms.func()



