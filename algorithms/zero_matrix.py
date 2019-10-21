# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:28:23 2019

@author: Michael ODonnell
"""

# Question:
# Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.


def zero_matrix(A):
    # get matrix length and height
    height = len(A)
    length = len(A[0])
    
    # create list of rows to be zero'd
    z_row = []
    
    # create list of columns to be zero'd
    z_col = []
    
    # loop through matrix to find position of 0 values
    for i in range(length):
        for j in range(height):
            
            # if we find a zero value, add the row and col to the lists
            if A[i][j] == 0:
                z_row.append(int(i))
                z_col.append(int(j))

    # now, zero out the rows
    for y in z_row:
        for z in range(length):
            A[y][z] = 0
                    
    # then, zero out the columns
    for k in z_col:
        for l in range(height):
            A[l][k] = 0
            
    # finally... return the new matrix
    return(A)
          

print(zero_matrix([[1, 2, 3],
                   [0, 5, 6],
                   [7, 8, 9]]))
