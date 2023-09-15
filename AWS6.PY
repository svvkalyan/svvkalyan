def custom_upper(string):
    return string.upper()

def custom_lower(string):
    return string.lower()

# Testing the custom functions
text = "Hello, World!"
print(custom_upper(text))  # Output: HELLO, WORLD!
print(custom_lower(text))  # Output: hello, world!




sequence = [1, 2, 34, 65, 1, 2, 65, 66, 44, 33, 22, 87, 123412, 9, 78, 76]
odd_sequence = [num for num in sequence if num % 2 != 0]
print(odd_sequence)  # Output: [1, 65, 1, 65, 33, 87, 9]





fruits = {
    'apple': 10,
    'mango': 20,
    'pineapple': 25,
    'orange': 30,
    'strawberry': 50,
    'jackfruit': 10
}

fruits_above_20 = {fruit: value for fruit, value in fruits.items() if value > 20}
print(fruits_above_20)
# Output: {'pineapple': 25, 'orange': 30, 'strawberry': 50}
