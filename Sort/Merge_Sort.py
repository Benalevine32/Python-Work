#merge sory
import random

def mergeSort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr) //2
    left_half =mergeSort(arr[:mid])
    right_half=mergeSort(arr[mid:])

    return merge(left_half,right_half)

def merge(left,right):
    sorted_list =[]
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

random_list = [random.randint(1, 1000) for _ in range(100)]
print("presorted: ", random_list)

sorted_list = mergeSort(random_list)
print("Sorted: ", sorted_list)