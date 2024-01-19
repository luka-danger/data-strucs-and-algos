# Don't get tricked into using a nested for loop!!! --> O(n^2) 

def item_in_common(list1, list2): 
    my_dictionary = {}
    for i in list1:
        my_dictionary[i] = True
    for j in list2:
        if j in my_dictionary:
            return True 
    return False 

list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))
    
'''
list1 = [1, 3, 5]
list2 = [2, 4, 5]

Loop through first list O(n)
{ 
  1: True, 
  3: True,
  5: True
}

Loop through second list O(n)
{ 
  1: -- Compare 1 and 2
  3: -- Compare 3 and 3
  5: -- Compare 5 and 5 (True!)
}

Big O = O(2n) --> O(n)
'''