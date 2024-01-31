def BubbleSort(numbers):
    # Iterate through entire list
    # Use - 1 to prevent off by 1 error
    for i in range(0, len(numbers) - 1): 
        # Iterate through list minus elements already sorted
        for j in range(0, len(numbers) - i - 1):
            # Check if element 1 is larger than element 2
            # If condition is true, swap elements
            if(numbers[j] > numbers[j+1]):
                # Initialize temp variable and point at index of element 1
                temp = numbers[j]
                # Move element 1 to the next index (where element 2 was)
                numbers[j]= numbers[j+1]
                # Move element 2 to temp index (initial index of element 1)
                numbers[j+1] = temp
    
