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


cv['skills'].append(skills[skill_1 - 1])
cv['skills'].append(skills[skill_2 - 1])


if (25 < cv['age'] < 40) and (cv['experience'] > 3):
	if "Python" in cv['skills']:
		print("You have been accepted,", cv['name'])

	else:
		print("Unfortunately", cv['name'], "you do not fit the criteria. We wish you success.")







	