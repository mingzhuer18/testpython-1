class MyDecorator:
    def __init__(self, cls):
        """
        初始化装饰器，接受被装饰的类。
        """
        self.cls = cls

    def __call__(self, *args, **kwargs):
        """
        实例化被装饰的类，并在实例化过程中添加额外功能。
        """
        print(f"创建 {self.cls.__name__} 实例时，执行装饰器逻辑")
        # 创建原始类的实例
        instance = self.cls(*args, **kwargs)
        # 可以对实例进行额外处理
        return instance

    # def greet(self):
    #     print("this is decorator greeting")


# 使用装饰器类来装饰另一个类
@MyDecorator
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

# 创建类的实例
obj = MyClass("Alice")
print(obj)
obj.greet()
# 输出：
# 创建 MyClass 实例时，执行装饰器逻辑
# Hello, Alice!
