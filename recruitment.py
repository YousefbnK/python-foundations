skills = ["Python", "Design", "Presentation", "Leadership"]
cv = {}


cv['name'] = input("What is your name ?   ")
cv['age'] = int(input("How old are you ?   "))
cv['experience'] = int(input("How many years of experience do you have ?   "))
cv['skills'] = []

for skill in skills:
	print(skills.index(skill) +1, end='')
	print(". ", skill)

skill_1 = int(input("Choose a skill from the list by entering its number:  "))
skill_2 = int(input("Choose another skill from above by entering its number:  "))


print("Choose a skill from the list by entering its number: ", skill_1)
print("Choose another skill from above by entering its number: ", skill_2)

def user_entry(i, j):
	if i or j == "1":
		cv['skills'].append(skills[0])

	elif i or j == "4":
		cv['skills'].append(skills[3])

	else:
		cv['skills'].append(skills[skill_1, skill_2])

user_entry(skill_1, skill_2)


if (25 < cv['age'] < 40) and (cv['experience'] > 3):
	if "Python" in cv['skills']:
		print("You have been accepted,", cv['name'])

	else:
		print("Unfortunately", cv['name'], "you do not fit the criteria. We wish you success.")







	