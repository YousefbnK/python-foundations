from datetime import date

employees = []
managers = []

class Employee():
	def __init__(self, name, age, salary, employment_year):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_year = employment_year

	def get_working_years(self):
		return date.today().year - self.employment_year

	def __str__(self):
		return "name: {}, Age: {}, Salary: {}, Working Years: {}".format(self.name, self.age, self.salary, self.get_working_years())
		
class Manager(Employee):
	def __init__(self, name, age, salary, employment_year, bonus):
		super().__init__(name, age, salary, employment_year)
		self.bonus = bonus

	def get_bonus(self):
		return self.salary * self.bonus

	def __str__(self):
		return "Name: {}, Age: {}, Salary: {}, Working Years: {}, Bonus: {}".format(self.name, self.age, self.salary, self.get_working_years(), self.get_bonus())  


options = ["Show Employees", "Show Managers", "Add an Employee", "Add a Manager", "Exit"]

print("Welcome to HR Pro 2019")

stop = "no"

while stop == "no":

	print("Options:")

	for i in options:
		# print (options.index(i) +1, i)
		print(f"{options.index(i) +1}. {i}")

	user_input = int(input("What would you like to do?  "))

	if user_input == 1:
		for facts in employees:
			print(facts)

	elif user_input == 2:
		for facts in managers:
			print(facts)

	elif user_input == 3:
		name = input("Name: ")
		age = int(input("Age: "))
		salary = int(input("Salary: "))
		employment_year = int(input("Employment year: "))

		employees.append(Employee(name, age, salary, employment_year))
		print("Employee added successfully")

	elif user_input == 4:
		name = input("Name: ")
		age = int(input("Age: "))
		salary = int(input("Salary: "))
		employment_year = int(input("Employment year: "))
		bonus = float(input("Bonus Percentge: "))

		managers.append(Manager(name, age, salary, employment_year, bonus))
		print("Manager added successfully")

	elif user_input == 5:
		stop = "yes"
