num = int(input())

#1
def squa(num):
    a = 1
    while a <= num:
        yield a*a
        a += 1
        

ans1 = squa(num)
listanss = []
for i in ans1:
    listanss.append(i)
print(listanss)


#2
def evens(num):
    a = 1
    while a <= num:
        if a % 2 == 0:
            yield a
        a += 1

ans2 = evens(num)
listans = []
for i in ans2:
    listans.append(i)
print(listans)         



#3
def by3_4(num):
    for i in range(num + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
ans3 = by3_4(num)
listans2 = []
for i in ans3:
    listans2.append(i)
print(listans2)  

#4
#это задание буквально то же самое что первое, просто отличие в том, что мне надо использовать range(a, b+1)

#5
def rev(num):
    for i in reversed(range(num + 1)):
        yield i

ans4 = rev(num)
list4 = []
for i in ans4:
    list4.append(i)
print(list4)
