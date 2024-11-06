import numpy as np

twoDemensionalArray = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15, 16]])
print(twoDemensionalArray)
print(" ")

#Adding Column to two dimensional array

#First number means effects rows
#Axis effects Columns


#newTwoDemensionalArray = np.insert(twoDemensionalArray, 0, [[17,18,19,20]], axis=1)
#print(newTwoDemensionalArray)
#print(" ")

#Accessing any element
#a[i][j] i = row / j = column bhb

def accessElements(array, rowIndex, columnIndex):
    if rowIndex >= len(array) or columnIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][columnIndex])

def traversesTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

#Search 2D Array
def searchTDArray(array, target):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == target:
                return 'Item is located at ' + str(i) + " " + str(j)
    return 'Element is not found'

newTDarray = np.delete(twoDemensionalArray,0, axis=1)
print(newTDarray)


#accessElements(twoDemensionalArray, 1, 2)

#traversesTDArray(twoDemensionalArray)

#print(searchTDArray(twoDemensionalArray, 8))