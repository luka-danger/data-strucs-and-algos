class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


# Set parameter to input stack 
def sort_stack(stack):
    # Initialize temp stack
    temp_stack = Stack()
    while not stack.is_empty():
        # Pop each element in input stack into temp variable 
        temp = stack.pop()
        # Run while temp stack not empty and top element is greater than element in temp 
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            # Push each item popped from temp stack into input stack
            stack.push(temp_stack.pop())
        # Push temp variable into temp stack
        temp_stack.push(temp)
    while not temp_stack.is_empty():
        # Pop each sorted item from temp stack and push to input stack 
        stack.push(temp_stack.pop())


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""