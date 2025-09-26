import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random as rng

# Literally js a linebreak
lineBreak = "-_"*50

# Load our dataframe:
df = pd.read_csv('students_very_real_data.csv')
pennData = pd.DataFrame(df)


# First five lines of the dataframe
print(f"\n{lineBreak}\n\nHead of the Dataframe\n")
print(pennData.head())

# Last five lines of the dataframe
print(f"\n{lineBreak}\n\nTail of the Dataframe\n")
print(pennData.tail())

# Summary of the dataframe
print(f"\n{lineBreak}\n\nSummary of the Dataframe\n")
print(pennData.info())

# Statistical Analysis of the dataframe
print(f"\n{lineBreak}\n\nStatistics of the Dataframe\n")
print(round(pennData.describe()))

# Counts of students in pathways in the dataframe
print(f"\n{lineBreak}\n\nCounts of students in pathways\n")
print(pennData["Pathway"].value_counts())

# Average GPS per year in the dataframe
print(f"\n{lineBreak}\n\nAverage GPA per year\n")
print(pennData.groupby("Year")["GPA"].mean())

# Top 3 GPA students in the dataframe
print(f"\n{lineBreak}\n\nTop 3 students by GPA\n")
print(pennData.sort_values(by="GPA", ascending=False).head(3))

# 3.5+ GPA students in the dataframe
print(f"\n{lineBreak}\n\nStudents with GPA > 3.5\n")
print(pennData[pennData["GPA"]>3.5])

# Data of first student in the dataframe
print(f"\n{lineBreak}\n\nFirst Student Data\n")
print(pennData.iloc[0])