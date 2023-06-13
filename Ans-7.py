# Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
# Create three dictionaries
dict1 = {'name': 'John', 'age': 25, 'gender': 'Male'}
dict2 = {'name': 'Jane', 'age': 30, 'gender': 'Female'}
dict3 = {'name': 'Bob', 'age': 40, 'gender': 'Male'}

# Create a dictionary containing the three dictionaries
main_dict = {
    'dict1': dict1,
    'dict2': dict2,
    'dict3': dict3
}

# Print the main dictionary
print("Main Dictionary:")
for key, value in main_dict.items():
    print(key, value)
