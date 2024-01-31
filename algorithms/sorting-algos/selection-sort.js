function selectionSort(nums) {
    for (i = 0; i < nums.length - 1; i++) {
        let smallestIndex = i
        for (j = i + 1; j < nums.length; j++) {
            if (nums[j] < nums[smallestIndex]) {
                smallestIndex = j
            }
        }
        if (smallestIndex !== i) {
            [nums[i], nums[smallestIndex]] = [nums[smallestIndex], nums[i]]
        }
    }
} 

let numbers = [12, 19, 2, 17, 3, 8, 19, 20, 18, 1]

selectionSort(numbers) 