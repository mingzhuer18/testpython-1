# 普通成员变量可以被实例调用修改
# 带双下划线的私有成员变量 不能被实例调用直接修改

class Student(object):
    # class variable
    school = 'primary-school'
    __school = 'private-primary-school'

    # class method
    @classmethod
    def a_class_method(cls):
        print("this is a class method", "can i get public class variable?")
        if cls.school and cls.school == 'primary-school':
            print("YES!")
        else:
            print("NO!")
        print("this is a class method", "can i get private class variable?")
        if cls.__school and cls.__school == 'private-primary-school':
            print("YES!")
        else:
            print("NO!")

        print("this is a class method", "can i get public instance variable?", "\nNO")

    @staticmethod
    def a_static_method(change_variable = 'city'):
        print("this is a static method")
        print("can static method get public class variable?")
        if Student.school is not None:
            print("YES!")
            print("before change, public class variable is", Student.school)
            print("change public class variable to '%s'" % change_variable)
            Student.school = change_variable
            print("after change, public class variable is", Student.school)
        else:
            print("NO!")
        print("can static method get private class variable?")
        if Student.__school is not None:
            print("YES!")
            print("change private class variable to '%s'" % change_variable)
            Student.__school = change_variable
            print("private class variable is", Student.__school)
        else:
            print("NO!")

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.__score = 0

    def get_info(self):
        return self.name, self.__age, self.__score

    def set_score(self, score):
        self.__score = score
        self.print_score()
        return self.__score

    def print_score(self):
        print("score is", self.__score)

    def print_class_var(self):
        # self.school="sfkljflsjdfls"
        print("在成员方法中用self.var方式访问类变量", self.school)


stu = Student("Annie", 24)
print(Student.__dict__)
print(stu.__dict__)
print(
    "实例方法调用类变量用self，只是get不会添加这个类变量到成员变量列表，如果修改了类变量，则会添加到实例的成员变量列表中")
stu.print_class_var()

print(Student.__dict__)
print(stu.__dict__)
print(stu.get_info())
# ('Annie', 24, 0)
stu.name = 'Ben'
print(stu.get_info())
# ('Ben', 24, 0)
print(stu.get_info())
# ('Ben', 24, 0)
print("可以动态添加成员变量？给inst和class加一个teacher试试 - YES")
stu.teacher = "tom"
Student.teacher = "Jacky"
print(Student.__dict__)
print(stu.__dict__)
stu.teacher = "Lucy"
Student.teacher = "Lucy"
print(Student.__dict__)
print(stu.__dict__)

print("可以动态添加方法？给inst和class加试试")


def add_num(num1, num2):
    return num1 + num2


stu.add_num1 = add_num
print(stu.add_num1(3, 5))

Student.add_num2 = add_num
print(Student.add_num2(5, 6))
print(Student.__dict__)
print(stu.__dict__)

stu.set_score(70)
print(stu.get_info())
# ('Ben', 24, 70)
print(Student.get_info(stu))

print("---------------------------- class var and class method -----------------------------")
stu2 = Student('Anni', 14)
print(stu.school)
stu.print_class_var()
print("the private class var cannot be invoked by instance and class")
# print(stu.__school)
# print(Student.__school)
print(stu2.school)
stu2.print_class_var()
print(Student.school)

stu.a_class_method()
Student.a_class_method()
print("update class variable in instance 1 from primary-school to secondary-school")
stu2.school = 'primary-school-update'
print(stu.school)
stu.print_class_var()
print(stu2.school)
stu2.print_class_var()
print(Student.school)
Student.school = 'secondary-school'
print(stu.school)
stu.print_class_var()
print(stu2.school)
stu2.print_class_var()
print(Student.school)
stu.school = 'third-school'
print(stu.school)
print(stu2.school)
print(Student.school)
stu2.school = 'forth-school'
print(stu.school)
print(stu2.school)
print(Student.school)

print(Student.__dict__)
print(stu.__dict__)

print("---------------------------- static method -----------------------------")
stu.a_static_method()
print("---------------------")
stu2.a_static_method()
print("---------------------")
Student.a_static_method()
