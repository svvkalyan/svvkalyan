# 1) Name = “some name”
name = "some name"

# Convert to uppercase, lowercase, and capitalize
upper_name = name.upper()
lower_name = name.lower()
capitalized_name = name.capitalize()

# Replace 'e' with 'E'
modified_name = name.replace('e', 'E')

print(upper_name)
print(lower_name)
print(capitalized_name)
print(modified_name)


# 2) L = [1, 2, 3]
L = [1, 2, 3]

# Extend the list and remove the 5th value (index 4)
L.extend([5, 6, 7])
del L[4]

print(L)



# 3) d = {'mango': 10, 'banana': 0, 'apple': 15, 'orange': 0, 'pineapple': 20}
d = {'mango': 10, 'banana': 0, 'apple': 15, 'orange': 0, 'pineapple': 20}

# Remove out of stock fruits
out_of_stock_fruits = [fruit for fruit, quantity in d.items() if quantity == 0]
for fruit in out_of_stock_fruits:
    del d[fruit]

# Update mango quantity and decrease pineapple quantity
d['mango'] = 15
d['pineapple'] -= 5

print(d)




a = [2, 4, 6, 8, 10]

# Target: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
a += [12, 14, 16, 18]
print(a)

# Target: [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
a[:] = [-i for i in a][::-1] + [0]
print(a)

# Target: [2, 3, 4, 5, 6, 7, 8, 10]
a[1:1] = [3, 4, 5, 6, 7]
print(a)