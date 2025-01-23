#Functions 1
#1
def normalweight_to_american(grams):
    return grams * 28.3495231

#2
def americantemp_to_normaltemp(faren):
    C = (5 / 9) * (faren - 32)
    print(C)

#3
def solve(heads, legs):
    for i in range(heads):
        j = heads - i
        if (2*i + 4*j) == legs:
            print("Chickens: ", i, "Rabbits: ", j)

#4
numbers = [int(x) for x in input("Enter numbers ").split()]
def prime(numbers):
    def isprime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return [n for n in numbers if isprime(n)]
primes = prime(numbers)
print(primes)

#5
import random
string = input("Enter a string ")
n = 0
ans = []
fact = 1
l = len(string)
for x in range(1, l+1):
    fact *= x
print('Number of permutations: ', fact)




