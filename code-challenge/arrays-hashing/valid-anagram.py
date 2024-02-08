def validAnagram(s, t,):
    if len(s) != len(t):
        return False
    
    # Initialize hashmap to store count of each character in s and tß
    countS, countT = {}, {}
    # Iterate through length of string s 
    for i in range(len(s)):
        # Count the occurence of each character in string s 
        # Increment the count of character by 1 for every instance
        # If key does not exist in hashmap, use default value 0
        countS[s[i]] = 1 + countS.get(s[i], 0)
        