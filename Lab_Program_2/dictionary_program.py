# 1. Sort the dictionaries in ascending order based on the Key of the dictionary.
def sort_dict_keys(dictionary):
    sorted_keys = sorted(dictionary.keys())
    return sorted_keys

my_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}

sorted_keys = sort_dict_keys(my_dict)

for key in sorted_keys:
    print(key, my_dict[key])

# 2. Create the dictionary with Numeric as Value in Key – Value pair and find the sum of all the values in the Dictionary
def sum_of_values(dictionary):
    total_sum = 0
    for value in dictionary.values():
        total_sum += value
    return total_sum

# Create a dictionary with numeric values
numeric_dict = {
    "value1": 11,
    "value2": 9,
    "value3": 30,
    "value4": 24,
    "value5": 19,
}

print("Original dictionary:", numeric_dict)

total_value_sum = sum_of_values(numeric_dict)

print("Sum of all values in the dictionary:", total_value_sum)

# 3.Write a Python code to demonstrate the sorting in descending order of values with lambda function.
my_dict = {'apple': 5, 'banana': 10, 'cherry': 3, 'date': 8, 'grape': 2}

# Sorting the dictionary in descending order of values using a lambda function
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

for key, value in sorted_dict.items():
    print(f'{key}: {value}')
