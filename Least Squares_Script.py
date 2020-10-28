# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:12:19 2020

@author: Luke

Least Squares for the Refinery Problem

"""

import sympy as sp

##### ENTER THE COEFFICIENT MATRIX (A)#####
A = sp.Matrix([[1,0,0],
             [1,1.1,1.4641],
             [1,1.9,13.0321],
             [1,3.0,81.0],
             [1,4.1,282.5761],
             [1,5.3,789.0481]
             ])

print("The Coeficient Matrix:")
sp.pprint(A)

##### ENTER THE SOLUTION VECTOR #####
D = sp.Matrix([[4.0],
             [3.6],
             [4.1],
             [5.6],
             [7.9],
             [11.8]])

print("\nThe Solution Vector:")
sp.pprint(D)

##### CREATES AN AUGMENTED MATRIX FOR A&D #####
aug=A.col_insert(3,D)

##### PRINTS THE AUGMENTED MATRIX AND RREF FORM
print("\nAugmented Matrix for AX=D:")
sp.pprint(aug)            
print("\nReduced Row Echelon Form for the Augmented Matrix:")
sp.pprint(aug.rref()[0])
#print("\nTHE SYSTEM IS INCONSISTENT")


##############################################################################
print('\n--------------------------------------------------------------')
print("FIND THE BEST SOLUTION USING LEAST SQUARES (A^T A AND A^T B)")

#CREATE THE PIECES YOU NEED FOR THE NORMAL EQUATIONS: A^T A AND A^T B

##### FIND THE TRANSPOSE OF A & D #####
ATA = A.transpose() * A
ATb = A.transpose() * D
I = ATA.inv() #INVERSE

print("\nA transpose A =")
sp.pprint(ATA)
print("\nA transpose D = ")
sp.pprint(ATb)
print('\nInverse A Transpose A')
sp.pprint(I)

print('\nx-hat = (Inverse of ATA) * (A Transpose B)')
sp.pprint(I * ATb)

##############################################################################
## now we need to create the augmented matrix for the normal equatations
## !!!! if you use this code and change A, you may end up with a 
## ATA bigger than 2 x 2 , and will need to change 3 below

ne_aug = ATA.col_insert(3,ATb)

print('\n--------------------------------------------------------------')
print('The Augmented Matrix for the Normal Equations(Transpose A&B) is:')
sp.pprint(ne_aug)
print("\nIts reduced rref is")
sp.pprint(ne_aug.rref()[0])


# Pull out the solution
# ne_aug.rref()[0] gets the rref matrix
# .col(2) picks column 3 (counting starts a 0, because of 0 indexing)
xhat=ne_aug.rref()[0].col(2)
print("\nThe Least Squares Solution, x_hat, is:")
sp.pprint(xhat)

## find out how close we are by 
## computing the the least squares projection

p=A*xhat

print("\np = A x_hat = ") 
sp.pprint(p)

# finally the least squares error which is minimized by least squares projection

diff  =  D-p

print("\nLeast Squares Error")

sp.pprint(diff.norm())