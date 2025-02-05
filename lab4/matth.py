import math

com = dir(math)
print(com)


digr = 15
pi = math.pi
rad = digr * pi / 180
rad2 = round(rad, 6)
print(rad2)



#2
H = 5
b1 = 5
b2 = 6
area = ((b1 + b2)/2)*H
print(area)


#3
sides = 4
length = 25
a = (sides*length*length*(math.cos(pi/sides))/math.sin(pi/sides))/4
print(a)

#4
base = 5
height = 6
print(base*height)