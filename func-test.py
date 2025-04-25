"""
******* 参数类型：默认值参数、位置参数、关键字参数、仅位置参数标记、仅关键字参数标记、文档字符串、函数注解 *******
"""
from setuptools.command.build_ext import if_dl

print(__doc__)
# test_func_para1
# * 可变参数，表示任意多个位置参数，返回一个元组
# ** 任意多个关键字参数，返回一个字典


# test_func_para2
# * 也可以表示强制位置参数， 它后面的参数只能通过关键字传递参数给third

# test_func_para3
# 值传递: 不可变参数 - 函数内值改变，不影响函数外
# 引用传递: 可变参数 - 函数内值改变，影响函数外

def test_func_para1(first, second='sec_values', *third, **forth):
    print(first)
    print(second)
    print(third)
    print(forth)


def test_func_para2(first, second, *, third='33'):
    print(first)
    print(second)
    print(third)


def test_func_para3(first_str, second_list):
    print('--------- in func, before change --------------')
    print('########', first_str, id(first_str), type(first_str).__name__)
    print('%%%%%%%%', second_list, id(second_list), type(second_list).__name__)
    print('--------- in func, change --------------')
    first_str = 'this is not hello, has been changed'
    second_list[2] = 'second'
    # string is immutable - below id is changed
    print('########', first_str, id(first_str), type(first_str).__name__)
    # list is mutable  - below id is not changed, but the item is changed
    print('%%%%%%%%', second_list, id(second_list), type(second_list).__name__)
    print('--------- in func, quite --------------')


para_var1 = [1, 2, 3]
para_var2 = {'k1': 'v1', 'k2': 'v2'}
test_func_para1('this is first', 'this is second', *para_var1, **para_var2)
test_func_para2('this is first', 'this is second', third='this is third')

fs = 'hello'
sl = [3, 4, 'wrwe']
print('########', fs, id(fs), type(fs).__name__)
print('%%%%%%%%', sl, id(sl), type(sl).__name__)
test_func_para3(fs, sl)
# if fs is changed in func, when quit the func, compare to the time when not call func, fs's values is not changed, but id changed
print('########', fs, id(fs), type(fs).__name__)
print('%%%%%%%%', sl, id(sl), type(sl).__name__)


print("(1)默认值参数是可变参数（list/dict/class等）(2)调用函数时使用默认值参数；随着多次调用默认值会累计")
def test_func_4(a, l=[]):
    l.append(a)
    print(l)

test_func_4(11)
test_func_4(12)
test_func_4(13)
# [11]
# [11, 12]
# [11, 12, 13]

print("(1)默认值参数是可变参数（list/dict/class等）(2)调用函数时使用默认值参数；需要特别处理避免默认值累计现象")
def test_func_5(a, l=[]):
    if not l:
        l=[]
    l.append(a)
    print(l)

test_func_5(a=11)
test_func_5(12)
test_func_5(13)
# [11]
# [12]
# [13]

print("-------- 仅限位置参数：/ 仅限关键字参数：* ----------")

def combined_example(pos_only, /, standard, *, kwd_only):
    """To test Positional-Only Parameters and keyword-only Parameters
    /(forward-slash) 仅限位置参数标记，之前的参数必须使用位置参数传值
    * 仅限关键字参数标记， 之后的参数必须使用关键字参数形式传递该形参
    """
    print(pos_only, standard, kwd_only)

print(combined_example.__doc__)
combined_example('first', 'second', kwd_only=True)
combined_example('first', standard='second', kwd_only=True)
# combined_example(post_only='first',standard='second', kwd_only=True) # combined_example() got an unexpected keyword argument 'post_only'

print("----------- annotation for function -------------")
def test_func_annotation(a:str,  c:dict,b:int=5,)->list:
    return [x+'-'+y+'-'+a+'-'+str(b) for x,y in c.items() ]

print(test_func_annotation.__annotations__)
print(test_func_annotation('anotest', {'second':'sss'}))

print("--------------- 解包 ------------------------")
print("1 - 列表或元组解包 -----")
my_list = [1,2,3]
my_tuple=('a','b','c')
my_str='hello'

a,b,c=my_list
print(a,b,c)
a,b,c=my_tuple
print(a,b,c)
a,b,c,d,e=my_str
print(a,b,c)

print("2 - 使用*解包list -----")
print(*my_list)
print(*my_tuple)
print(*my_str)

print("2-1 - 使用*解包传入函数的可变位置参数 -----")
print("2-1 - 调用变量时需要在集合前加* -----")
tt=[4,7,0]
def unpack_position(a, *args):
    print(a)
    print(args)
unpack_position('first', *tt)
unpack_position('first', *my_tuple)

print("3 - 使用**解包dict -----")
info = {'name': 'Bob', 'age': 30}
print(info)
print("name is {name}, age is {age}".format(**info))
def unpack_dict(**kwargs):
    for key, value in kwargs.items():
        print(f"k:v is {key}:{value}")
unpack_dict(**info)







