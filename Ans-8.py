# Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
list1 = ['name', 'age', 'gender']
list2 = ['John', 25, 'Male']

# Convert the two lists into a dictionary
my_dict = dict(zip(list1, list2))

# Print the resulting dictionary
print("Dictionary:", my_dict)
