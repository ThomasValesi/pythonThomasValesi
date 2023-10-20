#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:23:30 2023

@author: thomasvalesi
"""

dico={
      'H' :{'Element': 'Hydrogen', 'Atomic Number':1 , 'Melting Point': 14, 'Boiling Point' : 20},
      'He':{'Element': 'Helium', 'Atomic Number':2 , 'Melting Point': 1, 'Boiling Point' : 4},
      'Li':{'Element': 'Lithium', 'Atomic Number':3 , 'Melting Point': 453, 'Boiling Point' : 1603},
      'Be':{'Element': 'Beryllium', 'Atomic Number':4 , 'Melting Point': 1560, 'Boiling Point' : 2742},
      'B' :{'Element': 'Boron', 'Atomic Number':5 , 'Melting Point': 2349, 'Boiling Point' : 4200}}
e=input('saisir le symbole de un élement')
t=int(input('saisir sa temperature'))

if(dico[e]['Melting Point']<t<dico[e]['Boiling Point']):
    print('liquide')
elif(t<dico[e]['Melting Point']):
    print('solid')
elif(t>dico[e]['Boiling Point']):
    print('gaz')
print(dico['Be']['Atomic Number'])

    
    
dicobank={
            'ANZ': {'years 1 & 2':2.3 , 'year 3': 4.1},
            'Bank of australia': {'years 1 & 2':0.1 , 'year 3': 5.0},
            'Commonwealth bank': {'years 1 & 2':3.5 , 'year 3': 3.8},
            'West pack': {'years 1 & 2':3.7 , 'year 3': 3.7}}

one_two=float(input('saisir votre pret mesuel de lannée 1 et 2 : '))
three=float(input('saisir votre pret mesuel de lannée 3 : '))

if(dicobank['ANZ']['years 1 & 2']==one_two and dicobank['ANZ']['year 3']==three):
    print('ANZ')
elif(dicobank['Bank of australia']['years 1 & 2']==one_two and dicobank['Bank of australia']['year 3']==three):
    print('Bank of australia')
elif(dicobank['Commonwealth bank']['years 1 & 2']==one_two and dicobank['Commonwealth bank']['year 3']==three):
    print('Commonwealth bank')
elif(dicobank['West pack']['years 1 & 2']==one_two and dicobank['West pack']['year 3']==three):
    print('West pack')



nb_degree=int(input('saisir le nombre de degrès : '))
coef_degre=input('saisir les coef : ')
tab_degres=coef_degre.split(' ')
tab_degre_float=[float(num) for num in tab_degres]
cst=float(input('saisir la constante : '))
x=float(input('saisir x : '))

tot=0.0
for i in range(nb_degree):
    tot=tab_degre_float[i]*x**(i+1) + tot
tot=tot+cst
print(tot)


import numpy as np
import random
import matplotlib.pyplot as plt

array=np.arange(0,21)
for i in range(9,16):
    array[i]=array[i]*(-1)
print(array)


array=np.arange(15,56)
print(array)
print(array[1:40])

array=np.zeros((3,4))
for i in range(3):
    for j in range(4):
        array[i,j]=input('entrer un nombre : ')
print(array)


array=np.zeros(10)
for i in range(10):
    array[i]=random.randint(5,50)
print(array)

array=np.zeros(5)
for i in range(5):
    array[i]=int(input('entrer un nombre entre 0 et 10'))
print(array)
array2=np.zeros(5)
for i in range(5):
    array2[i]=int(input('entrer un nombre entre 0 et 10'))
print(array2)
array3=array*array2
print(array3)

array=np.zeros((3,4))
a=10
for i in range(3):
    for j in range(4):
        array[i,j]=a
        a=a+1
print(array)
nb_lignes, nb_colonnes=array.shape
print(nb_lignes , nb_colonnes)

array=np.ones((4,4))
for i in range(4):
    array[i,i]=0
print(array)


array1=np.array([1,0,3,4,5])
array2=np.array([1,7,8,2])
array3=np.zeros(len(array1)+1)
a=0
for i in range(len(array1)):
    for j in range(len(array2)):
        if(array1[i]==array2[j]):
            array3[a]=array2[j]
            a=a+1
print(array3)



array1=np.array([1,0,4,4,1])
array2=np.array([[1,7,8,2],[1,9,2,3]])
array3=np.zeros(len(array1))
a=0
for i in range(len(array1)):
    for j in range(len(array1)):
        if(array1[i]==array1[j]):
            array3[a]=array1[j]
            a=a+1
print(array3)

array1=np.array([1,0,4,4,1])
array1_unique=np.unique(array1)
print(array1_unique)


array2=np.array([[1,7,8,7],
                 [1,9,2,3]])
print(array2)
array2_unique=np.unique(array2)
print(array2_unique)

array1=np.array([1,9,3,4,5])
array2=np.array([1,7,8,2,8])
array3=np.zeros(len(array1))
a=0
for i in range(4,-1,-1):
    array3[a]=array1[i]*array2[a]
    a=a+1
print(array3)

# Create the original array
original_array = np.arange(100)

# Given scalar value
given_scalar = 42.89

# Find the closest value
closest_value = original_array[(np.abs(original_array - given_scalar)).argmin()]

print("Original array:")
print(original_array)
print(f"Given scalar: {given_scalar}")
print(f"Closest value: {closest_value}")


# Create a random 10x2 matrix with Cartesian coordinates
cartesian_matrix = np.random.rand(10, 2)

# Extract x and y coordinates
x = cartesian_matrix[:, 0]
y = cartesian_matrix[:, 1]

# Calculate polar coordinates
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

# Print polar coordinates
print("Radius (r):")
print(r)

print("\nAngle (θ) in radians:")
print(theta)

# Convert angle to degrees
theta_degrees = np.degrees(theta)
print("\nAngle (θ) in degrees:")
print(theta_degrees)


array=np.linspace(1,5,21)
array1=array*0.1
print(array)
print(array1)

x0=float(input('saisir la valeur de x0 : '))
s=float(input('saisir la valeur de s : '))

array=np.arange(-1,1,0.4)
array2=np.zeros(len(array))
for i in range(len(array)):
    array2[i]=(1/np.sqrt(2*np.pi))*np.exp((-1/2)*((array[i]-x0)**2/s**2))
print(array2)


temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
'November', 'December']
array_mars=np.zeros(12)
for i in range(12):
    array_mars[i]=temp_mar[i]

average=np.average(array_mars)
print(average)

mini=np.min(array_mars)
maxi=np.max(array_mars)
index_mini=0
index_maxi=0
for i in range(12):
    if(array_mars[i]==mini):
        index_mini=i
    if(array_mars[i]==maxi):
        index_maxi=i

print(mini)
print(months[index_mini])
print(maxi)
print(months[index_maxi])




n=int(input('saisir le nombre détudiants : '))
array=np.zeros((n,4))
array_total=np.zeros(n)

for i in range(n):
    array[i,0]=i

for j in range(n):
    for k in range(1,3):
        if(k==1):
            array[j,k]=float(input(f'entrer la note du test théorique de l élève {j} : '))
        if(k==2):
            array[j,k]=float(input(f'entrer la note du test pratique l élève {j} : '))
            
for a in range(n):
    array[a,3]=array[a,1]*0.4 + array[a,2]*0.6
    array_total[a]=array[a,1]*0.4 + array[a,2]*0.6
print(array)
print()

maxi=np.max(array_total)
print(maxi)
index_maxi=np.where(array==maxi)
print(index_maxi)


n=int(input('saisir un nombre : '))
array=np.arange(n)
array_premier=np.zeros(n)
a=0
b=0
for i in range(n):
    for j in range(1,n):
        if(i%j==0):
            a=a+1
    if(a==2):
     array_premier[b]=i
     b=b+1
    a=0
print(array_premier)
            

x=np.linspace(-2,2,101)
plt.xlabel("X")
plt.ylabel("F(X)")
y=x**2
plt.plot(x,y,label="x¨2")
y2=x**4
plt.plot(x,y2, label="x¨4")
plt.legend()
plt.show()


x=np.linspace(-5,5,10)
plt.xlabel("X")
plt.ylabel('F(X)')
y=2*x+8
plt.plot(x,y,label='2x+8')
y2=-2*x+12
plt.plot(x,y2,label='-2x+12', color='green')
plt.legend()
plt.show()



nb=int(input('entrer le nombre de points : '))
start=float(input('entrer la valeur de départ : '))
end=float(input('entrer la valeur de fin : '))
x0=float(input('entrer la valeur de x0 : '))
s=float(input('entrer la valeur de s : '))

x=np.linspace(start,end,nb)
plt.xlabel('X')
plt.ylabel('G(X)')
plt.title('Gaussian graph')
y=(1/(np.sqrt(2*np.pi)))*np.exp((-1/2)*(((x-x0)**2)/(s**2)))
plt.plot(x,y,label='Gaussian')
plt.legend()
plt.savefig('Gauss.png')
plt.show()


nb=int(input('entrer le nombre de valeurs'))

x=np.linspace(0,3,nb)
plt.xlabel('X')
plt.ylabel('F')

y=np.exp(-x)
plt.plot(x,y,label='exp(-x)')

y2=np.sin(3*np.pi*x)*np.exp(-x)
plt.plot(x,y2,label='sin(3pix)*exp(-x)')

plt.title('exp et sin')
plt.legend()
plt.show()



nb_point=int(input('entrer le nombre de points : '))
nb_fonction=int(input('entrer le nombre de fonction : '))
start=float(input('entrer la valeur de départ : '))
end=float(input('entrer la valeur de fin : '))

x=np.linspace(start,end,nb_point)
plt.xlabel('X')
plt.ylabel('G(X)')
plt.title('Gauss fonction')


for i in range(nb_fonction):
    x0=float(input('entrer la valeur de x0 : '))
    s=float(input('entrer la valeur de s : '))
    y=(1/(np.sqrt(2*np.pi)))*np.exp((-1/2)*(((x-x0)**2)/(s**2)))
    plt.plot(x,y,label=f'x0={x0} et s={s}')

plt.legend()
plt.show


list_thomas=['salut','coucou']
list_thomas.insert(1,'bite')
print(list_thomas)
list_thomas.pop(0)
print(list_thomas)


array=np.arange(0,100,10)
print(array)
array1=np.linspace(0,100,10)
print(array1)





dico={
      'thomas':{'note1':13, 'note2':16, 'note3':20},
      'damien':{'note1':16, 'note2':19, 'note3':17}}

print(dico['damien']['note2'])
print(len(dico))



array=np.zeros((3,3))
print(array)

array=np.lin


def filter_numbers(list1, list2):
    # Create a new list containing odd numbers from list1
    odd_numbers = [x for x in list1 if x % 2 != 0]

    # Create a new list containing even numbers from list2
    even_numbers = [x for x in list2 if x % 2 == 0]

    # Concatenate the two lists to create the final result
    new_list = odd_numbers + even_numbers

    return new_list

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = filter_numbers(list1, list2)
print(result)


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
    

nb=int(input('entrer un nombre : '))
tot=0
for i in range(1,nb-1):
    if(nb%i==0):
        tot=tot+i
if(nb==tot):
    print('the number is perfect')
else:
    print('the number is not perfect')
    
    
nb=int(input('entrer un nombre : '))
list1=[]

for i in range(1000):
    a=0
    for j in range(1,1000):
        if(i%j==0):
            a=a+1
    if(a==2):
        list1.append(i)

for i in range(0,nb):
    print(list1[i])
        
    













    

