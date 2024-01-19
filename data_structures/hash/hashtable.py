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
    def set_items(self, key, value):
        # Computer address
        index = self.__hash(key)
        # Initialize empty list at address
        if self.data_map[index] == None:
            self.data_map[index] = []
        # Put key value Pair into empty address
        self.data_map[index].append([key, value])

my_hash_table = HashTable()

my_hash_table.set_items('bolts', 1400)
my_hash_table.set_items('washers', 50)
my_hash_table.set_items('lumber', 70)

my_hash_table.print_table()