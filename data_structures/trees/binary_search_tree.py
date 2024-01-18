class Node: 
    def __init__(self, value): 
        self.value = value 
        self.left = None 
        self.right = None 

class BinarySearchTree: 
    def __init__(self, value): 
        new_node = Node(value)
        self.root = new_node

    # To create an empty BST: 
    # def __init__(self):
    #     self.root = None 
        
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            # If inserting node at root, don't want to continue this method
            return True 
        temp = self.root 
        while (True):
            # If new node value is equal to another node in tree 
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True 
                temp = temp.left 
            else: 
                if temp.right is None: 
                    temp.right = new_node
                    return True 
                temp = temp.right 

            
my_tree = BinarySearchTree(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)