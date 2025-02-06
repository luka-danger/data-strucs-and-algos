
def sum_is_twenty(array, sub):
   index = []
   for i in range(len(array)):
      if sum(array[i: i + sub]) == 20:
         index.append(i)
   return len(index)

my_array = [7, 12, 8, 11, 9]
print(sum_is_twenty(my_array, 2))

