#1
from functools import reduce

def multiply(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [1, 2, 3, 4, 5]
result = multiply(numbers)
print(result)

#2
def count(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

s = "asdasd WDAD sda DAD ASd"
up, lo = count(s)
print(up, lo)

#3
def pal(s):
    return s == s[::-1]

s = asddsa
res = pal(s)
print(res)

#4
import time
import math
def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

number = 25100
milliseconds = 2123
result = delayed_square_root(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

#5
def all_elements_true(t):
    return all(t)

t = (True, True, True)
result = all_elements_true(t)
print("Are all elements of the tuple true?", result)