class MyNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self,other):
        return MyNumber(self.a + other.a, self.b + other.b)

    def __str__(self):
        return 'MyNumber (%d, %d)' % (self.a, self.b)

num1 = MyNumber(1, 2)
num2 = MyNumber(10, 20)
print(num1 + num2)
