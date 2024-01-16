class Node:
    def __init__(self, value): 
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value): 
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1 

    def print_queue(self):
        temp = self.first
        while temp: 
            print(temp.value)
            temp = temp.next
    
    # Add item to end of queue (Getting in line) 
    def enqueue(self, value):
        # Create new node
        new_node = Node(value)
        # First and last item in line 
        if self.length == 0:
            self.first == new_node
            self.last == new_node
        else: 
            # Enqueue from end 
            # Add new node to end 
            self.last.next = new_node
            # Move last pointer to new node
            self.last = new_node
        # Increment length of list by 1 
        self.length += 1

    # Remove item from list 
    def dequeue(self):
        if self.length == 0:
            return None 
        temp = self.first
        # Reset pointers to None 
        if self.length == 1:
            self.first = None
            self.last = None 
        else: 
            # Move pointer to next node 
            self.first = self.first.next 
            # Remove node from list 
            temp.next = None 
        self.length -= 1
        return temp 

my_queue = Queue(4)

my_queue.enqueue(5)

# Test dequeue 
my_queue.dequeue()

my_queue.print_queue()
