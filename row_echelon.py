"""
row_echelon.py

Educational implementation of Row Echelon Form (REF) and RREF.
"""
import numpy as np
from typing import List, Tuple
def swap_rows(M: np.array, i: int, j: int)-> None:
    M[[i,j]]=M[[j,i]]
def find_nonzero_row(M: np,array, col, start_row)->None:
    numberOfRow=M.shape()
    for i in range(start_row, numberOfRow[0]):
        if M[i,col]!=0:
         return i
    return None
