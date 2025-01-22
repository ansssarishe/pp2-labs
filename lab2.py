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
mylist = thislist.copy() #asdakjs
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
thistuple = ("apple",) #comma is essential if i want to create tuple with one element
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#A tuple can contain different data types
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
#y = list(x)
#y[1] = "kiwi"
#x = tuple(y)
#print(x)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y #or we can just add tuples
print(thistuple) 

#Unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2 #tuple can be added
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 #tuple can be multiplied
print(mytuple)




#Sets 
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Set items are unchangeable, but you can remove items and add new items.
#In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Duplicates are not allowed
thisset = {"apple", "banana", "cherry", "apple"} #this will not be added
print(thisset)
#Set can contain different data types at once

#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
print("banana" in thisset)

#Once a set is created, you cannot change its items, but you can add new items.
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) #self explanotary
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #no elements will raise an error
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #no elements will NOT raise an error
print(thisset)

thisset.pop() #removes the random element element

"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)


#Dictionaries
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
x = thisdict.keys()
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) #adds a new key value pair
print(thisdict)
thisdict.pop("model")
print(thisdict)

for x in thisdict:
  print(x)
for x in thisdict.values():
  print(x)
for x in thisdict:
  print(thisdict[x])
for x, y in thisdict.items():
  print(x, y)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])




#If Statements
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

if a > b: print("a is greater than b")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

for x in "banana":
  print(x)

#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass