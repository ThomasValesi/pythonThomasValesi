#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:22:25 2023

@author: thomasvalesi
"""

message='Good Morning'
print(message)
print(len(message))
print(message[3])
print(message[5:8])
print(message.upper())
print(message.lower())
print(message.count('o'))
print(message.find('o'))
message=message.replace('Morning', 'Afternoon')
print(message)
print(dir(str))
print(dir(int))

num = input("Enter an integer : ")
num = int(num)

if(num>5) :
    print('the number is higher than 5')
else : 
    print('the number is lower than 5')
    

note = int(input("Entrez votre note sur 100 : "))

if note >= 90:
    grade = "A"
elif note >= 80:
    grade = "B"
elif note >= 70:
    grade = "C"
elif note >= 60:
    grade = "D"
elif note >= 50:
    grade = "E"
else:
    grade = "F"

# Affichez la note attribuée
print(f"Votre note est {grade}")


heigth = float(input("enter your height in m : "))
weigth = float(input("enter your weigth in kg : "))
bmi = (weigth)/(heigth**2)

if(bmi<18.5) : 
    print("underweigth : ")
    print(bmi)
    
elif(18.5<=bmi<=25) :
    print("normal weigth : ")
    print(bmi)
    
elif(25<bmi<=30) :
    print("overweigth : ")
    print(bmi)
    
elif(bmi>30) :
    print("obesity : ")
    print(bmi)
    
    
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

while True:
    print("Choisissez une option:")
    print("1. Celsius vers Fahrenheit")
    print("2. Celsius vers Kelvin")
    print("3. Fahrenheit vers Celsius")
    print("4. Fahrenheit vers Kelvin")
    print("5. Kelvin vers Celsius")
    print("6. Kelvin vers Fahrenheit")
    print("7. Quitter")
    
    choix = input("Entrez le numéro de l'option souhaitée : ")
    
    if choix == "7":
        print("Au revoir!")
        break
    
    valeur = float(input("Entrez la température à convertir : "))
    
    if choix == "1":
        resultat = celsius_to_fahrenheit(valeur)
        print(f"{valeur} Celsius équivaut à {resultat} Fahrenheit")
    elif choix == "2":
        resultat = celsius_to_kelvin(valeur)
        print(f"{valeur} Celsius équivaut à {resultat} Kelvin")
    elif choix == "3":
        resultat = fahrenheit_to_celsius(valeur)
        print(f"{valeur} Fahrenheit équivaut à {resultat} Celsius")
    elif choix == "4":
        resultat = fahrenheit_to_kelvin(valeur)
        print(f"{valeur} Fahrenheit équivaut à {resultat} Kelvin")
    elif choix == "5":
        resultat = kelvin_to_celsius(valeur)
        print(f"{valeur} Kelvin équivaut à {resultat} Celsius")
    elif choix == "6":
        resultat = kelvin_to_fahrenheit(valeur)
        print(f"{valeur} Kelvin équivaut à {resultat} Fahrenheit")
    else:
        print("Option invalide. Veuillez entrer un numéro entre 1 et 7.")
        
        

n1 = int(input("enter a number :  "))
n2 = int(input("enter a differient number : "))

if(n1%n2==0) :
    print("n1 is divisible by n2")
    print(n1/n2)
elif(n1%n2!=0) :
    print("n1 is not divisible by n2")
    print(n1//n2, n1%n2)
    

a = int(input("enter nb unit"))
price=0

if(a<=100) :
    print("no charge")
    
elif(100<a<200) :
    price = (a-100)*5
    print("the price is ")
    print(price)
    
elif(a>=200) : 
    price = 100*5 + (a-200)*10
    print("the price is ")
    print(price)
    





while num>0 :
    res = num//3
    print("the integer division of {} by 3 is {} ".format(num,res))
    num = int(input("Enter a integer value : "))    

print("we are done")
num=550
compt = 0
while num>0 :
    res = num//3
    compt = compt +1

print("we are done")
print(compt)
num=550
compt = 0
while num>=0 :
    res = num//3
    compt = compt +1

print("we are done")
print(compt)
num=550
compt = 0
while num>3 :
    res = num//3
    compt = compt +1

print("we are done")
print(compt)
num=550
compt = 0
while num>3 :
    num = num//3
    compt = compt +1

print("we are done")
print(compt)
num=550
compt = 0
while num>0 :
    num = num//3
    compt = compt +1

print("we are done")
print(compt)
num = int(input("Enter a integer value : "))    
compt = 0
while num>0 :
    res = num//3
    print("the integer division of {} by 3 is {} ".format(num,res))
    num = int(input("Enter a integer value : "))   
    compt = compt +1

print("we are done")
print(compt)
num = int(input("Enter a integer value : "))    
ndiv=1

while ndiv<num:
    res=num//ndiv
    print("the integer division of {} by {} is {} ".format(num, ndiv, res))
    ndiv=ndiv+1

print("we are done")
print("total number of division : {}".format(ndiv))
num = int(input("Enter a integer value : "))    
ndiv=1

while ndiv<num:
    res=num//ndiv
    print("the integer division of {} by {} is {} ".format(num, ndiv, res))
    ndiv+=1

print("we are done")
print("total number of division : {}".format(ndiv))
num=1
ndiv=0
while num>0 and num<211:
    if num%3==0:
        print("the number is{}".format(num))
        ndiv = ndiv +1
    num=num+1

print("total number of iteration : {}".format(ndiv))
print("we are done")
num=1
ndiv=0
while num>0 and num<211:
    if num%3==0:
        print("the number is {}".format(num))
        ndiv = ndiv +1
    num=num+1

print("total number of iteration : {}".format(ndiv))
print("we are done")
num=int(input(print("Enter number")))
compt=0

while compte<10:
    res=res+num
    num=int(input(print("Enter number")))
    compt=compt+1

moy=res//compte
print("moy")
num=int(input("Enter number"))
compt=0

while compt<10:
    res=res+num
    num=int(input("Enter number"))
    compt=compt+1

moy=res//compt
print("moy")
num=int(input("Enter number"))
compt=0

while compt<9:
    res=res+num
    num=int(input("Enter number"))
    compt=compt+1

moy=res//compt
print(moy)
num=int(input("Enter number"))
compt=0
res=0

while compt<9:
    res=res+num
    num=int(input("Enter number"))
    compt=compt+1

moy=res//compt
print(moy)
i=1
while i<=4:
    print"*"*i
    i=i+1
i=1
while i<=4:
    print("*")*i
    i=i+1
a*i
i=1
a="*"
while i<=4:
    a*i
    i=i+1
i=1
a="*"
while i<=4:
    print(a*i )
    i=i+1
num=int(input("Enter number"))
res=1
i=0

while num>1:
    res=res*(num-i)
    i=i+1

print(res)
num=int(input("Enter number"))
res=1
i=0

while num-i>1:
    res=res*(num-i)
    i=i+1

print(res)
num=int(input("Enter number : "))
res=1
i=0

while num-i>1:
    res=res*(num-i)
    i=i+1

print("the factorial {} is : ".format(res))
num=int(input("Enter number : "))
res=1
i=0

while num-i>1:
    res=res*(num-i)
    i=i+1

print("the factorial of {} is {}".format(num, res))
name = 'Jesaa29Roy'
size = len(name)
i=0
while i<size:
    if name[i].isdecimal():
        break;
    print(name[i], end=' ')
    i=i+1
print("|nThe execution has stopped")
i=1
a="*"
while i<=4:
    print(a*i )
    i=i+1
name = 'Jesaa29Roy'
size = len(name)
i=0
while i<size:
    if name[i].isdecimal():
        break;
    print(name[i], end=' ')
    i=i+1
print("/nThe execution has stopped")
name = 'Jesaa29Roy'
size = len(name)
i=0
while i<size:
    if name[i].isdecimal():
        break;
    print(name[i], end=' ')
    i=i+1
print()
print("The execution has stopped")
name = 'Jesaa29Roy'
size = len(name)
i=-1
while i<size-1:
    i=i+1
    if not name[i].isalpha():
        continue;
    print(name[i], end=' ')
    i=i+1
print()
print("The execution has stopped")
name = 'Jesaa29Roy'
size = len(name)
i=-1
while i<size-1:
    i=i+1
    if not name[i].isalpha():
        continue;
    print(name[i], end=' ')
    i=i+1
name = 'Jesaa29Roy'
size = len(name)
i=-1
while i<size-1:
    i=i+1
    if not name[i].isalpha():
        continue;
    print(name[i], end=' ')

















