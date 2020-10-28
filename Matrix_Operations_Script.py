# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:29:12 2020

@author: Luke
"""

import sympy as sp

# SCALING A MATRIX
print("SCALAR MULTIPLICATION OF MATRICES")
A = sp.Matrix([[2,0,-2],
             [4,-5,2]])

#MULTIPLYING MATRIX A
C = -3*A
print("A =")
sp.pprint(A)

print("2A =")
sp.pprint(C)
print("---------------------")


##### MATRIX ADDITION/SUBTRACTION #####
print("MATRIX ADDITION / SUBTRACTION")
A = sp.Matrix([[1,2],
             [-3,1]])
B = sp.Matrix([[-5,2],
             [4,2]])
C = A.add(2*B)
D = A+B
print("A =")
sp.pprint(A)
print("B =")
sp.pprint(B)
print("\nA+B =")
sp.pprint(C)
print("\nA-B =")
sp.pprint(D)
print("---------------------")

##### MATRIX MULTIPLICATION A AND B MUST BE CONFORMABLE #####
print("MATRIX MULTIPLICATION")

A = sp.Matrix([[979/3220,-45/644],
             [-45/644,11/644]])
B = sp.Matrix([[51.2],
             [198.2],
             ])
C = A*B

print("A =")
sp.pprint(A)

print("B =")
sp.pprint(B)

print("\nAB =")
sp.pprint(C)

print("---------------------")

##### THE TRANSPOSE OF A MATRIX #####
print("THE TRANSPOSE OF A MATRIX")

A = sp.Matrix([[1,-3.25],
               [1,-1.25],
               [1,1.75],
               [1,2.75]])
B = sp.Matrix([[1],
              [3],
              [5],
              [5]])

C = A.transpose()
D = B.transpose()


print("A =")
sp.pprint(A)

print("\nB =")
sp.pprint(B)

print("\nA transpose =")
sp.pprint(C)

print("\nB transpose =")
sp.pprint(D)

##### INVERSE #####
#Inverse = A.inv()  ##Must be square matrix to invert
#print('\nInverse of A Transpose')
#sp.pprint(Inverse)