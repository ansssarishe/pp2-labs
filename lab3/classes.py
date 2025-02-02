#1
class firstc:
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.upper())

#2
class Shape:
    class Square:
        def __init__(self, length):
            self.length = length

        def area(self = 0):
            return self.length * self.length
        
#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self = 0):
        return self.length * self.width

#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def dist(self, p):
        
        
#5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

#6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = list(filter(lambda x: is_prime(x), numbers))
return prime_numbers