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
first_three_chars = domain_name1[0:3]   # Slice from index 0 to 2 (inclusive)
last_three_chars = domain_name1[-3:]    # Slice from the third-to-last character to the end
middle_chars = domain_name1[2:5]        # Slice from index 2 to 4 (inclusive)

# Negative slicing
second_to_last_char = domain_name1[-2]  # Accessing the second-to-last character

print("\nPositive Slicing:")
print("First Three Characters:", first_three_chars)
print("Last Three Characters:", last_three_chars)
print("Middle Characters:", middle_chars)

print("\nNegative Slicing:")
print("Second-to-Last Character:", second_to_last_char)

# Slicing with a step
alternate_chars = domain_name[::2]  # Starting from the first character, every second character

# Reversing the string using slicing
reversed_domain_name = domain_name[::-1]  # Using a step of -1 to reverse the string

print("\nSlicing with a Step:")
print("Alternate Characters:", alternate_chars)

print("\nReversed Domain Name:")
print("Reversed:", reversed_domain_name)
