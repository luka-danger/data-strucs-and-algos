# Instructions: 
# Given an integer array, nums, return true if any value appears at least twice in array
# Return false if every element is distinct 

# Pseudocode: 
# For Loop (x in nums)
# Iterate through each value in nums
# If i = some value in nums, return false
# If i != some value in nums, return true 

#ideas: 
# Put each number into new array and run a nested for loop to compare? 
# O(n^2) - not best approach 

# Sorted array could be O(logn) which would be more ideal 

# Solution 
nums = []
for i in nums: 
    x = i 
        