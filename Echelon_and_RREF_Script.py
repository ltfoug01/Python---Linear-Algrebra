# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:19:17 2020

Program allows user to enter an augmented matrix and 
determines the Echelon Form and Reduced Row Echelon Form (RREF)

@author: Luke
"""

import sympy as sp

##A = sp.Matrix([[3,2,6,0],[-6,-6,-12,0],[0,-7,-7,0]])

## ENTER MARTIX A
A = sp.Matrix([[1,2,5],
             [2,-3,6],
             [1,-12,-4]
             ])

## PUT MATRIX A INTO ECHELON FORM
A_echelon = A.echelon_form()

##PRINT ORIGINAL MATRIX AND ECHELON FORM MATRIX
print("The echelon form of Matrix A: \n")
sp.pprint(A)
print("\nis\n")
sp.pprint(A_echelon)

## PRINT THE RREF OF MATRIX A
print("\nand the rref form is\n")
sp.pprint(A.rref())
print("\nor\n")
sp.pprint(A.rref())

#print("\nThe last column, which is the solution \n")
#sp.pprint(A.rref()[0].col(3))