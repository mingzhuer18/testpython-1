
def func():
    try:
        num = int(input("please input a number"))
        print(num+1)
        # return 100/num
    except ValueError:
        print("please input a number")
    except ZeroDivisionError:
        print("please input a non-zero number")
        raise
    else:
        print("right!")
    finally:
        print("finally")
    print("-" * 50)

print(func())

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

print("------------ except 匹配从前往后，一旦匹配不会执行后面的except -----------------")
print("------------ 如果异常是某个类的子类，且父类的 except 块在前，那么父类的 except 块会捕获该异常 ------------ ")
for cls in [ C, D, B]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

x=5
assert x<6, "x should be less than 6"
assert x>6, "x should be greater than 6"




