#!/usr/bin/python3


def bar(size):
    print(size)


class Triangle:

    def __init__(self, size):
        self.size = size

    def pyramid(self):
        print(self.size)

    def foo(self):
        print(self.size)


class TriangleOne:
    def __init__(self, size):
        self.size = size

    def foo(self):
        print(self.size)


obj = Triangle(30)
obj.pyramid()
obj.foo()

one = TriangleOne(10)
one.foo()

# obj.bar(40)  # this is not in class scoped
bar(50)
