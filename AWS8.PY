def custom_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step

for num in custom_range(2, 10, 2):
    print(num)  # Output: 2, 4, 6, 8




def recursive_range(start, stop, step=1):
    if start < stop:
        yield start
        yield from recursive_range(start + step, stop, step)

for num in recursive_range(2, 10, 2):
    print(num)  # Output: 2, 4, 6, 8





def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

gcd_lambda = lambda a, b: a if b == 0 else gcd_lambda(b, a % b)

print(gcd_recursive(48, 18))  # Output: 6
print(gcd_lambda(48, 18))     # Output

