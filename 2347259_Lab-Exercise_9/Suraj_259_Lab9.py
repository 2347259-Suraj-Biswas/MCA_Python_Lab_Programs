# Q1. Write a program to distinguish between Array Indexing and Fancy Indexing.
import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Array: ",array1)

arr_indexing1 = array1[3]
arr_indexing2 = array1[1]


print("Array Indexing 1[3]:",arr_indexing1)
print("Array Indexing 2[1]:",arr_indexing2)   

fancy_indexing1 = array1[[1, 4, 5, 7]]
fancy_indexing2 = array1[[0,3]]

print("Fancy Indexing 1[[1, 4, 5, 7]]: ",fancy_indexing1) 
print("Fancy Indexing 2[[0,3]]: ",fancy_indexing2) 

# Q2. Execute the 2D array Slicing.
import numpy as np

arr1 = np.array([
    [2, 4, 6, 8], 
    [10, 20, 30, 40]
])
print("2D Array: ")
print(arr1)
print("\n2D Array Slicing: ")
arr_slicing = arr1[0:2, 0:3]
print(arr_slicing)

# Q3. Create the 5-Dimensional arrays using ‘ndmin’.
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print("\nArray: ")
print(arr1)
arr2 = np.array(arr1, ndmin=5)

print("\nArray shape using ndmin: ")
print(arr2.shape)

# Q4. Reshape the array from 1-D to 2-D array

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Array: ")
print(arr1)

# reshaping 1D to 2D array with 3 rows, 3 columns
reshape_1Darr = arr1.reshape((3, 3))

print(reshape_1Darr)

# Q5. Perform the Stack functions in Numpy arrays – Stack(), hstack(), vstack(), and dstack().

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nArray 'a': ")
print(a)

print("\nArray 'b': ")
print(b)

# 1. stack() Function:
c = np.stack([a, b])

print("\nArray using stack(): ")
print(c)

#2. hstack() Function:
d = np.hstack([a, b])

print("\nArray using hstack(): ")
print(d)

#3. vstack() Function
e = np.vstack([a, b])

print("\nArray using vstack(): ")
print(e)

#4. dstack() Function:
f = np.dstack([a, b])

print("\nArray using dstack(): ")
print(f)

# Q6. Perform the searchsort method in Numpy array.

import numpy as np

arr1 = np.array([1,2,4,5,8,9])
print("\nArray: ")
print(arr1)

arr2=[3,6,7]

print("\nArray using searchsorted():")
arr3 = np.searchsorted(arr1,arr2)
print(arr3)

# Q7. Create Numpy Structured array using your domain features.
import numpy as np

blood_bank = np.dtype([
('bank_id', 'int32'),
('bank_name', 'U50'), 
('blood_units', 'int32'),
('address', 'U100'),
])

bank_data = np.array([
(1, 'KBS',240,'SG_Palya'),
(2, 'Union',143,'Kormangla'),
(3, 'Sagar',111,'UB_City')
], dtype=blood_bank)

print("\nBlood Bank Structured Array:")
print(bank_data)

# Q8. Create Data frame using List and Dictionary.

import pandas as pd

data_list = [
    ['KBS Blood Bank', 'New York', 'AB+', 233],
    ['Union Blood Center', 'Los Angeles', 'O-', 150],
    ['Sagar Blood Bank', 'Chicago', 'A+', 100],
    ['Apollo Blood Center', 'San Francisco', 'B-', 50]
]

columns_list = ['Name', 'Location', 'Blood Type', 'Units Available']

df_list = pd.DataFrame(data_list, columns=columns_list)

data_dict = {
    'Name': ['KBS Blood Bank', 'Union Blood Center', 'Sagar Blood Bank', 'Apollo Blood Center'],
    'Location': ['New York', 'Los Angeles', 'Chicago', 'San Francisco'],
    'Blood Type': ['AB+', 'O-', 'A+', 'B-'],
    'Units Available': [233, 150, 100, 50]
}

df_dict = pd.DataFrame(data_dict)

print("Blood Bank DataFrame created using Lists:")
print(df_list)

print("\nBlood Bank DataFrame created using Dictionaries:")
print(df_dict)

# Q9. Create Data frame on your Domain area and perform the following operations to find and eliminate the
# missing data from the dataset.
# • isnull()
# • notnull()
# • dropna()
# • fillna()
# • replace()
# • interpolate()

import pandas as pd
import numpy as np

# Define the sample blood bank dataset
data = {
    'Donor_ID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Mary', 'David', 'Sarah', 'Michael'],
    'Age': [30, 25, 35, np.nan, 28],  # Adding missing age for one donor (np.nan represents a missing value)
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Blood_Type': ['A+', 'O-', 'B+', 'AB+', 'A-'],
    'Salary': [50000, 60000, 55000, 0, 48000],  # Adding a missing salary (0 represents a missing value)
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Check for missing data using isnull() and notnull()
print("Checking for missing data:")
print(df.isnull())
print(df.notnull())

# Drop rows with missing data using dropna()
df_cleaned = df.dropna()
print("\nData frame after dropping rows with missing data:")
print(df_cleaned)

# Fill missing data with a specific value using fillna()
df_filled = df.fillna({'Age': 0, 'Salary': 0})
print("\nData frame after filling missing data:")
print(df_filled)

# Replace specific values using replace()
df_replaced = df_filled.replace({'Gender': {'Male': 1, 'Female': 0}})
print("\nData frame after replacing values:")
print(df_replaced)

# Interpolate missing values using interpolate()
df_interpolated = df_filled.interpolate()
print("\nData frame after interpolating missing values:")
print(df_interpolated)


# Q10. Perform the Hierarchical Indexing in the above created dataset.

import pandas as pd

data = {
    'Blood Type': ['A+', 'B+', 'O+', 'A-', 'B-', 'O-'],
    'Donor Location': ['City 1', 'City 2', 'City 1', 'City 3', 'City 2', 'City 4'],
    'Donation Date': ['2023-01-05', '2023-02-12', '2023-03-20', '2023-04-10', '2023-05-15', '2023-06-08'],
    'Donor Name': ['Donor 1', 'Donor 2', 'Donor 3', 'Donor 4', 'Donor 5', 'Donor 6']
}

df = pd.DataFrame(data)

df.set_index(['Donor Location', 'Blood Type'], inplace=True)

print("DataFrame with Hierarchical Indexing:")
print(df)




