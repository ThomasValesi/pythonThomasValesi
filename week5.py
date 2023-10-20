#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:55:15 2023

@author: thomasvalesi
"""



def five_numbers():
    list_numbers = []
    for i in range(5):
        number = int(input("Entrer un nombre : "))
        list_numbers.append(number)
    return list_numbers

resultat = five_numbers()
print("Les cinq nombres que vous avez entrés sont :", resultat)

def max_min(list_):
    maximum=max(list_)
    print(f"le max est {maximum}")
    minimum=min(list_)
    print(f"le min est {minimum}")
    
a=max_min(resultat)
    

try:
    f=open('/content/testfile.text')
except Exception:
    print("sorry this file doesn't exist")


def odd_even():
    num=float(input("Entrez un nombre : "))
    if num%2==0:
        print("pair")
    else:
        print("impair")

resultat=odd_even()
        

try:
    odd_even()
except ValueError:
    print("saisi incorrect veuillez reocmmencer")




def prime_odd_even_number():
    n=float(input("Enter the value of n : "))
    a=0.0
    for i in range(1,n+1):
        if n%i==0 :
            a=a+1
    if a==2:
        print("the number {} is prime".format(n))
    elif n==1:
        print("the number {} is prime".format(n))
    else : 
        print("the number {} is not prime".format(n))
        
    if n%2==0:
         print("pair")
    else:
         print("impair")
        
        

try:
    prime_odd_even_number()
except ValueError:
    print("saisi incorrect veuillez reocmmencer")
    
    



##----------------------------------------------------------------------------

import numpy as np

matrice = np.array([[1, 0, 1], [1, 2, 1], [1, 0, 1]])
print(matrice)

arr=np.array([[1, 2, 3]])
r1=np.repeat(arr, 3, axis=0)
print(r1)

arr=np.array([[1, 0, 1]])
r1=np.repeat(arr, 3, axis=0)
r1[1,1]=2
print(r1)

matrice1 = np.ones((5, 5))
matrice2 = np.zeros((3,3))
matrice2[1,1]=9
matrice1[1:4,1:4]=matrice2
print(matrice1)


import numpy as np
y = np.arange(10, 31, 1)
y[4] = 1
print(y)



































