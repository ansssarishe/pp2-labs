#HOME
print("1st lab welcome")

#Intro
print("а кириллицу умеет принтить?")

#Get Started
import sys
print(sys.version)

#Syntax
if 99 > -3:
    print("no shit sherlock, 99 is def greater than -3")

y = 3
print(y)

#Comments
print("Didnt know") #I can leave comments like this

#Variables
x = 3
x = "Now its string type"

z = str("3") #this thingy is string now too
print(type(z)) #important: A != a, python is case sensitive

long_ahh_variable_name = 1
myvar = "John"
my_var = "John"
_my_var = "John" #why is it gray?
myVar = "John"
MYVAR = "John"
myvar2 = "John"

a, b ,c = 'a', 'b', 'c'
print(a)
print(b)
print(c)

a1, b1, c1 = "abc"
fruits = ["apple", "banana", "cherry"]
x1, y1, z1 = fruits

e = 'Hello'
r = 'Wrodl'
print(e, r)
print(e + r)

f = "bebebobo"
def myfunc():
  global f
  f = "rororor"

myfunc()

print("hi " + f)

#Data Types
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
complex = 1j
ra = range(3)
print(ra)
dictionary = {"amazing" : 3, "isn it?" : 2913}
print(dictionary)

#Numbers
q = 1    # int, it has no limits in length
w = 2.8  # float, "E" can be used to represent 10^
g = 1j   # complex
# i = complex(q)
# print(i) why does this not work?

import random
print(random.randrange(1, 3)) # 3 is not included

#Casting
x3 = float(1)     # x will be 1.0
y3 = float(2.8)   # y will be 2.8
z33 = float("3")   # z will be 3.0
w3 = float("4.2") # w will be 4.2       I am running out of variable names

#Strings
# " " or ' ' can be used, it really doesnt matter
multiline_thingy = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multiline_thingy)
#Strings are arrays
arr = "asdas"
print(arr[1])
print(len(arr))

for m in "banana":
  print(m)

insane = "Hello, World!"
print("Hello" in insane)
if("Hello" not in insane):
  print("Hello is not in the string")
print(insane[0:3]) #slicing
print(insane[-5:-2]) #negative indexing
print(insane[:2])
print(insane[2:])

print(insane.upper())
#strip removes whitespaces from the beginning or the end
print(insane.replace("o","J"))
print(insane.split("o"))
print(insane + "  " + insane)

age = 36
txt = f"My name is John, I am {age}"
print(txt)
price = 59
txt = f"The \t price \t is {price:.2f} dollars"
print(txt)


#\'	Single Quote	
#\\	Backslash	
#\n	New Line	
#\r	Carriage Return	
#\t	Tab	
#\b	Backspace	
#\f	Form Feed	
#\ooo	Octal value	
#\xhh	Hex value

#also strings have tons of methods, like isalpha, isnumeric, isalnum, etc



