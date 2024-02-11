# Introduction to Algorithms 
## Exercise 1.2-2

# Assume on a computer, for size n
# Insertion sort runs at 8n^2 steps
#  Merge sort runs at 64 n log n 
# Which values is insertion sort faster than merge sort? 

# Start at n = 2
n = 2

# Simplifiy the logarithms and then compare in a while loop
while n >= 2 ** (n/8):
    # Increment n until it is larger than the simplified merge sort run time
    n += 1
# Decrease by 1 to find max value
n -= 1

print(f'The highest value where is  : {n}')

## Exercise 1.2-3
x = 2

while 2 ** x < 100 * x ** 2: 
    x += 1

print(f'The smallest value of n where 2^n is faster than 100n^2: {x}')