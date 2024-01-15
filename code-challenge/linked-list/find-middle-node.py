class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        # Initialize slow and fast pointer to head
        slow = self.head
        fast = self.head
        # While fast and fast.next is not None 
        while fast and fast.next: 
            # Move slow pointer one node at a time
            slow = slow.next
            # Move fast pointer two nodes at a time
            fast = fast.next.next
        # Return middle node
        return slow 


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

# Output should be 3
print( my_linked_list.find_middle_node().value)