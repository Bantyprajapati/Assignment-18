# Write a python program to create and print a dictionary which stores your information.(name, age, gender .....)
# Create a dictionary to store your information
my_information = {
    'name': 'John Doe',
    'age': 25,
    'gender': 'Male',
    # Add more key-value pairs for additional information
}

# Print the dictionary
print("My Information:")
for key, value in my_information.items():
    print(key.capitalize() + ": " + str(value))
