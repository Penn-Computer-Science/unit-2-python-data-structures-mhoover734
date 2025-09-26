import pandas as pd
import random

fNames = ["Jim", "Joe", "Jeff", "Jeremy", "James", "Joneson", "Jeremiah", "Jacob", "Jack", "Jackson", "Jessa", "Jace", "Jacqueline", "Jill", "Jane", "Julian", "John", "Johnson", "Jones"]
lNames = ["Smith", "Jones", "Williams", "Brown", "Davis", "Miller", "Garcia", "Hoover", "Washington", "Wilson", "Demetrius", "Aria", "Benjamin", "Wyatt", "Doe", "Lincoln", "Franklin", "Ignatious", "Foregon", "Booth", "Gronk", "Grank", "Julianatious", "Jefferson", "Jackson", "Yang", "Aizagov", "Foglesong", "Pillion", "Marsh", "Toney", "Trevor"]
years = ["Freshman", "Sophomore", "Junior", "Senior", "Victory Lap"]
pathways = ["Early College", "Engineering", "Computer Science", "Business", "Marketing", "Early Childhood Education", "Culinary", "Criminal Justice", "Construction", "Bio Med"]
print(len(fNames)*len(lNames))
names = []
for i in range(500):
    while True:
        newName = f"{random.choice(fNames)} {random.choice(lNames)}"
        if not(newName in names):
            names.append(newName)
            break

data = {
    "Name": names,
    "Age": [random.randint(14, 19) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.5), 2) for _ in names],
    "Credits Completed": [random.randint(0, 60) for _ in names],
    "Year": [random.choice(years) for _ in names],
    "Pathway": [random.choice(pathways) for _ in names]
}

pennData = pd.DataFrame(data)

print(pennData)

pennData.to_csv('students_very_real_data.csv', index=False)