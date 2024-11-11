#Udemy Course for python lists
#List creation, names dictate the type of list it is    
integers = [1,2,3,4]
strings = ['a', 'b', 'c', 'd']
floats = [1.1, 2.2, 3.3, 4.4]
mixed = [1,'two',3,'four']
nested = [1,2,3,4, [1,2,3,4]]

#Trverses through the list
for x in mixed:
    print(x)

#Accessing elements of the list
print(integers[0])
#Adding elements to the end of the list
integers.append(5)
print(integers)

#Adding elements to the beginning of the list
integers.insert(0,0)
print(integers)

#Removing elements from the list
integers.remove(4)
print(integers)

#poping item out of list
integers.pop(0)
print(integers)

#pop vs remove:
#pop removes the item and returns it
#remove removes the item and doesn't return anything, Removes the first occurrence of a value
#pop is faster than remove

del integers[0]
print(integers)
#Del: Deletes by index or slice, or deletes the entire list or variable.

#Reversing list
integers.reverse()
print(integers)

#Combining two lists with extend built in method
newInts =[10,11,12,13]
integers.extend(newInts)
print(integers)

#Slicing a list
#Everything before index 4
print(integers[:4])
#Everything after index 4
print(integers[4:])
#Everything between index 2 and 4
print(integers[2:4])


#Searcbing a list
def searchList(array, target):    
    for i in range(len(array)):
        if array[i] == target:
            return 'Item is located at ' + str(i)
        return 'Element is not found  '
    
#hfdsnj

#Concating two lists
a = [1,2,3]
b = [4,5,6]
c = a + b 
print (c)

#Creates repeating elements based on the number
starOperator = [2]
starOperator *= 3
print(starOperator)

print(len(integers))
print(min(integers))
print(max(integers))
print(sum(integers))

#adding user info to a list
myList = list()
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        num = float(num)
    except:
        print('Invalid input')
        continue
    myList.append(num)
    average = sum(myList) / len(myList)
print("average: ", average)