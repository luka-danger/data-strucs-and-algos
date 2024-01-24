# Big O Notation 

# O(n)
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

# Drop Constants O(n)
# n + n = n 
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

# O(n^2)
# nxn = n^2
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

# Drop non-dominants
#O(n^2 + n) = O(n^2)

# O(n^2)
def print_items(n):
    #O(n)
    for i in range(n):
        #O(n)
        for j in range(n):
            print(i,j)
        #O(n)
        for k in range(n):
            print(k)
    
# O(1)
# Number of operations don't change for addition
# n + n + n is also O(1)
def add_items(n):
    return n + n

