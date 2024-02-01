def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1 
        while j >= 0 and temp < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = temp

numbers = [15, 4, 9, 1, 8, 7]

insertion_sort(numbers)

print(numbers)