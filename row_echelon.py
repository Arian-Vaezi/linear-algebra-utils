"""
row_echelon.py

Educational implementation of Row Echelon Form (REF) and RREF.
"""
import numpy as np
from typing import List, Tuple
def swap_rows(M: np.array, i: int, j: int)-> None:
    M[[i,j]]=M[[j,i]]

def find_nonzero_row(M: np.array, col, start_row):
    n_row=M.shape[0]
    for i in range(start_row, n_row):
        if M[i,col]!=0:
         return i
    return None

def add_scaled_row(M, source_row, target_row,scale):
   M[target_row]+=M[source_row]*scale

def scale_row(M: np.array,i:int , factor: float):
   if factor==0:
      raise ValueError("scale factor must be non-zero")
   M[i]=factor*M[i]

def row_echelon(M: np.array):
    A=M.copy()
    n_row, n_cols=M.shape
    pivot_row=0

    for col in range (n_cols):
       r=find_nonzero_row(A, col, pivot_row)
       if r is None:
        continue
       if r!=pivot_row:
          swap_rows(A,r,pivot_row)
       factor=1.0/A[pivot_row,col]
       scale_row(A,pivot_row,factor)
       for r2 in range(pivot_row+1,n_row):
          scale=-A[r2,col]
          add_scaled_row(A,pivot_row,r2,scale)
       pivot_row+=1
    return A
M= np.array([[4,2,3]
              ,[2,5,6]
              ,[3,8,9]], float)

M=row_echelon(M)
print(M)

