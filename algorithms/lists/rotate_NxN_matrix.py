# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:56:57 2019

@author: Michael ODonnell
"""

# Question:
# Rotate matrix A by 90 degress clockwise

A = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]]


def rotate_matrix(matrix):
    # general approach, rotate each square matrix within A by 90 degrees
    
    # first, find the number of squares that make up the NxN matrix
    # and, make sure the matrix is square
    N = len(matrix)
    
    if N != len(matrix[1]) or matrix == None:
        print(matrix, "is not an NxN matrix")
        
    else:
        # in python, // is floor division
        # use floor division to find number of squares within sqare
        for i in range(N // 2):
            
            # loop through each square and rotate one piece at a time
            for j in range(i, N-i-1):
                
                # make a temporary top row
                temp = matrix[i][j]
                
                # send top row to the rightmost column
                matrix[i][j] = matrix[N-1-j][i]
                
                # send rightmost column to the bottom row
                matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
                
                #send the bottom row to the leftmost column
                matrix[N-1-i][N-1-j] = matrix[j][N-1-i]
                
                #send the leftmost column to the top row
                matrix[j][N-1-i] = temp
    
    return(matrix)

# alright, let's test it..
rotate_matrix(A)
print(A)
    