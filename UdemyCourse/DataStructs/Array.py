from array import *

my_array = array('i', [1,2,3,4,5])

#Traverses through the array 
for i in my_array:
    print(i)
print(" ")

#Access individual elements of the array 
print(my_array[0])

#Adding element to the array 
# O(1) Time complexity
my_array.append(6)
print(my_array)
print(" ")

#Insterting elemetn to the array
#This is different than append (Takes two arguments)
#Append adds element to the end of the arry
#Instert takes two arguments
# The first is the index, Second is value
# O(n) Time complexity where n is size of array
my_array.insert(6,7)
print(my_array)
print (" ")

#Extending array with array.extend
my_array1 = array('i' , [8,9,10])
my_array.extend(my_array1)
print(my_array)
print(" ")

#Adding elements to an array from a lists

tempList = [24,25,26]
my_array.fromlist(tempList)
print(my_array)
print(" ")

#Remove element with remove function
my_array.remove(26)
print(my_array)
print(" ")

#Removing last element from arrya
my_array.pop()
print(my_array)
print(" ")

#Index method to find any given method
print(my_array.index(3))
print(" ")

#Reverse the array using build in python function

my_array.reverse()
print(my_array)
print(" ")

#Get array buffer information
print(my_array.buffer_info())
print(" ")