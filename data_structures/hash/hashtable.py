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
            print(i, ": ", val)
    
my_hash_table = HashTable()
my_hash_table.print_table()