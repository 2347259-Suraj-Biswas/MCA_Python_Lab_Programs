# 2. Write a Python program to implement the object-oriented concepts of multiple, 
# Multilevel and Hierarchical Inheritances using your domain applications.

# Python program to demonstrate
# multiple inheritance
# Base class1
class Donor:
	donorname = ""
	def donor(self):
		print(self.donorname)

# Base class2
class Staff:
	staffname = ""
	def staff(self):
		print(self.staffname)

# Derived class
class BloodBank(Donor, Staff):
	def display(self):
		print("Donor Name:", self.donorname)
		print("Staff Name:", self.staffname)
		print("\n")

s1 = BloodBank()
s1.staffname = "Ram"
s1.donorname = "Suraj"
s1.display()

# Python program to demonstrate
# multilevel inheritance
# Base class
class BloodBank:
	def __init__(self, placename):
		self.placename = placename

# Intermediate class
class Donor(BloodBank):
	def __init__(self, donorname, placename):
		self.donorname = donorname

		BloodBank.__init__(self, placename)

# Derived class
class BloodGroup(Donor):
	def __init__(self, bloodgroup, donorname, placename):
		self.bloodgroup = bloodgroup

		Donor.__init__(self, donorname, placename)

	def print_name(self):
		print('Place name :', self.placename)
		print("Donor name :", self.donorname)
		print("Blood Group :", self.bloodgroup)


s1 = BloodGroup('O+ve', 'Suraj', 'Port Blair')
s1.print_name()
print("\n")

# Python program to demonstrate
# Hierarchical inheritance
# Base class
class BloodBank:
	def func1(self):
		print("The function is inside BloodBank class")

# Derived class1
class Donor1(BloodBank):
	def func2(self):
		print("This is Donor 1.")

# Derivied class2
class Donor2(BloodBank):
	def func3(self):
		print("This is Donor 2.")


Donor1 = Donor1()
Donor2 = Donor2()

Donor1.func1()
Donor1.func2()
Donor2.func3()
