#Coding Exercises Arrays and lists 

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
