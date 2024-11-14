#Coding Exercises Arrays and lists 

import numpy as np
#Exercise 1
def missing_number(arr, n):
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    # Calculate the actual sum of the array
    actual_sum = sum(arr)
    # The missing number is the difference between the expected sum and the actual sum
    return expected_sum - actual_sum

arr = [1, 2, 3, 5]  # Here, n should be 5 since numbers from 1 to 5 are expected
n = 5
print(missing_number(arr, n))  # Output should be 4


#Find two pairs
#Leet code two sum

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])

nums = [2, 7, 11, 15]
target = 18
findPairs(nums, target)


# Testing to see if an array contains a specific number
myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def linearSearch(arr, targert):
    for i in range(len(arr)):
        if arr[i] == target:
            return 'Item is located at ' + str(i)
    return 'Element is not found'


def max_product(arr):
    # Initialize two variables to store the two largest numbers
    max1, max2 = 0, 0  # O(1), constant time initialization
 
    # Iterate through the array
    for num in arr:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment
 
    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication

arr = [1, 2, 3, 4, 5]
print(max_product(arr))