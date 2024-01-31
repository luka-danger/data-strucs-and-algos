function bubbleSort(numbers) {
    for (i = 0; i < numbers.length; i++) {
        for(j = 0; j < numbers.length - i - 1; j++) {
            if (numbers[j]> numbers [j+1]) {
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp 
            }
        }
    }
}

let numbers = [12, 19, 2, 17, 3, 8, 19, 20, 18, 1]

bubbleSort(numbers)