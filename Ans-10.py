# Write a python program to get the key of lowest value from the dictionary.sample_dict = {'C': 92,'Java': 66,'Python': 85}
sample_dict = {
    'C': 92,
    'Java': 66,
    'Python': 85
}

# Find the key of the lowest value
lowest_value = min(sample_dict.values())
lowest_key = min(sample_dict, key=sample_dict.get)

# Print the key of the lowest value
print("Key of lowest value:", lowest_key)
