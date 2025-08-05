'''
Author: Daniel Mulligan
Date: Jun 12 2025
Description: This script uses the CSV file to create frequency tables, graphs and charts for analysis.
File Name: ft_graphs.py
Notes:
*/
'''

import pandas as pd
import matplotlib.pyplot as plt

#Loading the cleaned data from the previous csv file
df = pd.read_csv('student_examination_cleaned.csv')

#Creating a frequency table for the study hours
study_hours_freq = {'1–2': 0, '2–3': 0, '4–5': 0}

for hour in df['Average Study Hours']:
    if 1 <= hour <= 2:
        study_hours_freq['1–2'] += 1
    elif 2 < hour < 4:
        study_hours_freq['2–3'] += 1
    elif 4 <= hour <= 5:
        study_hours_freq['4–5'] += 1 

#Converting to DataFrame for viewing
study_hours_df = pd.DataFrame(list(study_hours_freq.items()), columns=['Study Hour Range', 'Frequency'])

plt.figure(figsize=(4, 2))
plt.axis('off')
plt.title("Frequency Table: Average Study Hours")
table = plt.table(cellText=study_hours_df.values, colLabels=study_hours_df.columns, loc='center', cellLoc='center')
table.scale(1, 1.5)
plt.tight_layout()
plt.show()

#Creating a frequency table for the student ages
age_group_freq = {'18–25': 0, '25–35': 0, '35–45': 0, 'Over 45': 0}

for age in df['Student Age']:
    if 18 <= age < 25:
        age_group_freq['18–25'] += 1
    elif 25 <= age < 35:
        age_group_freq['25–35'] += 1
    elif 35 <= age < 45:
        age_group_freq['35–45'] += 1
    elif age >= 45:
        age_group_freq['Over 45'] += 1

#Converting to DataFrame for viewing
age_group_df = pd.DataFrame(list(age_group_freq.items()), columns=['Age Group', 'Frequency'])

#Plotting Age Group Table
plt.figure(figsize=(4, 2))
plt.axis('off')
plt.title("Frequency Table: Student Age Groups")
table = plt.table(cellText=age_group_df.values, colLabels=age_group_df.columns, loc='center', cellLoc='center')
table.scale(1, 1.5)
plt.tight_layout()
plt.show()


#Creating a frequency table for the student marks
bin_edges = [0, 20, 30, 40, 50, 60, 70, 80, 90, 100]
bin_labels = ['0-20%', '21-30%', '31-40%', '41-50%', '51-60%', '61-70%', '71-80%', '81-90%', '91-100%']

#Converting the marks to percentages
df['Percent'] = (df['Student Mark'] / 130 * 100).round(0)

#Binning the percentages
df['Percent Bin'] = pd.cut(df['Percent'], bins=bin_edges, labels=bin_labels, right=True, include_lowest=True)

#Counting frequency per bin
marks_freq = df['Percent Bin'].value_counts().sort_index()

#Converting to dictionary 
marks_freq_dict = marks_freq.to_dict()

#Converting marks_freq_dict to DataFrame
marks_df = pd.DataFrame(list(marks_freq_dict.items()), columns=['Mark Bin', 'Frequency'])

#Defining the bin label order for sorting
bin_order = ['0-20%', '21-30%', '31-40%', '41-50%', '51-60%', '61-70%', '71-80%', '81-90%', '91-100%']

#Sorting the DataFrame using the defined order
marks_df['Mark Bin'] = pd.Categorical(marks_df['Mark Bin'], categories=bin_order, ordered=True)
marks_df = marks_df.sort_values(by='Mark Bin')

#Plotting marks table
plt.figure(figsize=(6, 4))
plt.axis('off')
plt.title("Frequency Table: Student Marks (High to Low)")
table = plt.table(cellText=marks_df.values, colLabels=marks_df.columns, loc='center', cellLoc='center')
table.scale(1, 1.5)
plt.tight_layout()
plt.show()

#Plotting the student count by age group
plt.figure(figsize=(8, 5))
plt.bar(age_group_freq.keys(), age_group_freq.values(), color='skyblue')
plt.xlabel('Student Age Groups')
plt.ylabel('Number of Students')
plt.title('Student Count by Age Group')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

#Creating aa function to sort the student ages into groups
def classify_hour(hour):
    if 1 <= hour <= 2:
        return '1–2'
    elif 2 < hour < 4:
        return '2–3'
    elif 4 <= hour <= 5:
        return '4–5'

df['Study Hour Group'] = df['Average Study Hours'].apply(classify_hour)

#Dropping the rows where the group is none 
filtered_df = df.dropna(subset=['Study Hour Group'])

#Grouped and calculated the average student mark per group
grouped_df = filtered_df.groupby('Study Hour Group', as_index=False)['Student Mark'].mean()

#Sorted the groups into the desired order
grouped_df['Sort Order'] = grouped_df['Study Hour Group'].map({'1–2': 1, '2–3': 2, '4–5': 3})

grouped_df = grouped_df.sort_values('Sort Order')

#Plotting the average student mark by study time
plt.figure(figsize=(8, 5))
plt.plot(grouped_df['Study Hour Group'], grouped_df['Student Mark'], marker='o', linestyle='-', color='red')

plt.xlabel('Study Hours (Grouped)')
plt.ylabel('Average Student Mark')
plt.title('Average Student Mark by Study Time')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#Plotting the student mark vs the exam duration
plt.figure(figsize=(8, 5))
plt.scatter(df['Examination Time'], df['Student Mark'], color='green', alpha=0.4)
plt.xlabel('Time Taken on Exam (minutes)')
plt.ylabel('Student Mark')
plt.title('Student Marks vs. Exam Duration')
plt.grid(True)
plt.tight_layout()
plt.show()

#Plotting the study time vs the students age
plt.figure(figsize=(8, 5))
plt.scatter(df['Average Study Hours'], df['Student Age'], color='orange', alpha=0.4)
plt.xlabel('Average Study Hours (Time on Campus)')
plt.ylabel('Student Age')
plt.title('Study Time vs. Student Age')
plt.grid(True)
plt.tight_layout()
plt.show()