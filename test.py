import randomcat
string = input("Enter a string ")
n = 0
ans = []
fact = 1
l = len(string)
for x in range(1, l+1):
    fact *= x
print('Number of permutations: ', fact)

while n < fact:
    ns = ''.join(random.sample(string,len(string)))
    if ns not in ans:
        ans.append(ns)
        n += 1
print(ans)
