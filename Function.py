from time import sleep
import math


class Max:
    def __init__(self, lst):
        self.lst = lst

    def max_funk(self):
        return self.lst


max_s = Max(max(5, 7, 9, 5, 2))
print(max_s.max_funk())


class Sum:
    def __init__(self, lst):
        self.lst = lst

    def sum_num(self):
        s = 0
        for i in self.lst:
            s += i
        return s


sum_ = Sum([5, 8, 4, 4, 6, 7, 8])
print(sum_.sum_num())


class Mul:
    def __init__(self, lst):
        self.lst = lst

    def mul_num(self):
        s = 1
        for i in self.lst:
            s *= i
        return s


mul_ = Mul([5, 8])
print(mul_.mul_num())


def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1


print(string_reverse('1234abcd'))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(n=998))


def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")


test_range(10)


def string_test(s):

    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])


string_test('The quick Brown Fox')


def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))



def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
print(test_prime(9))



def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))





def printValues():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    print(l)


printValues()


def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)


print("Square root after specific miliseconds:")
print(delay(lambda x: math.sqrt(x), 100, 16))
print(delay(lambda x: math.sqrt(x), 1000, 100))
print(delay(lambda x: math.sqrt(x), 2000, 25100))


def even_nums():

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
        pass
    return b


print(even_nums())

even_nums()


def pascal():
    pascals = 1
    m = 10
    for i in range(m):
        pascals += 1
    return pascals


print(pascal())
pascal()

