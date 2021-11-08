"""
Write Python program to store 10th class percentage of students in array. Write function for sorting array of floating point numbers in ascending order using radix sort and display top five scores.
"""
# Function to take student percentage:------------------------------------------------

def createArray(n):
    array = []
    for i in range(n):
        percentage = float(input(f"Enter percentage of student {i+1}: "))
        array.append(percentage)
    return array

# function to find maximum element

def maximum(array):
    max = array[0]
    for i in range(len(array)):
        if max<array[i]:
            max = array[i]
    return max

# Main function to run radix sort
def mainFun(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[int(index % 10)] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[int(index % 10)] - 1] = array[i]
        count[int(index % 10)] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
    
# Function of radix sort 

def radixSort(array):
    max = maximum(array)
    place = 1
    while (max//place)!=0:
        mainFun(array, place)
        place *= 10
    return array
 
n = int(input("Enter total number of students value: "))
array = createArray(n)
mini = len(array)-6
maxi = len(array)-1
index = 1
array = radixSort(array)
print("Sorted array using radix sort in ascending order is : ", array)
print("---------------------Top scorer using radix sort-------------------------\n")
for i in range(maxi, mini, -1):
    if i>=0:
        print(f"Topper No. {index}", array[i],"\n")
    index+=1   
