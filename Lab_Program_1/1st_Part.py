#Write a paragraph about introducing you and your selected domain (include Full Name, domain name, register number, year …….).
about_data = """
Hi my name is Suraj Biswas , I am currently pursuing a PG course in MCA for the academic year 2023-2024 . 
My student regno is 2347259 . 
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
import re

element_data_types = {
    "name" : "string",
    "regno" : "int",
    "course" : "string",
    "year" : "int",
    "domain" : "string",
}

elements = re.findall(r'\b\w+\b', about_data)

for element in elements:
    if element in element_data_types:
        data_type = element_data_types[element]
        print(f"{element} - {data_type}")

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
