#Node constructor for doubly linked list

class Node:
    def __init__(self, value): 
        self.value = value
        self.next = None
        self.prev = None

# Doubly linked list constructor 
class DoublyLinkedList: 
    def __init__(self, value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head == None: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1 
        # Insert method requires boolean return 
        return True 
    
    def pop(self):
        # If no items in linked list
        if self.length == 0:
            return None
        # Set temp variable to tail 
        temp = self.tail
        # If 1 item in linked list 
        if self.length == 1: 
            self.head = None
            self.tail = None
        else: 
            # Move pointer to previous node
            self.tail = self.tail.prev
            # Set next node to none to remove end node
            self.tail.next = None 
            # Break off temp pointer
            temp.prev = None 
        self.length -= 1
        return temp 
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True 
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head 
        if self.length == 1:
            self.head == None
            self.tail == None
        else:
            self.head = self.head.next
            self.head.prev = None 
            temp.next = None 
        self.length -= 1
        return temp 
    
    def get(self, index):
        # Return none when index out of range
        if index < 0 or index >= self.length:
            return None 
        temp = self.head
        # Start at head when index is in first half of list
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        # If index is in second half of list
        else: 
            # Set variable to tail
            temp = self.tail
            # Iterate through list backward, starting at tail and decrement
            for _ in range(self.length - 1, index, -1):
                # Move variable back by 1 
                temp = temp.prev
        return temp #.value <-- Use when testing get()

    # Set value of node in selected index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp: 
            temp.value = value
            return True 
        return False
    
    # Insert value at selected index
    def insert(self, index, value):
        # Return false when index is out of range
        if index < 0 or index > self.length:
            return False
        # Use prepend method when index is 0
        if index == 0: 
            return self.prepend(value)
        # Use append method when index is length of list
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        # Assign variable value to selected index - 1
        before = self.get(index -1)
        # Assign variable value to before + 1 (or selected index + 1)
        after = before.next 
        # Point new node to before pointer
        new_node.prev = before
        # Point new node to after pointer
        new_node.next = after 
        # Assign new node 
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True 
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0: 
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        # Assign variable to selected index (node to remove)
        temp = self.get(index)
        # Isolate temp variable 
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        # Remove node 
        temp.next = None
        temp.prev = None 
        self.length -= 1 
        return temp 
        
        
my_doubly_linked_list = DoublyLinkedList(1)

my_doubly_linked_list.append(2)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

my_doubly_linked_list.pop()

my_doubly_linked_list.prepend(0)

my_doubly_linked_list.pop_first()

my_doubly_linked_list.insert(2, 3)

my_doubly_linked_list.remove(2)

# Change value of index 1 to 17
# my_doubly_linked_list.set_value(1, 17)

# Use when testing get()
# print(my_doubly_linked_list.get(1))

my_doubly_linked_list.print_list()