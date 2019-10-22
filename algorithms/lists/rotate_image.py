# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:26:37 2019

@author: Michael ODonnell
"""

# Question:
# Given an image represented by an NxN matrix,
# where each pixel image is 4 bytes
# Write a method to rotate the image by 90 degrees.
# Can you do this in place?

def rotate_matrix(A):
    # find dimensions of matrix
    N = len(A[0])
    
    # figure out how many squares are in the matrix
    for i in range(N // 2):
        
        # for each square, find length of sides of square
        for j in range(i, N - i - 1):
            
            # make a te,porary top row
            temp = A[i][j]
            
            # send top row to last column
            A[i][j] = A[N - 1 - j][i]
            
            #  send last column to bottom row
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j] 
            
            # send bottom row to left column
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            
            # send left column to top row
            A[j][N - 1 - i] = temp
    
    # cross fingers and print matrix!
    print(A)
            
rotate_matrix([[1, 2, 3], 
               [4, 5, 6],
               [7, 8, 9]])
        
