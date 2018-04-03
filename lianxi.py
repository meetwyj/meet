class Foo(object):
<<<<<<< HEAD
=======


>>>>>>> 44bf33a0a926e19b4710307f50dedce347816feb
    def __add__(self, other):
        return 987
    def __mul__(self, other):
        return 123
    def __sub__(self, other):
        return 654
a = Foo()
b = Foo()
print(a-b)
print('Hello World')
print(a*b) # 123
print(a+b) # 987
print(a-b) # 654
