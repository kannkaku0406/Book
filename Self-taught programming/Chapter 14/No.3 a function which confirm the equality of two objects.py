def hello(one, two):
    return one is two

a = 10
b = 1
c = a
print(hello(a, b))
print(hello(a, c))