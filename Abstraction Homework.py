
from abc import ABCMeta, abstractmethod


class List(metaclass=ABCMeta):
    def __init__(self, social):
        self.social = social

    @abstractmethod
    def show_social_apps(self):
        return self.social

    @abstractmethod
    def show_age(self):
        return self.show_age()

    @abstractmethod
    def __bool__(self):
        return True

    def get_social(self):
        return self.social


class Str(ABCMeta):
    def __new__(cls, *args, **kwargs):
        super.__new__(cls)

    def view_point(cls):
        pass

    @staticmethod
    def share_a(self):
        return self.social

    @abstractmethod
    def show_str(cls):
        print(" Hello , My  new followers")


class Set(ABCMeta):

    A = {3, 8, 4, 3, 8, 9}
    @abstractmethod
    def print_set(cls):
        return ABCMeta


class Bool(metaclass=Str):
    def __new__(cls, *args, **kwargs):
        super.__new__(cls)

    def display(self):
        return 'GitHub.com'

class Int(metaclass=Bool):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + self.b


A = Int(12, 8)


# lst = List('Telegram')
# print(lst.show_social_apps())
# ls = List(23)
# print(ls.show_age())
# al = List(True)
# print(al.__bool__())
# print(ABCMeta.print_set)
# print(a + b)