snake_case = "This is a variable using snake_case"
camelCase = "This is a variable using camelCase"
PascalCase = "This is a variable using PascalCase"
UPPER_CASE = "This is a variable using UPPER_CASE"


original_string = "Hello, World!"
reversed_string = original_string[::-1]
print(reversed_string)



example_list = [1, 2, 3]
print("Attributes from dir():")
print(dir(example_list))

# Let's use help() to understand the usage of a specific attribute
help(example_list.append)


example_object = "Hello"
all_attributes = dir(example_object)
for attribute in all_attributes:
    print(attribute)


example_string = "Hello, World!"
help(str.upper)
help(example_string.upper)
