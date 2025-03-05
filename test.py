def process_numbers(x):
    return x % 2 == 0

def square(x):
    return x * x
        
nums = [1, 2, 3, 4, 5, 6]
it = iter(nums)
ans = list(filter(process_numbers, nums))
print(ans)
print(list(map(square, it)))