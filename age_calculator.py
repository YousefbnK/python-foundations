from datetime import date

def check_birthdate(year, month, day):
	today = date.today()
	if today.year - year < 1:
		return False
	else:
		return True

def calculate_age(year, month, day):
	today = date.today()
	age = today.year - year

	print(age, "years")

year = int(input("What year were you born ?   "))
month = int(input("What month were you born ?   "))
day = int(input("What day were you born ?   "))

if check_birthdate(year, month, day) is True:
	calculate_age(year, month, day)
else:
	print("Birthdate invalid")