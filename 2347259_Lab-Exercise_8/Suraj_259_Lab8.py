# Q1. Download the Titanic dataset and perform the Exploratory data analysis using pandas.
# Read the dataset (df= pd.read_csv(r'………………………….\Titanic.csv')
# Display the first and last 10 instances from the dataset
# Acquire the necessary information using the df.info() and df. Describe().
# Retrieve the number of columns and rows. (using shape)

import pandas as pd

df = pd.read_csv(r'Titanic.csv');

print("----------First 10 instances:----------")
print(df.head(10))

print("\n----------Last 10 instances:----------")
print(df.tail(10))

print("\n----------Summary of the DataSet----------")
print(df.info())

print("\n----------Describing the DataSet---------")
print(df.describe())

num_rows , num_columns = df.shape
print(f"\nNo. of Rows: {num_rows}")
print(f"No. of columns: {num_columns}")

# Q2. Create the data visualization using the matplotlib.
# Visualize the Gender of Passengers using the Bar graph.
# Visualize the Survival Count of Passengers using the Bar graph.
# Visualize the Age of Passengers using the Bar/Histogram graph.
# Visualize the comparison of Age and Fare of Passengers using the Scatterplot.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"Titanic.csv")

#Visualize the Gender of Passengers using the Bar graph.
gender_count = df['Sex'].value_counts()

plt.figure(figsize=(5, 6))
plt.bar(gender_count.index, gender_count.values, color = 'Green')
plt.title('GENDER OF THE PASSENGERS')
plt.xlabel('SEX')
plt.ylabel('COUNT')
plt.show()

#Visualize the Survival Count of Passengers using the Bar graph.
survival_count = df['Survived'].value_counts()

plt.figure(figsize=(5, 6))
plt.bar(survival_count.index, survival_count.values)
plt.title('SURVIVAL COUNT OF THE PASSENGERS')
plt.xlabel('SURVIVED')
plt.ylabel('COUNT')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()

# Visualize the Age of Passengers using the Bar/Histogram graph.

plt.figure(figsize=(10, 6))
plt.hist(df['Age'].dropna(), bins=20, edgecolor='black', color='orange')
plt.title('AGE DISTRIBUTION OF THE PASSENGERS')
plt.xlabel('AGE')
plt.ylabel('COUNT')
plt.show()

# Visualize the comparison of Age and Fare of Passengers using the Scatterplot.
plt.figure(figsize=(15, 6))
plt.scatter(df['Age'], df['Fare'], alpha=0.5)
plt.title('AGE & FARE COMPARISON OF THE PASSENGERS')
plt.xlabel('AGE')
plt.ylabel('FARE')
plt.show()



