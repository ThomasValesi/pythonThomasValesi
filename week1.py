#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 08:45:31 2023

@author: thomasvalesi
"""

a= 5
b=3
c=2.5

d=(2*a+b**2)/c
print(d)

n = input("entrer un nombre : ")
n=float(n)
print(n*2)

p=float(input("entrer une pression : "))
print(p*2)

import math

r=float(input("enter the value of the radius"))
h=float(input("enter the value of the height"))
pi=math.pi

v=(1/3)*pi*r**2*h
print(v)

num1 = float(input("enter a numeric value:"))
num2 = float(input("enter another numeric value : "))
sum = num1 + num2
product = num1*num2
print("the sum of {} and {} is {}".format(num1, num2, sum))
print("the product of {} and {} is {}".format(num1, num2, product))

cel = float(input("Enter a temperature in degrees Celsius : "))
fahr=(cel*(9/5))+32
print("The temperature {} in Celsius is {} in Fahrenheit".format(cel,fahr))

length = float(input("Enter the lenght of a cube : "))
area=length**2*6
volume=length**3
print("the area of the cube is {} and its volume is {}".format(area,volume))


banknote10=float(input("how many banknotes of 10 do you have : "))
banknote20=float(input("how many banknotes of 20 do you have : "))
banknote50=float(input("how many banknotes of 50 do you have : "))
nb10=10
nb20=20
nb50=50
tot=banknote10*nb10+banknote20*nb20+banknote50*nb50
print("the total of his banknotes is : {}".format(tot))

radius = float(input("Enter the radius of the circle"))
cirlen = 2*pi*radius
cirarea= pi*radius**2
print("The length of the circle is {} and its area is {}".format(cirlen, cirarea))

angle=float(input("Enter the angle "))
cote1=float(input("Enter the cote 1 "))
cote2=float(input("Enter the cote 2 "))
radian=angle*(pi/180)
c2=cote1**2+cote2**2-2*cote1*cote2*math.cos(radian)
c=math.sqrt(c2)
print("the third length is : {}".format(c))







































