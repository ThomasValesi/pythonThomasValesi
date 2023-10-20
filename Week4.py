#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 08:57:04 2023

@author: thomasvalesi
"""
a="h"
numbers_list=[]
sum=0
while True :
    a=input("Entered values : ")
    
    if a=="":
        break

    a=int(a)
    numbers_list.append(a)
    sum=sum+a
    
taille=len(numbers_list)
m=sum/taille

print(numbers_list)
print(f'the mean is : {m}')




names=input("Enter all the name with a blank between each of one : ")
name_list=names.split(" ")

for i in range (len(name_list)):
    print(f'Hi {name_list[i]}')
    

atomes=input("Enter the atome : ")
atomes_list=atomes.split(" ")

numbers=input("how many atome in the molecule : ")
numbers_list=numbers.split(" ")
numbers_list_float=[float(num) for num in numbers_list]

    

mass=input("What is it mass : ")
mass_list=mass.split(" ")
mass_list_float=[float(m) for m in mass_list]
    
print(mass_list_float)
print(numbers_list_float)

total=0.0

for i in range (len(numbers_list_float)):
    total+=(numbers_list_float[i])*(mass_list_float[i])

print(total)



degree_max=int(input('Enter the maximum degree : '))

numbers=input("Enter all the coefficient min degree --> max degree : ")
numbers_list=numbers.split(" ")
numbers_list_float=[float(num) for num in numbers_list]
print(numbers_list_float)

x=float(input('Enter the value of x : '))

total=0.0

for i in range (degree_max):
    total=numbers_list_float[i]*x**i + total
    
print(f"the result of this polynom is : {total}")



##------------------------------------------------------------------------------



Dict = dict({1:'Geek', 2:'for', 3:'Geeks'})
print("\nDictionnarywhith the use of dict() : ")
print(Dict)


Dict ={1:'Geek', 2:'for', 3: {'A':'Welcome', 'B': 'To', 'C':'Geeks'}}
print(Dict)
print(Dict[3]['A'])

Country_capital = {
    'United states' : 'Washington'
    , 'France':'Paris'}
print(Country_capital['France'])
Country_capital['France']='Marseille'
print(Country_capital['France'])


keys = ['Ten', 'Twenty', 'Thirty']
values = [10,20,30]
Dict ={}
Dict1 ={}
for i in range(len(keys)):
    Dict[i]=keys[i]
    Dict1[i]=values[i]
print(Dict)
print(Dict1)


# Create a dictionary to store information about the first ten elements
elements = {
    "H": {"element": "Hydrogen", "atomic_number": 1, "melting_point": -259.16, "boiling_point": -252.87},
    "He": {"element": "Helium", "atomic_number": 2, "melting_point": -272.20, "boiling_point": -268.93},
    "Li": {"element": "Lithium", "atomic_number": 3, "melting_point": 180.54, "boiling_point": 1342.0},
    "Be": {"element": "Beryllium", "atomic_number": 4, "melting_point": 1287.0, "boiling_point": 2470.0},
    "B": {"element": "Boron", "atomic_number": 5, "melting_point": 2076.0, "boiling_point": 3927.0},
    "C": {"element": "Carbon", "atomic_number": 6, "melting_point": 3915.0, "boiling_point": 3915.0},
    "N": {"element": "Nitrogen", "atomic_number": 7, "melting_point": -210.0, "boiling_point": -195.8},
    "O": {"element": "Oxygen", "atomic_number": 8, "melting_point": -218.8, "boiling_point": -183.0},
    "F": {"element": "Fluorine", "atomic_number": 9, "melting_point": -219.7, "boiling_point": -188.1},
    "Ne": {"element": "Neon", "atomic_number": 10, "melting_point": -248.6, "boiling_point": -246.1}
}

def determine_state(symbol, temperature):
    element_info = elements.get(symbol)
    
    if element_info is None:
        return "Element not found"
    
    melting_point = element_info["melting_point"]
    boiling_point = element_info["boiling_point"]
    
    if temperature < melting_point:
        return "Solid"
    elif melting_point <= temperature <= boiling_point:
        return "Liquid"
    else:
        return "Gas"

# Input from the user
symbol = input("Enter the symbol of an element (e.g., H, He, Li): ")
temperature = float(input("Enter a temperature (in Celsius): "))

# Convert Celsius to Kelvin
temperature += 273.15

state = determine_state(symbol, temperature)

print(f"At {temperature} K, {elements[symbol]['element']} ({symbol}) is in the {state} state.")






