# 1.Create a LIST with your domain attributes, insert the elements using the append (), insert(), extend() 
# and add any iterables (tuples, sets, dictionaries etc.) to the list (Use all the methods ).
print("Output\n")
print("--------------")
print("\n1. Program to create a LIST with your domain attributes, insert the elements using the append (), insert(), extend() and add any iterables to the list (Use all the methods ).\n")
domain_attributes = ["FirstName", "LastName","Email",]

# Using append() to add individual elements
domain_attributes.append("BloodGroup")
domain_attributes.append("Gender")

# Using insert() to add an element at a specific index
domain_attributes.insert(1, "StaffID")

# Using extend() to add multiple elements from an iterable
new_attributes = ["ContactNumber", "Address"]
domain_attributes.extend(new_attributes)

# Using append() to add a tuple
tuple_attribute = ("CampID", "CampName")
domain_attributes.append(tuple_attribute)

# Using insert() to add a set at a specific index
set_attribute = {"OrganizerName", "Location"}
domain_attributes.insert(2, set_attribute)

# Using extend() to add elements from a dictionary's keys
dict_attribute = {"DonationID": "1231", "DonorID": "100"}
domain_attributes.extend(dict_attribute.keys())

print(domain_attributes)

# 1.Write a program to swap the first and last elements in a list.
print("\n1.Write a program to swap the first and last elements in a list.\n")
num_lst = [10,21,11,40,30]

temp = num_lst[0]
num_lst[0] = num_lst[-1]
num_lst[-1] = temp

print(num_lst)

# 2. Write a program to find the sum of the digits in a list.
print("\n2. Write a program to find the sum of the digits in a list.\n")
sum = 0
for i in num_lst:
    sum += i
print(f"Sum of the digits in the list is:{sum}")

# 3. Write a program to find the smallest element in a list.
print("\n3. Write a program to find the smallest element in a list.\n")
def find_smallest_element(num_list):
    smallest = num_list[0]
    for num in num_list:
        if num < smallest:
            smallest = num
    return smallest

print("Original list of numbers:", num_lst)

smallest_element = find_smallest_element(num_lst)

print("Smallest element in the list:", smallest_element)

# 1. Sort the dictionaries in ascending order based on the Key of the dictionary.
print("\n1. Sort the dictionaries in ascending order based on the Key of the dictionary.\n")
def sort_dict_keys(dictionary):
    sorted_keys = sorted(dictionary.keys())
    return sorted_keys

my_dict = {'e': 2, 'h': 1, 'o': 4, 'l': 3}

sorted_keys = sort_dict_keys(my_dict)

for key in sorted_keys:
    print(f"{key}:{my_dict[key]}")

# 2. Create the dictionary with Numeric as Value in Key – Value pair and find the sum of all the values in the Dictionary
print("\n2. Create the dictionary with Numeric as Value in Key – Value pair and find the sum of all the values in the Dictionary\n")
def sum_of_values(dictionary):
    total_sum = 0
    for value in dictionary.values():
        total_sum += value
    return total_sum

# Create a dictionary with numeric values
numeric_dict = {
    "name": 11,
    "age": 29,
    "regno": 40,
    "dob": 54,
    "phno": 20,
}

print("Original dictionary:", numeric_dict)

total_value_sum = sum_of_values(numeric_dict)

print("Sum of all values in the dictionary:", total_value_sum)

# 3.Write a Python code to demonstrate the sorting in descending order of values with lambda function.
print("\n3.Write a Python code to demonstrate the sorting in descending order of values with lambda function.\n")
my_dict = {'bid': 5, 'volume': 10, 'date': 3, 'campid': 8, 'donor': 2}

# Sorting the dictionary in descending order of values using a lambda function
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

for key, value in sorted_dict.items():
    print(f'{key}: {value}')
