def custom_sum(iterable):
    total = 0
    for item in iterable:
        total += item
    return total

numbers = [1, 2, 3, 4, 5]
print(custom_sum(numbers))  # Output: 15





def custom_ljust(string, width, fillchar=' '):
    return string + fillchar * (width - len(string))

def custom_rjust(string, width, fillchar=' '):
    return fillchar * (width - len(string)) + string

text = "Hello"
print(custom_ljust(text, 10, '-'))  # Output: "Hello-----"
print(custom_rjust(text, 10, '-'))  # Output: "-----Hello"




def is_palindrome(number):
    return str(number) == str(number)[::-1]

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(is_palindrome(121))  # Output: True
print(fibonacci(7))        # Output: [0, 1, 1, 2, 3, 5, 8]
print(factorial(5))        # Output: 120






def custom_range(start, stop, step=1):
    result = []
    while start < stop:
        result.append(start)
        start += step
    return result

print(custom_range(2, 10, 2))  # Output: [2, 4, 6, 8]