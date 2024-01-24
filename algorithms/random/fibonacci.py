def fibonacci(num): 
    if num < 2 and num >= 0: 
        return num
    elif num < 0: 
        return -1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2) 
    
print(fibonacci(7)) 
print(fibonacci(20))