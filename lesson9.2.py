class SuperClass:
    def greeting(self):
        print('Hello!')


class ChildClass(SuperClass):
    pass


child = ChildClass()
child.greeting()
