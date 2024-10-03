import random

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]                             #Create Pivot at the middle
        left = [x for x in arr if x < pivot]                   #All numbers in array less than pivot in a left arr
        middle = [x for x in arr if x == pivot]                #Middle is equal to the pivot
        right = [x for x in arr if x > pivot]                  #all numebrs in array greater than pivot in right away 
        return quickSort(left) + middle + quickSort(right)     #Recursive to keep iterating until done


random_list = [random.randint(1, 1000) for _ in range(100)]
print("presort: ", random_list)

sorted_list = quickSort(random_list)
print("Sorted: ", sorted_list)
