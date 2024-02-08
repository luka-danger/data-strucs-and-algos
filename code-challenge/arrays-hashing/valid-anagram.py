def validAnagram(s, t,):
    if len(s) != len(t):
        return False
    
    # Initialize hashmaps to store count of each character in s and t
    countS, countT = {}, {}
    # Iterate through length of string s and add characters to hashmaps
    for i in range(len(s)):
        # Count the occurence of each character in string s 
        # Increment the count of character by 1 for every instance
        # If key does not exist in hashmap, use default value 0
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    # Iterate through hashmaps to make sure they contain same characters
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True 

# Run Time: O(s + t) --> O(n + n)

        