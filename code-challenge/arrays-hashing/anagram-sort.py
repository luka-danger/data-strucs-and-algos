def anagramSort(s, t):
    return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"

print(anagramSort(s, t))

a = "apple"
b = "baseball"

print(anagramSort(a, b)) 