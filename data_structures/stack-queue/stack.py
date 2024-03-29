class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None 

# Initialize stack w/ stack constructor

class Stack: 
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1 

    def print_stack(self):
        temp = self.top
        while temp: 
            print(temp.value)
            temp = temp.next

    def push(self, value):
        # Create new node
        new_node = Node(value)
        if self.height == 0: 
            self.top = new_node
        else: 
            # Initialize top as next node
            new_node.next = self.top 
            # Initailize top as new node
            self.top = new_node
            # Increase height by 1
            self.height += 1 

    def pop(self):
        if self.height == 0:
            return None 
        # Set variable to top
        temp = self.top 
        # Move top pointer to next node
        self.top = self.top.next
        # Remove top item from list 
        temp.next = None 
        # Decrement by 1 
        self.height -= 1
        return temp 

my_stack = Stack(4)

my_stack.push(3)

# Test pop method
# my_stack.pop()

my_stack.print_stack()