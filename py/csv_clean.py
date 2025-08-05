'''
Author: Daniel Mulligan
Date: Jun 12 2025
Description: This script cleans the CSV file created in csv_gen.py
File Name: csv_clean.py
Notes:
*/
'''

import numpy as np
import pandas as pd


target_num = 150

#defining a function to produce valid data rows
def generate_valid_rows(n, existing_ids):
    possible_ids = set(range(150)) - existing_ids
    new_ids = np.random.choice(list(possible_ids), size=n, replace=False)
    new_ages = np.random.randint(19, 51, size=n)
    
    base_study = np.random.uniform(1.0, 3.0, size=n)
    age_adjustment = ((new_ages - 25) / (50 - 25)) * 2  # Older = up to +2 hours
    study_hours = base_study + age_adjustment
    new_hours = np.clip(study_hours, 1, 6)
    
    base_marks = np.random.randint(0, 100, size=n)
    stuMark = base_marks + (new_hours * 6).astype(int)
    new_marks = np.clip(stuMark, 0, 129)
    

    base_time = np.random.randint(60, 180, size=n)
    stuTime = base_time - (stuMark / 130 * 40).astype(int)
    new_times = stuTime = np.clip(stuTime, 0, 179)
    
    new_percents = ((new_marks / 130) * 100).round(0).astype(int)
    return pd.DataFrame({
        'Student Number': new_ids,
        'Student Age': new_ages,
        'Average Study Hours': new_hours,
        'Student Mark': new_marks,
        'Percentage': new_percents,
        'Examination Time': new_times
    })

#Loading the data from original csv
df = pd.read_csv('student_examination.csv')

#Dropping the missing and duplicate values
df.dropna(inplace=True)
df.drop_duplicates(subset=['Student Number'], inplace=True)

#Filtering out the valid rows only
valid_df = df[
    (df['Student Mark'] != 0) &
    (df['Student Age'].between(19, 50)) &
    (df['Examination Time'] >= 60) &
    (df['Average Study Hours'] >= 1)
]

existing_ids = set(valid_df['Student Number'])

#Finding the number of rows needed to reach the target number of rows
rows_needed = target_num - len(valid_df)

#Generating the required number of rows
if rows_needed > 0:
    new_rows = generate_valid_rows(rows_needed, existing_ids)
    valid_df = pd.concat([valid_df, new_rows], ignore_index=True)

#exporting the new file with exactly 150 valid rows
valid_df.to_csv('student_examination_cleaned.csv', index=False)

print(f"Cleaned dataset ready with {len(valid_df)} students.")
print(valid_df.head())