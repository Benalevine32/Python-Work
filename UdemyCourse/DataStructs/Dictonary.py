#Dictory-
#A collection which is unordered, changeable and indexed. No duplicate members.
#Dictionaries are written with curly brackets, and have keys and values.


#Creating a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#Dictonary in memory
#Hashtables are a way of doing key value look ups in C languages. They store keyvaleus in an array then use hashing functions to
#find the index in the array cell that corresponds to the key.

engToEsp = {
    "one": "uno",
    "two": "dos",
    #Incorrect
    "three": "cuatro"
}
#Updating the value in key "three"
engToEsp["three"] = "tres"
#Adding a new key with a new Value
engToEsp["four"] = "cuatro"
print(engToEsp)

def TraversesDictionary(dict):
    for x in dict:
        print(x + ': ' + dict[x])
TraversesDictionary(engToEsp)

def SearchDictionay(dict, key):
    if key in dict:
        print(dict[key])
    else:
        print("Key not found")
SearchDictionay(engToEsp, "one")


#Deleting / Removing an element of the dictionary
engToEsp["five"] = "cinco"
print(engToEsp)
del engToEsp["Five"]
print(engToEsp)

#Built in dictionary methods 