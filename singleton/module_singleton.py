

class ModuleSingleton:
    def __init__(self, name, count):
        self.name=name
        self.count=count

    def func(self):
        print("before: {} has {} apples ".format(self.name, self.count))

ms = ModuleSingleton("Mike", 23)