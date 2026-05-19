'''
day2_data_structures

1 lists
2 tuples
3 sets
4 dictionaries
5 comprehensions
6 JSON handling
7 mini code exercises

'''
# 1 lists

fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)

animals = ["cat", "dog", "cow"]

for animal in animals:
    print(animal)

# 2 tuples

student = ("kaka", 21, "python")
name, age, course = student
print(name)
print(age)
print(course)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# 3 sets

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

colors = {"red", "blue", "green"}

for color in colors:
    print(color)

# 4 dictionaries

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2024
}

print(car["brand"])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

# 5 comprehensions

numbers = []

for x in range(5):
    numbers.append(x)

print(numbers)

even_numbers = [x for x in range(10) if x % 2 == 0]

print(even_numbers)

# 6 JSON handling

import json

student = {
    "name": "Ravi",
    "age": 20
}

json_data = json.dumps(student)

print(json_data)

import json

data = '{"name":"Teja","age":21}'

python_data = json.loads(data)

print(python_data)
print(python_data["name"])

# 7 mini code exercises

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

def insertionSort(arr):
    n = len(arr)
    
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]         
        j = i - 1
        while j >= 0 and key < arr[j]: 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key      


arr = [12, 11, 13, 5, -1]
insertionSort(arr)
print(arr)