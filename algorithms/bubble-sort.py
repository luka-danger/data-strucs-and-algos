def bubble_sort(list):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j+ 1] = list[j+1], list[j]
    return list

the_list = [6, 3, 4, 2, 7, 1, 5]

print(bubble_sort(the_list))