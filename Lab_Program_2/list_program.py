# 1.Create a LIST with your domain attributes, insert the elements using the append (), insert(), extend() 
# and add any iterables (tuples, sets, dictionaries etc.) to the list (Use all the methods ).
print(f"1. Program to create a LIST with your domain attributes, insert the elements using the append (), insert(), extend() and add any iterables to the list (Use all the methods ).")
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
num_lst = [10,21,11,40,30]

temp = num_lst[0]
num_lst[0] = num_lst[-1]
num_lst[-1] = temp

print(num_lst)
# 2. Write a program to find the sum of the digits in a list.
sum = 0
for i in num_lst:
    sum += i
print(f"Sum of the digits in the list is:{sum}")

# 3. Write a program to find the smallest element in a list.
def find_smallest_element(num_list):
    smallest = num_list[0]
    for num in num_list:
        if num < smallest:
            smallest = num
    return smallest

print("Original list of numbers:", num_lst)

smallest_element = find_smallest_element(num_lst)

print("Smallest element in the list:", smallest_element)
