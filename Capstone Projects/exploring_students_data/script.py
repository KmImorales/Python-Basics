# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Add the path to the external folder
external_folder_path = os.path.abspath('../Capstone Projects/data_utils')
sys.path.append(external_folder_path)

# Import the function from the external file
from __init__ import process_dataset

# Import data
file_path = '../Capstone Projects/exploring_students_data/students.csv'

#Call function to process dataset from _data_functions
process_dataset(file_path, delimiter=';', categorical_threshold=0.1)

students = pd.read_csv(file_path)

# Print first few rows of data
print(students.head(5))

# Print summary statistics for all columns
print(students.describe(include='all'))

# Transform all numeric columns to categorical

#Grades database
# all_grades = students['G1'] + students['G2'] + students['G3']

# Calculate mean
# mean_math = all_grades.mean()

# # Calculate median
# median_math = all_grades.median()

# # Calculate mode
# mode_math = all_grades.mode()

# # Calculate range
# range_math = all_grades.max() - all_grades.min()

# # Calculate standard deviation
# std_math = all_grades.std()

# # Calculate MAD
# mad_math = all_grades.mad()

# # Create a histogram of math grades
# hist_math = plt.hist(students['math'], bins=20)

# plt.show()
# plt.clf()

# # Create a box plot of math grades
# box_math = plt.boxplot(students['math'])

# plt.show()
# plt.clf()

# # Calculate number of students with mothers in each job category
# mothers_jobs = students['Mjob'].value_counts()

# # Calculate proportion of students with mothers in each job category
# mothers_jobs_prop = students['Mjob'].value_counts(normalize=True)

# # Create bar chart of Mjob
# bar_for_mjob = plt.bar(mothers_jobs.index, mothers_jobs)

# plt.show()
# plt.clf()

# # Create pie chart of Mjob
# pie_for_mjob = plt.pie(mothers_jobs, labels=mothers_jobs.index)

# plt.show()