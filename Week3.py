#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:16:08 2023

@author: thomasvalesi
"""

range(2,8,2)

n=int(input("Enter the value of n:"))
for i in range(1, n+1):
    q_i=i**2
    print(q_i)

n=int(input("Enter the value of n:"))
for i in range(1,n+1,2):
    q_i=i**2
    print(q_i)
    
    
sum=0
for i in range(6):
    sum=sum+i
    print(f"The value of sum is in each iteration : {sum}")
print("The sum i valid {}".format(sum))
    

for i in range(4):
    for j in range(3):
        print("i={}, j={} ".format(i,j))
        
sum=0
n=int(input("Enter the value of n : "))
for i in range(n+1):
    sum=sum+i
print(f"The value of the sum is : {sum}")


fact=1
n=int(input("Enter the value of n : "))
for i in range(1,n+1,1):
    fact=fact*i
print("the factorial of {} is {} ".format(n,fact))


for i in range(1,10):
    for j in range(1,10):
        print("{}{}".format(i,j))
        
for i in range(1,10):
    for j in range(0,10):
        if i!=j:
            print("{}{}".format(i,j))
              

n=int(input("Enter the value of n:"))
t=0
for i in range(1,n+1):
    t=(i*(i+1))/2
    print(t)


for i in range (10):
    for j in range(10):
        for k in range(10):
            if i+j+k==22:
                print("{}{}{}".format(i,j,k))


for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            if i**3+j**3+k**3==(i**100+j*10+k):
                print("{}{}{}".format(i,j,k))
                

n=int(input("Enter the value of n : "))
odd=0
sum=0
for i in range(0,n):
    odd=2*i+1
    sum=sum+odd
    print(odd)
print(sum)


n=int(input("Enter the value of n : "))
a=0
for i in range(1,n+1):
    if n%i==0 :
        a=a+1
if a==2:
    print("the number {} is prime".format(n))
elif n==1:
    print("the number {} is prime".format(n))
else : 
    print("the number {} is not prime".format(n))
        


def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

# Exemple d'utilisation :
n = 10
for i in range(n):
    print(fibonacci_iterative(i))
    
    
##-----------------------------------------------------------------------------

us_president_list=['Joe Biden', 'Donald Trump', 'Barack Obama', 'George W Bush', 'Bill Clinton']
print(us_president_list[1])


us_president_list=['Joe Biden', 'Donald Trump', 'Barack Obama', 'Barack Obama', 'George W Bush', 'George W Bush']
for president in us_president_list:
    print(president)

us_president_list.append('Bill Clinton')
print(us_president_list)

friend_list=['Chloé', 'Erwan', 'Carla', 'Elena', 'Charles', 'Damien']
for i in range(3):
    print(friend_list[i])

friend_list.append('Antoine')
print(friend_list)

friend_list.remove('Antoine')
print(friend_list)

us_president_tuples=('Joe', 'Biden', '2021-01-20', 'Democratic')
print(us_president_tuples)


_Integer=[1,2,3,4]
print(_Integer)
print(_Integer[1:3])


friend_list=['Chloé', 'Erwan', 'Carla', 'Elena', 'Charles', 'Damien']
print(friend_list[:4])
print(friend_list[3:])

print(friend_list[::2])
print(friend_list[-2])


num =int(input("Enter a number"))
num_list=[]
for i in range(1,num+1):
    num_list.append(1/i)
print(num_list)

sum=0
for j in range (num):
    sum= sum + num_list[j]
print(sum)


a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b
print(f"First instruction print {c}")
b[0] = -1
d = []
for e in a:
    d.append(e+1)
print(f"Second instruction print: {d}")
d.append(b[0]+1)
d.append(b[1] +1)
print(f"Third instruction print: {d}")
print(f"Fourth instruction print: {d[-2:]}")
print(f"Fifth instruction print: {d[:-1]}")
print(f"Sixth instruction print: {d[1:4]}")


num=int(input("Enter a number "))
square_list=[]
for i in range(num+1):
    square_list.append(i**2)
print(square_list)


nom=[]
note=[]
m=0

name="aaaa"
while (name!=""):
    name=input("Enter a name : ")
    if(name!=""):
        nom.append(name)
        x=int(input("Enter his grade : "))
        note.append(x)

somme=0
for i in range (len(note)):
    somme+=note[i]
if (len(note)!=0):
    m=somme/len(note)
print (nom)
print (note)
print("the average is : ", m)
























