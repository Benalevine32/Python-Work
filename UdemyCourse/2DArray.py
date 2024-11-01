import numpy as np

twoDemensionalArray = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15, 16]])
print(twoDemensionalArray)
print(" ")

#Adding Column to two dimensional array

#newTwoDemensionalArray = np.insert(twoDemensionalArray, 0, [[17,18,19,20]], axis=1)
#print(newTwoDemensionalArray)
#print(" ")

#Accessing any element
#a[i][j] i = row / j = column

def accessElements(array, rowIndex, columnIndex):
    if rowIndex >= len(array) or columnIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][columnIndex])



accessElements(twoDemensionalArray, 1, 2)