'''
Author: Daniel Mulligan
Date: Jun 5 2025
Description: This script creates a CSV file with random values for analysis
File Name: csv_gen.py
Notes: 
*/
'''



import numpy as np
import pandas as pd


n = 150

stuNum = np.random.choice(range(150), size=n, replace=False)

stuAge = np.random.randint(19, 51, size=n)

#Base random component
base_study = np.random.uniform(1.0, 3.0, size=n)
#Age adjustment
age_adjustment = ((stuAge - 25) / (50 - 25)) * 2  # Older = up to +2 hours
#Add influence of age adjustment
study_hours = base_study + age_adjustment
# Clamp values to 1-5 range
avHours =  np.clip(study_hours, 0, 5)



#Base random component
base_marks = np.random.randint(0, 100, size=n)
#Add influence of study hours (scaled)
stuMark = base_marks + (avHours * 6).astype(int)  # Up to +30 extra marks
#Clamp values to 0–129 range
stuMark = np.clip(stuMark, 0, 129)

stuPercent = ((stuMark / 130) * 100).round(0).astype(int)

#Base random component
base_time = np.random.randint(60, 180, size=n)  # assume minimum time is 1 hour (60 mins)
#Subtract a factor of marks — students with high marks finish quicker
stuTime = base_time - (stuMark / 130 * 40).astype(int)  # subtract up to 40 mins
#Clamp time between 0 and 179
stuTime = np.clip(stuTime, 0, 179)



# Build DataFrame
df = pd.DataFrame({
    'Student Number': stuNum,
    'Student Age': stuAge,
    'Average Study Hours': avHours,
    'Student Mark': stuMark,
    'Percentage': stuPercent,
    'Examination Time': stuTime
})

# Export to CSV
df.to_csv("student_examination.csv", index=False)
