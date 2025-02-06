def mergeSort(array):
    if len(array) <= 1:
        return array
    
    middle = len(array) // 2
    leftSide = mergeSort(array[:middle])
    rightSide = mergeSort(array[middle:])
    
    return merge(leftSide, rightSide)

def merge(left, right):
    sortedArray = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedArray.append(left[i])
            i += 1
        else:
            sortedArray.append(right[j])
            j += 1

    # Add any remaining numbers from each array
    sortedArray.extend(left[i:])
    sortedArray.extend(right[j:])

    return sortedArray

unsorted_even = [7, 2, 5, 4, 1, 6, 0, 3]
unsorted_uneven = [7, 2, 5, 4, 1, 6, 8, 0, 3]
lonely_array = [2]

print(mergeSort(unsorted_even))
print(mergeSort(unsorted_uneven))
print(mergeSort(lonely_array))