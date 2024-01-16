# Node constructor
class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

# Linked list constructor 
class LinkedList:
    def __init__(self, value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# Print items in linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# Append item to end of linked list
    def append(self, value):
        new_node = Node(value)
        # Test to see if linked list is empty 
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else: 
            self.tail.next = new_node
            self.tail = new_node
        # Increase length of linked list by 1
        self.length += 1   
        return True  

    def pop(self):
        if self.length == 0: 
            return None
        temp = self.head
        pre = self.head 
        # While temp.next is not None
        while(temp.next): 
            pre = temp 
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # Second if statement is after length is decremented
        if self.length == 0:
            self.head = None
            self.tail = None
        # Return node that was just removed
        # For testing, return temp.value 
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        # Use temp: head needs something pointing at it in order to remove
        temp = self.head 
        self.head = self.head.next 
        temp.next = None
        self.length -= 1
        # Second if statement after decrementer, when starting with one item
        if self.length == 0:
            self.tail = None
        # Return item removed from linked list 
        return temp 
    
    # Return index of node 
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # No variable used in for loop, so use _
        for _ in range(index):
            temp = temp.next
        return temp
    
    # Set is a keyword in Python, so need to call it set value
    # Set value of node 
    def set_value(self, index, value):
        temp = self.get(index)
        # if temp is not None
        if temp: 
            temp.value = value
            return True
        # bypass if statement with invalid index
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
     
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next 
        temp.next = None 
        self.length -= 1
        return temp 

    # 🚨 Common Coding Interview Question 🚨
    def reverse(self):
        temp = self.head
        self.head = self.tail 
        self.tail = temp
        # after variable prevents gaps in linked list 
        after = temp.next 
        before = None 
        for _ in range(self.length):
            # these steps must be in order to prevent gap 
            after = temp.next
            temp.next = before 
            before = temp
            temp = after

# Create a linked list with node 2
my_linked_list = LinkedList(2)

# Add value to end of list
my_linked_list.append(3)

# Add value to beginning of list
my_linked_list.prepend(1)

# Get Node at index 2
my_linked_list.get(2)

# Set value of node 1 to value of 4
my_linked_list.set_value(1, 4)

# Insert value 2 at index 1
my_linked_list.insert(2, 2)

my_linked_list.remove(1)

my_linked_list.reverse()

my_linked_list.print_list()
# Test cases for pop()
'''
# Test (2) Items - Returns 2 Node
print(my_linked_list.pop())
# Test (1) Item - Returns 1 Node
print(my_linked_list.pop())
# Test (0) Items - Returns None
print(my_linked_list.pop())
'''

# Test cases for pop_first()
'''
# Test (2) Items - Returns 2 Node
print(my_linked_list.pop_first())
# Test (1) Item - Returns 1 Node
print(my_linked_list.pop_first())
# Test (0) Items - Returns None
print(my_linked_list.pop_first())
'''

