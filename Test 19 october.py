#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 12:46:16 2023

@author: thomasvalesi
"""

import numpy as np
import matplotlib.pyplot as plt

##Exercice 1

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

list3=[]

for i in list1:
    if(i%2==0):
        list3.append(i)

for i in list2:
    if(i%2!=0):
        list3.append(i)
        
print(list3)



##Exercice 2
list1=[]

for i in range(-100,100,1):
    if(i**2-5*i+6==0):
        list1.append(i)
print(list1)
        

x=np.linspace(-5,5,100)
plt.title("x^2 - 5x +6")
plt.xlabel("X")
plt.ylabel("Y")   
y=x**2-5*x+6

plt.plot(x,y)

plt.legend()
plt.show()


##Exercice 3

h=float(input("Enthe the hypothenus lenght : "))
a=float(input("Enthe the side 1 lenght : "))
b=float(input("Enthe the side 2 lenght : "))

if(h**2==a**2+b**2):
    print("It's a right angle triangle")
elif(h**2<a**2+b**2):
    
    print("It's a acute angle triangle")
    
    if(h==a and h==b):
        print("And its an equilateral tringle")
    elif(a==b):
        print("And its an isocele tringle")
    else:
        print("And its an scalene tringle")  
    
else:
    print("It's a obtuse angle triangle")
    


##Exercice 4

nb1=int(input("saisir un nombre : "))
nb2=int(input("saisir un nombre : "))
tot1=0
for i in range(1,nb1-1):
    if(nb1%i==0):
        tot1=tot1+i


if(tot1==nb2):
    print(f'{nb1} and {nb2} are friends')
else:
    print(f'{nb1} and {nb2} are not friends')


##Exercice 5

x=100000000

for i in range(5):
    x=x*1.06
    
print(f"The total is : {x} €")


##Exercice 6

list1 = [1, 3, 5, 7, 9]
list2 = [2, 3, 4, 6, 8, 9]

list3=[]

for i in list1:
    for j in list2:
        if(i==j):
            list3.append(i)
            
print(list3)


##Exercice 7

nb=int(input('entrer un nombre : '))
tot=0
for i in range(1,nb-1):
    if(nb%i==0):
        tot=tot+i
if(nb==tot):
    print('the number is perfect')
else:
    print('the number is not perfect')

##Exercice 9

x=np.linspace(-5,5,100)
plt.title("F(X) and G(X)")
plt.xlabel("X")
plt.ylabel("Y") 
 
y=x**2-2*x+1
plt.plot(x,y,label="F(X)")

y2=3*x+5
plt.plot(x,y2,label="G(X)")

plt.legend()
plt.show()
plt.savefig("fonction.png")


##Exercice 11

nb=int(input('Enter a number : '))
list1=[]

for i in range(1000):
    a=0
    for j in range(1,1000):
        if(i%j==0):
            a=a+1
    if(a==2):
        list1.append(i)

print("The list of prime is : ")

for i in range(0,nb):
    print(list1[i])
    
    
##Exercice 12

print()
print()
name=input("Entrer votre nom : ")
number=input("Entrer votre numéro d'employé' : ")
number_hours=float(input("Entrer votre nombre d'heures travailler cette semaine : "))
hourly_rate=float(input("Entrer votre salaire à l'heure : "))
standard_tax=float(input("Entrer la taxe standard : "))
overtime_tax=float(input("Entrer la taxe des heures sup : "))
print()
print()

hourly_overtime=hourly_rate*1.5
nb_hours_normal=0
nb_hours_overtime=0
total_hours_normal=0
total_hours_overtime=0
deduction_normal=t=0
deduction_overtime=0
total_pay=0
total_deduction=0
net_pay=0

if(number_hours>=37.5):
    nb_hours_normal=37.5
    nb_hours_overtime=number_hours-nb_hours_normal
    
    total_hours_normal=nb_hours_normal*hourly_rate
    total_hours_overtime=(number_hours-nb_hours_normal)*hourly_overtime
    
    deduction_normal=total_hours_normal*standard_tax
    deduction_overtime=total_hours_overtime*overtime_tax
    
    total_pay=total_hours_normal+total_hours_overtime
    
    total_deduction=deduction_normal+deduction_overtime
    
    net_pay=total_pay-total_deduction
    
else:
    nb_hours_normal=number_hours
    
    total_hours_normal=number_hours*hourly_rate
    
    deduction_normal=total_hours_normal*standard_tax
    
    total_pay=total_hours_normal
    
    total_deduction=deduction_normal
    
    net_pay=total_pay-total_deduction
    


print(f'Employé : {name}')
print(f"Numéro d'employé : {number}")
print()
print()

print(f"Normal :     heure : {nb_hours_normal}    salaire à l'heure : {hourly_rate}     Total : {total_hours_normal}  tax : {standard_tax}     deduction : {deduction_normal}")

print(f"heures sup : heure : {nb_hours_overtime}    salaire à l'heure : {hourly_overtime}     Total : {total_hours_overtime}  tax : {overtime_tax}     deduction : {deduction_overtime}")

print(f"Salaire brut : {total_pay}")
print(f"Total déduction : {total_deduction}")
print(f"Salaire net : {net_pay}")










































