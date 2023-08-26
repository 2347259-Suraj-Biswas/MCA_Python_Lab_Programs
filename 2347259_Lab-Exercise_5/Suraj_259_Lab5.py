# Q1. Write a program to handle the exception of ZeroDivisionError.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

try:
    print("---Division by Zero Program---")
    result = num1 / num2
    print(f"Division of {num1} & {num2} = {result}")
except ZeroDivisionError:
    print("Invalid operation! Cannot divide by Zero. Divide by a valid number.")
finally:
    print("Divison Program exited.")

# Q2. Write a program to handle the exception of IndexError.

try:
    print("\n---IndexError Program---")
    lst = []
    num = int(input("Enter number of elements to enter in array: "))
    for i in range(0, num):
        elements = int(input())
        lst.append(elements)
    print(f"\nList of elements: {lst}")
    search_index = int(input("Enter an index to find: "))
    print(f"{lst[search_index]}")
except IndexError:
    print("Invalid Index provided. Index position does not exists. Please give valid index")
finally:
    print("Index program ended.")

