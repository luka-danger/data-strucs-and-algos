def print_all_permutations(permList, nameList):
    size = len(nameList)
    
    if size == 0:
        for i in range(len(permList)):
            if i == len(permList) - 1:
                print(permList[i])
            else:
                print(permList[i], end=', ')
    else:
        for i in range(size):
            newPerms = permList.copy()
            newPerms.append(nameList[i])
            newNames = nameList.copy()
            newNames.pop(i)
            print_all_permutations(newPerms, newNames) 

if __name__ == "__main__":
    nameList = input().split(' ')
    permList = []
    print_all_permutations(permList, nameList)


    


