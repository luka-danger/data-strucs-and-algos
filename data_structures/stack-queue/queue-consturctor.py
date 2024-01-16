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
    
    # Add itme to end of queue (Getting in line) 
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
            

my_queue = Queue(4)

my_queue.enqueue(5)

my_queue.print_queue()
