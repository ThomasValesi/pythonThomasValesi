#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:34:39 2023

@author: thomasvalesi
"""

import numpy as np
import math

##S09_4 Convert Angstroms to Nanometers

angst = np.linspace(1.0, 5.0, 21)
nano = angst * 0.1
print("Angstroms:", angst)
print("Nanometers:", nano)

##S09_5 Table of values

arr = np.linspace(-1, 1, 6)
xo = 0
s = 0.3
arr2 = np.empty(6)

for i in range(6):
    arr2[i] = (1 / (math.sqrt(2 * math.pi))) * math.exp((-1/2) * ((arr[i] - xo)**2 / s**2))

arr_rounded = np.around(arr, 5)
arr2_rounded = np.around(arr2, 5)
print(arr_rounded)
print(arr2_rounded)
    

##S09_6 Sea temperature statistics

temp = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

temp_np = np.array(temp)
average = np.mean(temp_np)

coldest_month_idx = np.argmin(temp_np)
coldest_month = months[coldest_month_idx]
coldest_temp = temp_np[coldest_month_idx]

warmest_month_idx = np.argmax(temp_np)
warmest_month = months[warmest_month_idx]
warmest_temp = temp_np[warmest_month_idx]

print(f"The average {average:.1f} ºC.")
print(f"The coldest month : {coldest_month} temperature : {coldest_temp:.1f} ºC.")
print(f"The warmest month : {warmest_month} temperature : {warmest_temp:.1f} ºC.")


##S09_10 Exam grades

num_students = int(input("Enter the number of students: "))

theory = np.empty(num_students, dtype=float)
problem = np.empty(num_students, dtype=float)

for i in range(num_students):
    theory_ = float(input(f"Enter the theory mark for student {i + 1} (0 to 10): "))
    problem_ = float(input(f"Enter the problem mark for student {i + 1} (0 to 10): "))
    
    theory[i] = theory_
    problem[i] = problem_

total = 0.4 * theory + 0.6 * problem

table = np.column_stack((np.arange(num_students), theory, problem, total))

max_total = np.max(total)
min_total = np.min(total)
avg_total = np.mean(total)

max_grade_index = np.argmax(total)

print("\nTable:")
print("Index | Theory Mark | Problem Mark | Total Mark")
for row in table:
    print(f"{int(row[0]):5} | {row[1]:11.2f} | {row[2]:12.2f} | {row[3]:10.2f}")

print(f"\nMaximum Total Grade: {max_total:.2f}")
print(f"Minimum Total Grade: {min_total:.2f}")
print(f"Average Total Grade: {avg_total:.2f}")

print(f"Position of Maximum Total Grade: {max_grade_index}")

