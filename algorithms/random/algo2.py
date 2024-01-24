S = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
x = 2

while x<11:
    for i in S: 
        if i % x == 0 and i != x: 
            S.remove(i)
            print(S)
    x = x + 1 
    print(x)
print(S)

c = 15 ** 61 % 667 
d = 1000000000000 % 10 
