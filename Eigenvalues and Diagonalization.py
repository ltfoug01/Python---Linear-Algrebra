# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:28:38 2020

@author: Luke

        Determinant
        Eigenvectors 
        Eigenvalues
        Diagonalization
"""
import sympy as sp

##### FIND THE DETERMINANT #####
A=sp.Matrix([[3,-3,1],
             [-2,8,-2],
             [2,-6,4]])

print("Matrix A =")
sp.pprint(A)

print("\nDeterminant of A = ")
sp.pprint(A.det())


########## FIND THE EIGENVECTORS AND EIGENVALUES ##########
print("\n----------------------------------------")
print('EIGENVALUES AND EIGENVECTORS\n')

A = sp.Matrix([[2,0,-24],
             [12,6,72],
             [0,0,6]])

print("Matrix A =")
sp.pprint(A)

print('\nEigenvalues :') ##(Value, Multiplicity)
print(A.eigenvals())

print("\nEigen Values (Eigenvalue, Algebraic multiplicity) of A  and the Eigenvectors")
sp.pprint(A.eigenvects())

print("\nP and D for A where P and D are the Diagonalization")


########## FIND THE DIAGONALIZATION ##########
print("\n----------------------------------------")

print("DIAGONALIZATION\n")

print("A =")

sp.pprint(A)
print("\nThe diagonalization of A, (P,D)")
sp.pprint(A.diagonalize())



