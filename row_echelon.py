"""
row_echelon.py

Educational implementation of Row Echelon Form (REF) and RREF.
"""
import numpy as np
from typing import List, Tuple
def swap_rows(M: np.array, i: int, j: int)-> None:
    M[[i,j]]=M[[j,i]]
