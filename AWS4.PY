# Using the + operator to concatenate strings
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

# Concatenating strings with numeric values
age = 30
message = "I am " + str(age) + " years old."
print(message)  # Output: I am 30 years old.



# Using f-string (formatted string literals)
name = "Alice"
age = 25
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Alice and I am 25 years old.

# Using str.format() method
item = "book"
price = 19.99
formatted_string = "The {} costs ${:.2f}".format(item, price)
print(formatted_string)  # Output: The book costs $19.99

# Using % formatting
quantity = 3
total_price = 45.00
formatted_string = "You bought %d items for a total of $%.2f" % (quantity, total_price)
print(formatted_string)  # Output: You bought 3 items for a total of $45.00



# Addition
a = 10
b = 5
sum_result = a + b
print(sum_result)  # Output: 15

# Subtraction
x = 20
y = 8
difference = x - y
print(difference)  # Output: 12

# Multiplication
num1 = 6
num2 = 7
product = num1 * num2
print(product)  # Output: 42

# Division
numerator = 15
denominator = 3
quotient = numerator / denominator
print(quotient)  # Output: 5.0

# Modulus (Remainder)
dividend = 17
divisor = 4
remainder = dividend % divisor
print(remainder)  # Output: 1






# += (Addition assignment)
total = 10
increment = 5
total += increment
print(total)  # Output: 15

# -= (Subtraction assignment)
value = 100
decrement = 30
value -= decrement
print(value)  # Output: 70

# *= (Multiplication assignment)
quantity = 3
item_price = 10
total_cost = 0
total_cost += quantity * item_price
print(total_cost)  # Output: 30