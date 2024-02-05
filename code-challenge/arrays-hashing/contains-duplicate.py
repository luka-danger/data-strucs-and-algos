# Instructions: 
# Given an integer array, nums, return true if any value appears at least twice in array
# Return false if every element is distinct 

# Solution 
def containsDuplicate(nums):
    hashset = set()
    
    for i in nums:
        if i in hashset: 
            return True
        hashset.add(i)
    return False

# Return False
myArray = [1, 2, 3, 4]
print(containsDuplicate(myArray))

# Return True
myOtherArray = [5, 6, 7, 5]
print(containsDuplicate(myOtherArray)) 

# Run Time: O(n)
# Solution iterates through array n times

# Space: O(n)
# Hashset memory could go up to size of array