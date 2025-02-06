def binary_search(array, item):
    start = 0
    end = len(array) - 1

    while start <= end: 
        # Find Middle Index
        middle = start + (end - start) // 2

        # Set value to middle index value
        middle_value = array[middle]

        if middle_value == item:
            return middle
        
        elif item < middle_value:
            # Set new middle index to left of middle index
            end = middle - 1

        # If item > middle
        else: 
            # Set middle index to right of middle index
            start = middle + 1

    # if item not found
    return None
    
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

item = int(input("Enter a positive integer: "))

print(f'Found {item} at index: {binary_search(my_array, item)}')