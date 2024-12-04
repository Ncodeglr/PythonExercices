"""Un robot se déplace dans une matrice et maximise son NBcoin
"""
import numpy as np
import random as rd

def InitMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = rd.randint(0,3)
    return matrix

def Trajectory(matrix,NBcoin,row,column):
    limit = 2
    print("NBcoin = ", NBcoin)
    print(matrix)
    if(row == limit and column == limit):
        print(f"\nTerminé ! Position finale : ({row}, {column}).")
        print(f"NBcoin total = {NBcoin}")
        return matrix
    else:
        if(row !=limit and column !=limit):
            tmp1 = NBcoin + matrix[row][column+1]
            tmp2 = NBcoin + matrix[row+1][column]
            tmp3 = NBcoin + matrix[row+1][column+1]
            print("Voici les tmp = ",tmp1,tmp2,tmp3)
            print("")
            NBcoin = max(tmp1,tmp2,tmp3)
            if(NBcoin == tmp1):
                row,column = row,column+1
            elif(NBcoin == tmp2):
                row,column = row+1,column
            else:
                row,column = row+1,column+1
        elif(column == limit):
            NBcoin = NBcoin + matrix[row+1][column] 
            row,column = row+1,column
        elif(row == limit):
            NBcoin = NBcoin + matrix[row][column+1] 
            row,column = row,column+1
        
        print(f"\nPosition actuelle : ({row}, {column})")
        return Trajectory(matrix,NBcoin,row,column)

matrix = np.zeros((3, 3))
Trajectory(InitMatrix(matrix),matrix[0][0],0,0)