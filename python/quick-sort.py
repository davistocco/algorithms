import numpy as np

array = np.random.randint(1, 101, 100)

def quick_sort(array, firstIndex, lastIndex):
    if firstIndex >= lastIndex:
        return
    pivot = array[lastIndex]
    leftPointer = firstIndex
    rightPointer = lastIndex

    while leftPointer < rightPointer:
        while array[leftPointer] <= pivot and leftPointer < rightPointer:
            leftPointer+=1
        while array[rightPointer] >= pivot and leftPointer < rightPointer:
            rightPointer-=1
        swap(array, leftPointer, rightPointer)
    swap(array, leftPointer, lastIndex)

    quick_sort(array, 0, leftPointer - 1)
    quick_sort(array, leftPointer + 1, lastIndex)

def swap(array, a, b):
    tmp = array[a]
    array[a] = array[b]
    array[b] = tmp

print('Array', array)
quick_sort(array, 0, len(array) - 1)
print('Sorted array', array)