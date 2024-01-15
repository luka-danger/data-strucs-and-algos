class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def has_loop(self):
        # Initialize slow and fast pointer to head
        slow = self.head
        fast = self.head
        # Iterate through each node in linked list
        for _ in range(self.length):
            # Move slow pointer one node at a time
            slow = slow.next
            # Move fast pointer two nodes at a time
            fast = fast.next.next 
            # Return false if both fast and fast.next is None, indicates no loop
            if fast and fast.next is None: 
                return False
            # Return false indicates no nodes
            if fast is None:
                return False
            # Return true when if both nodes meet, indicates loop
            if fast == slow:
                return True
    
    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""