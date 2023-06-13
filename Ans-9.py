# Write a python program to merge two python dictionaries into one dictionary.
dict1 = {'name': 'John', 'age': 25}
dict2 = {'gender': 'Male', 'country': 'USA'}

# Merge the two dictionaries into one
merged_dict = {**dict1, **dict2}

# Print the merged dictionary
print("Merged Dictionary:", merged_dict)
