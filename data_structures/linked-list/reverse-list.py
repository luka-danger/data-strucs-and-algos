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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 
        

    def reverse_list(self):
        temp = self.head 
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None 
        for _ in range(self.length):
            after = temp.next
            temp.next = before 
            before = temp
            temp = after 

new_linked_list = LinkedList(1)

new_linked_list.append(2)
new_linked_list.append(3)
new_linked_list.append(4)
new_linked_list.append(5)

new_linked_list.reverse_list()

new_linked_list.print_list()



