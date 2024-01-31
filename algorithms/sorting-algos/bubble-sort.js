function bubbleSort(numbers) {
    // Iterate through entire list
    for (i = 0; i < numbers.length; i++) {
        // Iterate through list minus elements already sorted
        for(j = 0; j < numbers.length - i - 1; j++) {
            // Check if element 1 is larger than element 2
            // If condition is true, swap elements
            if (numbers[j]> numbers [j+1]) {
                // Initialize temp variable and point at index of element 1
                temp = numbers[j]
                // Move element 1 to the next index (where element 2 was)
                numbers[j] = numbers[j+1]
                // Move element 2 to temp index (initial index of element 1)
                numbers[j+1] = temp 
            }
        }
    }
}

let numbers = [12, 19, 2, 17, 3, 8, 19, 20, 18, 1]

bubbleSort(numbers)