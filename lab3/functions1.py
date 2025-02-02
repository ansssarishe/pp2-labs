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
def permutations(string):
    def permute(s, l, r):
        if l == r:
            perms.append(''.join(s))
        else:
            for i in range(l, r + 1):
                s[l], s[i] = s[i], s[l]  # swap
                permute(s, l + 1, r)
                s[l], s[i] = s[i], s[l]  # backtrack

    perms = []
    permute(list(string), 0, len(string) - 1)
    return perms

#6
def string_rev(string):
    reversed_words = ' '.join(string.split()[::-1])
    return reversed_words

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#8
def spy_game(nums):
    if nums.count(0) == 2 and nums.count(7) == 1:
        return True
    return False

#9
def volume(r):
    v = r * r * r * 3.14159265358979323846 * 4 / 3
    return v

#10
def unique_list(lst):
    new_lst = []
    for i in lst:
        if lst.count(i) == 1:
            new_lst.append(i)
    return new_lst

#11
def ispalindrome(string):
    return string == string[::-1]

#12
def histogram(lst):
    for i in lst:
        print(i * '*')

#13
import random
def guess():
    name = input("Hello! What is your name?")
    print("Well, KBTU, I am thinking of a number between 1 and 20.")
    num = random.randint(1, 20)
    g = -1
    while g != num:
        g = int(input("Take a guess."))
        if g < num:
            print("Your guess is too low.")
        elif g > num:
            print("Your guess is too high.")
        else:
            break
    print("Good job, " + name + "! You guessed my number in " + str(g) + " guesses!")







