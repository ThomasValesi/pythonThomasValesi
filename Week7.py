#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:14:40 2023

@author: thomasvalesi
"""

import numpy as np
import matplotlib.pyplot as plt


%matplotlib inline

# Vos données et opérations pour créer le graphique
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Création du graphique
plt.plot(x, y)
plt.title('Exemple de graphique avec matplotlib')
plt.xlabel('X')
plt.ylabel('Y')

# Afficher le graphique
plt.show()


%matplotlib inline
x=np.linspace(-2,2,101)
y=x**2
print(x)

plt.plot(x,y)
plt.show


%matplotlib inline
x=np.linspace(0,3*np.pi, 500)

plt.plot(x, np.sin(x**2))
plt.title('A simple chirp')


%matplotlib inline
x=np.linspace(-2,2,101)
y=x**2
print(x)

plt.plot(y)
plt.show

x=np.linspace(-2,2,101)
plt.xlabel("X")
plt.ylabel("F(X)")
y=x**2
plt.plot(x,y,label="x¨2")
y2=x**4
plt.plot(x,y2, label="x¨4")
plt.legend()
plt.show()


%matplotlib inline
nb=int(input("Enter the number of point"))
x=np.linspace(-1,1,nb)
plt.xlabel("X")
plt.ylabel("cos(2pix)")
plt.title('2pix')
y=np.cos(2*np.pi*x)
plt.plot(x,y)
plt.savefig('cos2pix.png')
plt.show()



%matplotlib inline
nb=int(input("Enter the number of point"))
x=np.linspace(-1,1,nb)
plt.xlabel("X")
plt.ylabel("F(x)")
plt.title('2pix')

y=np.cos(2*np.pi*x)
plt.plot(x,y,label="cos(2pix)")

y2=np.sin(2*np.pi*x)
plt.plot(x,y2,label="sin(2pix)")

plt.legend()
plt.savefig('cossin2pix.png')
plt.show()



%matplotlib inline
nb=int(input("Enter the number of point"))
x=np.linspace(0,4,nb)
plt.xlabel("X")
plt.ylabel("F(x)")
plt.title('sin(pix)sin(20pix)e-x')

y=np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
plt.plot(x,y)

plt.savefig('sinsin.png')
plt.show()


try:
    nb = int(input("Enter the number of points: "))
    if nb <= 0:
        raise ValueError("Number of points should be a positive integer.")
except ValueError as e:
    print(f"Error: {e}")
else:
    x = np.linspace(0, 4, nb)
    plt.xlabel("X")
    plt.ylabel("F(x)")
    plt.title('sin(πx)sin(20πx)e⁻x')

    y = np.sin(np.pi * x) * np.sin(20 * np.pi * x) * np.exp(-x)
    plt.plot(x, y)

    plt.savefig('sinsin.png')
    plt.show()



%matplotlib inline
nb=int(input("Enter the number of point"))
v=np.linspace(2,10,nb)
T=380
R=0.08206
plt.xlabel("V")
plt.ylabel("P")
plt.title('p=RT/V')

p=R*T/v
plt.plot(v,p)

 


%matplotlib inline
nb=int(input("Enter the number of point"))
nbT=int(input("Enter the number of temperature"))

for i in range(nbT):
    T=int(input("Enter the number of temperature"))
    v=np.linspace(2,10,nb)
    p=0.08206*T/v
    plt.plot(v,p,label=str(T)+"K")
plt.xlabel("V")
plt.ylabel("P")
plt.title('p=RT/V')
plt.legend()
plt.savefig('isotherm.png')
plt.show()



%matplotlib inline
nb=int(input("Enter the number of point"))
x=np.linspace(-2,2,nb)
s=0.3
xo=0
plt.xlabel("x")
plt.ylabel("Gauss")
plt.title('GAUSS')

y=(1 / (np.sqrt(2 * np.pi))) * np.exp((-1/2) * ((x - xo)**2 / s**2))
plt.plot(x,y)
plt.legend()
plt.savefig('Gauss.png')
plt.show()



%matplotlib inline
nb=int(input("Enter the number of point"))
x=np.linspace(0,3,nb)
plt.xlabel("X")
plt.ylabel("F(x)")
plt.title('Comparaison')

y=np.exp(-x)
plt.plot(x,y,label="exp(-x")

y2=np.sin(3*np.pi*x)*np.exp(-x)
plt.plot(x,y2,label="sin(3pix)*exp(-x)")

plt.legend()
plt.savefig('exo2.png')




# Function to calculate a Gaussian curve
def gaussian(x, xo, s):
    return np.exp(-((x - xo) ** 2) / (2 * s ** 2)) / (s * np.sqrt(2 * np.pi))

# Ask how many curves to represent
num_curves = int(input("Enter the number of Gaussian curves to represent: "))

# Create an array to store the curves
curves = []

# Ask for parameters for each curve and generate the curves
for i in range(num_curves):
    xo = float(input(f"Enter the xo value for curve {i+1}: "))
    s = float(input(f"Enter the s value for curve {i+1}: "))
    curve = gaussian(x, xo, s)
    curves.append(curve)
    plt.plot(x, curve, label=f'Curve {i+1}: xo={xo}, s={s}')

# Generate the plot
plt.xlabel("X")
plt.ylabel("F(x)")
plt.title("Gaussian Curves")
plt.legend()
plt.savefig('gaussianes.png')
plt.show()



































