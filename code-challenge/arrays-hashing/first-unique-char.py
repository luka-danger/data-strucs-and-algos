from collections import Counter

def firstUniqueChar(strings):
    count = Counter(strings)
    for i, c in enumerate(strings):
        if count[c] == 1:
            return i
    return - 1 

# Test Case 1
# Should return 0
myString = "leetcode"
print(firstUniqueChar(myString))

# Test Case 2
# Should return 2
myString2 = "lemursloveleetcode"
print(firstUniqueChar(myString2))

# Test Case 3
# Should return -1
myString3 = "aabb"
print(firstUniqueChar(myString3))
