#Write a paragraph about introducing you and your selected domain (include Full Name, domain name, register number, year …….).
name = "Suraj Biswas"
course = "MCA"
regno = 2347259
year = 2023
domain = "Blood Bank Management System"
about_data = f"""
Hi my name is {name} , I am currently pursuing a PG course in {course} for the academic year {year}-2024 . 
My student regno is {regno} . 
As part of my postgraduate studies , I have chosen the domain of Blood Bank Management System . 
The primary objective of this system is to streamline and enhance the operations of blood banks by incorporating efficient data management ,  
donor and recipient information tracking , inventory management , and real-time availability updates . 
This system proves to be immensely beneficial as it optimizes the process of blood collection , storage , and distribution , 
ensuring timely access to blood units for medical emergencies , thus potentially saving lives .
"""

# Write a python program to count the frequency of any specific word (in your domain) in the paragraph.
print("\n1. Write a python program to count the frequency of any specific word (in your domain) in the paragraph:\n")
def word_occurence_count(about_data, search_word):
    words = about_data.lower().split()
    word_count = 0
    for word in words:
        if word == search_word.lower():
            word_count +=1
    return word_count

search_word = "blood"

frequency = word_occurence_count(about_data,search_word)
print(f"The word '{search_word}' appears {frequency} times in the paragraph.")

# Write a python program to display all the datatypes of selected specific elements in the paragraph. 
# (For example:– name - string, reg.no - int, marks - float, etc.)

print("\n2. Write a python program to display all the datatypes of selected specific elements in the paragraph.\n")
print(f"""
Name : {type(name)}
Course : {type(course)}
Regno : {type(regno)}
Year : {type(year)}
Domain : {type(domain)}
""")


# Write a python program to count the number of alphabets, numeric and other special symbols in the paragraph.
print("\n3. Write a python program to count the number of alphabets, numeric and other special symbols in the paragraph:\n")
def count_alpha_num_special(about_data):
    alphabets = numerics = specials = 0

    for char in about_data:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            alphabets += 1
        elif '0' <= char <= '9':
            numerics += 1
        elif not char.isspace():
            specials += 1

    return alphabets, numerics, specials

# Count symbols in the paragraph
alpha_count, numeric_count, special_count = count_alpha_num_special(about_data)

print(f"Alphabets: {alpha_count}")
print(f"Numeric characters: {numeric_count}")
print(f"Special symbols: {special_count}")

# 1. Create a Set with elements that consists of various data types (int, float, string, Boolean, etc. from your domain)
#  and perform the functions pop(), clear(), discard() and del. Write the insights as docstring.
print("\n1.Create a Set with elements that consists of various data types and perform the functions pop(), clear(), discard() and del.\n")
def manipulate_set():
    """
    This Python script demonstrates the usage of different set operations on a set containing elements of various data types.

    Insights:
    - Sets are unordered collections of unique elements, and they support various useful operations.
    - The `pop()` function removes and returns an arbitrary element from the set.
    - The `clear()` function removes all elements from the set, making it empty.
    - The `discard()` function removes a specified element from the set if it exists, and does nothing if the element is not present.
    - The `del` statement deletes the entire set.
    """

    mixed_set = {("donorid","112", "blood-group","O+ve"), 23.5, "Suraj", True, "Male",9328164536, "23-08-1999",("port","blair")}

    #original set
    print(f"Original Set: {mixed_set}")
    # Demonstrate the usage of pop()
    popped_element = mixed_set.pop() 
    print("Updated Set:", mixed_set)

    # Demonstrate the usage of clear()
    mixed_set.clear() 
    print("Cleared Set:", mixed_set)

    # Recreating the set 
    mixed_set = {("donorid","112", "blood-group","O+ve"), 23, "Suraj", True, "Male",9328164536, "23-08-1999",("port","blair")}

    # Demonstrate the usage of discard()
    mixed_set.discard("Male")  
    print("Set after Discarding:", mixed_set)

    # Demonstrate the usage of del
    del mixed_set 

    try:
        print("Set after using del:", mixed_set)
    except NameError:
        print("Set no longer exists.")

manipulate_set()

# 2.Update the Set with minimum 5 string attributes of your domain and arrange the Set in descending order.

print("\n2.Update the Set with minimum 5 string attributes of your domain and arrange the Set in descending order.\n")
# Creating a set with string attributes from my domain Blood Bank Management System
donor_set = {"FirstName", "LastName", "Gender","BloodGroup","ContactNumber","Email","Address"}

descending_list = sorted(donor_set,reverse=True)

print("Original Set:", donor_set)
print("Set in Descending Order:", descending_list)

# 3.Create a Tuple and Execute the packing and unpacking operations of tuples using the attributes of your domain.
print("\n3.Create a Tuple and Execute the packing and unpacking operations of tuples using the attributes of your domain.\n")
donor_tuple = ("Suraj","Biswas","Male","O+ve","3213453211","suraj@gmail.com","port blair")
FirstName ,LastName, Gender, BloodGroup, ContactNumber, Email, Address = donor_tuple

print(f"""
FirstName: {FirstName}
LastName: {LastName}
Gender: {Gender}
BloodGroup: {BloodGroup} 
ContactNumber: {ContactNumber}
Email: {Email}
Address: {Address}
""")

# 4.Enter your domain name as characters and count any number of characters and print the count (for example – 
# (‘p’,’r’,’o’,’g’,’r’,’a’,’m’) count of ‘r’ = 2)
print("4.Enter your domain name as characters and count any number of characters and print the count")
domain_name = ('b','l','o','o','d','b','a','n','k','m','a','n','a','g','e','m','e','n','t','s','y','s','t','e','m')
search_char = 'm'
count = 0
for char in domain_name:
    if char == search_char:
        count += 1
print(f"Count of '{search_char}' = {count}")

# 5.Enter your domain name, execute all the slicing possibilities and also negative indexing.
print("\n5.Enter your domain name, execute all the slicing possibilities and also negative indexing.\n")
domain_name1 = "Blood Bank Management System"
print(f"Domain Name: {domain_name1}")
# Positive slicing
first_three_chars = domain_name1[0:3]  
last_three_chars = domain_name1[-3:]   
middle_chars = domain_name1[2:5]       

# Negative slicing
second_to_last_char = domain_name1[-2] 

print("\nPositive Slicing:")
print("First Three Characters:", first_three_chars)
print("Last Three Characters:", last_three_chars)
print("Middle Characters:", middle_chars)

print("\nNegative Slicing:")
print("Second-to-Last Character:", second_to_last_char)

# Slicing with a step
alternate_chars = domain_name[::2]  

# Reversing the string using slicing
reversed_domain_name = domain_name[::-1] 

print("\nSlicing with a Step:")
print("Alternate Characters:", alternate_chars)

print("\nReversed Domain Name:")
print("Reversed:", reversed_domain_name)
