# recursion calculate factorial 
def factorial(num):
    if num == 1:
        return  1
    else:
        return num *  factorial(num-1)
            
# print(factorial(4))

# selection sort

def findSmallest(arr):
    smallest = arr[0] #assume the smallest is at zero index
    smallest_index =  0  #and this is zero
    for i in range(1,len(arr)): # we already use zero so we start from 1 to end of the array
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
     

# print(findSmallest([14,13,32,23,5,111,0,-1]))

def sortArray(arr):
    newArray = []
    copiedArray = arr
    for i in range(len(copiedArray)):
        smallest = findSmallest(copiedArray)
        newArray.append(copiedArray.pop(smallest))
    return  newArray


# print(sortArray([32,34,5,2,7,38,55,23,56,0]))

# binary search

def binary_search(arr,item):
    initial_index = 0
    final_index =  len(arr) - 1
    while initial_index <= final_index:
        mid_index  = (initial_index + final_index) //  2
        guess = arr[mid_index]
        if guess == item:
            return mid_index
        elif guess > item:
            final_index = mid_index - 1
        else:
            initial_index =  mid_index  +  1 
    return None

test_array = [2,3,5,6,7,8,33,45]
# print(binary_search(test_array,45))

# mergesort

def totalSum(arr):
    total  = 0
    for i in arr:
        total += i
    return total

array  =  [2,9,5,1,4,7]
# print(totalSum(array))


#recursion
def sumArray(array,index=0):
    if index == len(array):
        return 0
    else:
        total = array[index]
        index += 1
        return total + sumArray(array,index)

# print(sumArray(array))

#quick sort in python
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less =  [num for num in array[1:] if num <= pivot]
        greater = [num for num in array[1:] if num > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

quick_array = [3,7,0,5,32,56,2]
# print(quicksort(quick_array))

