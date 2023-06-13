# Write a python program to create a dictionary that contains three dictionaries.(nested)
# Create the nested dictionaries
dict1 = {'name': 'John', 'age': 25, 'gender': 'Male'}
dict2 = {'name': 'Jane', 'age': 30, 'gender': 'Female'}
dict3 = {'name': 'Bob', 'age': 40, 'gender': 'Male'}

# Create the main dictionary containing the nested dictionaries
nested_dict = {'person1': dict1, 'person2': dict2, 'person3': dict3}

# Print the nested dictionary
for person, details in nested_dict.items():
    print(person, details)
