# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:49:33 2020

@author: Luke
"""

import sympy as sp

##### MATRIX #####
A=sp.Matrix([[1,2,3,5],
             [3,6,10,17],
             [4,8,15,27]
             ])
print("matrix A")
sp.pprint(A)

##### DETERMINE THE COL(A) AND THE NULL(A)
print("\nColumn space of A is ")

sp.pprint(A.columnspace())

print("\nNull space of A is ")

sp.pprint(A.nullspace())

print("\nRank of A is ")

print(A.rank())