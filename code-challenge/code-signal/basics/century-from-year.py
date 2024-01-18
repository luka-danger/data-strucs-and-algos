# Given a year, return the century it is in 
# Century 1: Years 1 - 100
# Century 2: Years 101 - 200

import math

def solution(year):
    centuryCalc = year / 100
    if centuryCalc < 1 or centuryCalc == 1: 
        century = 1
        return century
    else:
        century = math.ceil(centuryCalc)
        return century 

# Test Case 
print(solution(1905))