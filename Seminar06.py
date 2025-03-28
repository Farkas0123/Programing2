class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        note = '-'
        return f'The parent of {self.data} is {str(note)if self.parent is None else str(self.parent.data)}. Left child {str(self.left.data) if self.left is not None else note}, right child {str(self.right.data) if self.right is not None else note}.'
    #is {self.parent}. 
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def Insert(self, data):
        newn = Node(data)
        if self.root is None:
            self.root = newn
            return
        
        current_node = self.root
        
        while True:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = newn
                    newn.parent = current_node
                    break
                current_node = current_node.left
            elif data > current_node.data:
                if current_node.right is None:
                    current_node.right = newn
                    newn.parent = current_node
                    break
                current_node = current_node.right
            else:
                print(f'The node {data} already exsists')
                break

    def Search(self, data):
        current_node = self.root
        while True:
            if data < current_node.data:
                if current_node.left is None:
                    return False
                current_node = current_node.left
            elif data > current_node.data:
                if current_node.right is None:
                    return False
                current_node = current_node.right
            else:
                return current_node
    
    def FindMinimumFromNode(self, node):
        if node is None:
            print('Do not give me a NONE VALUE, Do YoU UNDERSTAND?!')
            return
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left

        return current_node.data
    
    def FindSuccessor(self, data):
        #Hibás!!!
        element = self.Search(data)
        if  element != False:
            if element.right is None:
                return element.parent
            else:
                current_node = element.right
                while current_node.left is not None:
                    current_node = current_node.left
                return current_node
        else:
            print('This element does not exist')
            return


# Create an instance of BinarySearchTree
bst = BinarySearchTree()

# Insert values into the BST
bst.Insert(6)
bst.Insert(5)
bst.Insert(5)
bst.Insert(7)
bst.Insert(22)
bst.Insert(234)
bst.Insert(0)
bst.Insert(564)
bst.Insert(98)
bst.Insert(45)
bst.Insert(23)
bst.Insert(31)
print("done")

# Verifying the structure of the BST by printing the root and its immediate children
print(bst.root.left)
print(bst.root)

bst.Search(2)
print(bst.FindMinimumFromNode(None))

print(bst.FindSuccessor(98))


