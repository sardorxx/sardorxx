
"""1  - Exercise """


class Shape:
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return self.length


class Square(Shape):
    def __init__(self, length, radius):
        super().__init__(length)
        self.radius = radius

    def get_length(self):
        return str(self.length) + " " + str(self.radius)


shape = Shape(19)
square = Square(19, 7)
print(square.get_length())

"""2  - Exercise """


class Circle:
    def __init__(self, p, radius):
        self.radius = radius
        self.p = p

    def get_area(self):
        return self.p * self.radius * self.radius


circle = Circle(3.14, 12)

print(circle.get_area())

"""3  - Exercise """


class American:
    def __init__(self, state):
        self.state = state

    def print_s(self):
        return self.state


class NewYorker(American):
    def __init__(self, state, person):
        super().__init__(state)
        self.person = person

    def show_super(self):
        return str(self.state) + " " + self.person


american = American(50)
newyorker = NewYorker(50, 'John')
print(issubclass(NewYorker, American))


"""4  - Exercise """


class Init:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        return self.a + self.b


init = Init(2, 9)
print(init.a + init.b)

"""5  - Exercise """


class TwoMethod:

    def __init__(self, string):
        self.string = string

    def get_string(self):
        return self.string

    @staticmethod
    def to_upper(string):
        return string.upper()


two = TwoMethod('')
print(two.to_upper(input("String: ")))

"""
6-exercise
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __mul__(self):
        return self.length * self.width


rectangle = Rectangle(12, 6)
print(rectangle.length * rectangle.width)

""" 7 - exercise """


class American:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def print_nationality(string):
        return string.upper()


two = American('')
print(two.print_nationality('American'))
