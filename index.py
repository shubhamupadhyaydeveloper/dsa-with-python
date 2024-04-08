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