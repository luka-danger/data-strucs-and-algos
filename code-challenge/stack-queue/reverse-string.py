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


def reverse_string(string):
    # Initialize new stack
    stack = Stack()
    # Create empty string
    reversed_string = ''
    # Iterate through each char in input string
    for char in string: 
        # Push each char into stack 
        stack.push(char)
    # Run loop while stack is not empty
    while not stack.is_empty(): 
        # Pop last char from stack and add to first index of string
        # Repeat at next index with next char until stack is empty 
        reversed_string += stack.pop()
    return reversed_string
    
    






my_string = 'hello'

print ( reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""