def selection_sort(nums):
    for i in range(0, len(nums)):
        lowestIndex = i
        for j in range(i + 1, len(nums)):
            if (nums[j] < nums[lowestIndex]):
                lowestIndex = j
        (nums[i], nums[lowestIndex]) = (nums[lowestIndex], nums[i])

numbers = [12, 19, 2, 17, 3, 8, 19, 20, 18, 1]

selection_sort(numbers)

print(numbers)