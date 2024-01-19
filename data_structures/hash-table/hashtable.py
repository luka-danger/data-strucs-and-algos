# Create a hashtable with 7 items in it

class HashTable: 
    def __init__(self, size = 7): 
        self.data_map = [None] * size 

    # Create has method 
    def __hash(self, key):
        my_hash = 0
        for letter in key: 
            # Ord gets ASCII value for each letter
            # Multiply by any prime number
            # Use Modulo to get remainder (will be between 0 - 6: address space)
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
        
    def print_table(self):
        for i, val in enumerate(self.data_map):
            # Output Hash Table 
            # 4 : 'bolts', 1400 
            print(i, ": ", val)

    # Use hash method on key to create the address
    def set_item(self, key, value):
        # Computer address
        index = self.__hash(key)
        # Initialize empty list at address
        if self.data_map[index] == None:
            self.data_map[index] = []
        # Put key value Pair into empty address
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None: 
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key: 
                    return self.data_map[index][i][1]
        return None 

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            # Only run if there is something at address
            if self.data_map[i] is not None: 
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.get_item('bolts')

print(my_hash_table.keys())

my_hash_table.print_table()