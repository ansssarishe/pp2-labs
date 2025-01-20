#Booleans
#They represent either True or False values
print(10>9)
print(bool("hello"))
print(bool(15)) # These two thingys are True beacuse they are not empty and not 0

def myFunction() :
  return True

print(myFunction())

#Operators
#are used to perform operations on variables and values
"""
Python divides the operators in the following groups:

Arithmetic operators(+, -, *, /, %, **, //)
Assignment operators(=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=)
Comparison operators(and, or, not)
Logical operators(and, or, not)
Identity operators(is, is not)
Membership operators(in, not in)
Bitwise operators(&, |, ^, ~, <<, >>)
"""

#Lists
#are used to store multiple items in a single variable
#List items are ordered, changeable, and allow duplicate values.
list = ["apple", "banana", "cherry"]
l = [1, 5, 7, 9, 3]
print(l)
for x in range(0,4):
    l.append(x)
    print(l)
#Hence, the list is changeable and allows duplicate values and all new added thinks are added to the end
list1 = ["abc", 34, True, 40, "male"] #Lists can contain different data types
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #right number is never included

thislist1 = ["apple", "banana", "cherry"]

if "apple" in thislist1:
  print("Yes, 'apple' is in the fruits list")

thislist1[0] = "blackcurrant"
print(thislist1)

thislist1[1:3] = ["blackcurrant", "watermelon"]
print(thislist1)

thislist1[1:2] = ["asdasdas", "asdasd"]
print(thislist1)

thislist.insert(2, "watermelon")
print(thislist)

thislist.append("orange") #adds to the end
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #merges two arrays, no matter the tuple set or lists, even data types as long as first container allows it
print(thislist) 



thislist.remove("banana") #removes specific element of the list
print(thislist)

thislist.pop(1) #removes element by index, if index is not present it will pop the last item
print(thislist)

del thislist[0] #removes by index
print(thislist)

del thislist #deletes the list
# print(thislist) this will cause an error

thislist = ["apple", "banana", "cherry"]
thislist.clear() #deletes all elements
print(thislist)

for x in thislist:
  print(x)

for i in range(len(thislist)):
  print(thislist[i])

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

[print(x) for x in thislist] #list comprehension

"""
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)


newlist1 = [x for x in fruits if "a" in x] #way shorter isnt it
print("new list 1  ")
print(newlist1)

#The syntax is [expression for item in iterable if condition == True]
#the condition is optional, it is like sorting thingy
newlist2 = [x for x in fruits if x != "apple"] #this will remove apple from the list
print(newlist2)
#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple"

newlist3 = [x for x in range(10) if x < 5] #iterable can be anything
print(newlist3)

newlist4 = [x.upper() for x in fruits] #upper is a method that makes the string uppercase
print(newlist4)

newlist5 = ['hello' for x in fruits] #this will make a list of hello with the same length as fruits
print(newlist5)



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #will sort alphabetically
print(thislist)

thislist.sort(reverse = True) #will sort in reverse order
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #sorts based on how far from 50
print(thislist) #key = function is used to sort based on a function

#sort is key sensetive so to make it non sensitive we can do the following:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#You cannot copy a list simply by typing list2 = list1, because:
#list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#thislist = ["apple", "banana", "cherry"]
#mylist = list(thislist) #also copies
#print(mylist) somehow it doesnt work

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:] #same 
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)




#Tuples
"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
"""

