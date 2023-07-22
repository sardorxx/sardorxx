class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + self.x, self.y + self.y

    def __mul__(self, other):
        return self.x * self.x, self.y * self.y

    def __sub__(self, other):
        return self.x - self.x, self.y - self.y

    def __truediv__(self, other):
        return self.x / self.x, self.y / self.y

    def __floordiv__(self, other):
        return self.x // self.x, self.y // self.y


p1 = Point(1, 7)
p2 = Point(2, 8)

print(p1 + p2)
print(p1 - p2)
print(p1 * p2)
print(p1 / p2)
print(p1 // p2)


class Number:
    def __init__(self, num):
        self.num = num

    def __mod__(self, other):
        return self.num % other.num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num + other.num

    def __pow__(self, other):
        return self.num ** other.num

    def __rshift__(self, other):
        return self.num + other.num

    def __lshift__(self, other):
        return self.num + other.num

    def __and__(self, other):
        return self.num & other.num

    def __or__(self, other):
        return self.num | other.num

    def __xor__(self, other):
        return self.num ^ other.num

    def __lt__(self, other):
        return self.num < other.num

    def __gt__(self, other):
        return self.num > other.num

    def __le__(self, other):
        return self.num <= other.num

    def __ge__(self, other):
        return self.num >= other.num

    def __eq__(self, other):
        return self.num == other.num

    def __ne__(self, other):
        return self.num != other.num




num1 = Number(12)
num2 = Number(11)

print(num2 % num1)
print(num2 + num1)
print(num2 - num1)
print(num2 ** num1)
print(num2 >> num1)
print(num2 << num1)
print(num2 & num1)
print(num2 | num1)
print(num2 ^ num1)
print(num2 < num1)
print(num2 <= num1)
print(num2 >= num1)
print(num2 == num1)
print(num2 != num1)
























