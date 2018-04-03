class Foo(object):
    def __add__(self, other):
        return 987
    def __mul__(self, other):
        return 123
    def __sub__(self, other):
        return 654
<<<<<<< HEAD


# 加一段
a = Foo()
b = Foo()
=======
a = Foo()
b = Foo()
print(a-b)
print('Hello World')
>>>>>>> ada7ffbc30d9fc3729e9e6851ab17117ab943d20
print(a*b) # 123
print(a+b) # 987
print(a-b) # 654
