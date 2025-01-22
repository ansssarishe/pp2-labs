"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
"""
def my_function():
  print("Hello from a function")

my_function()


def my_function(fname): #arguments can be passed
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(*kids): # *if i dont know how many arguments i will pass
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function(country = "Norway"): #Norway is the default value
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function() #will use the default value
my_function("Brazil")


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


"""
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

To specify that a function can have only positional arguments, add , / after the arguments:
"""
def my_function(x, /):
  print(x)

my_function(3)


def my_function(*, x): #vice versa if the previous
  print(x)

my_function(x = 3)


def my_function(a, b, /, *, c, d): #they can be combined
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


"""
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
"""

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)


print("Lambda function")


#Lambda function
"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
"""
x = lambda a : a + 10
print(x(5))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))