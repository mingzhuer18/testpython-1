from singleton import singleton
def get_singleton2():
    print('this is call_singleton2')
    print(id(singleton))

from module_singleton import ms
def get_age2():
    ms.count+=1
    ms.func()