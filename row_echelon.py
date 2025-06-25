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

def row_echelon(M: np.array)->Tuple[np.ndarray,list[int]]:
    A=M.copy()
    n_row, n_cols=M.shape
    pivot_row=0
    pivot_cols=[]

    for col in range (n_cols):
       r=find_nonzero_row(A, col, pivot_row)
       if r is None:
        continue
       if r!=pivot_row:
          swap_rows(A,r,pivot_row)
       pivot_cols.append(col)
       factor=1.0/A[pivot_row,col]
       scale_row(A,pivot_row,factor)
       for r2 in range(pivot_row+1,n_row):
          scale=-A[r2,col]
          add_scaled_row(A,pivot_row,r2,scale)
       pivot_row+=1
    return A,pivot_cols

def rref(M:np.array)->np.array:
   E, pivot_cols= row_echelon(M)
   r=len(pivot_cols)
   for k in range(r-1,-1,-1):
      col=pivot_cols[k]
      for i in range(k):
         if E[i,col]!=0:
            scale=-E[i,col]
            add_scaled_row(E,k,i,scale)
      factor=1.0/E[k,col]  #renormalizing 
      scale_row(E,k,factor)
   return E
            

M= np.array([[4,1,1]
              ,[1,1,2]
              ,[1,1,3]], float)

# M=row_echelon(M)
RM= rref(M)
print(RM)


