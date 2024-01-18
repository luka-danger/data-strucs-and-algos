def palindrome(inputString):
    reverse_word = inputString[::-1]
    if inputString == reverse_word:
        return True 
    else: 
        return False 
    
palindrome('racecar')
 