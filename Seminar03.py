class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            last_node.next = new_node

    def insert(self, prev_data, data):
        if self.head == None:
            print('Empty linkedlist, please use append instead')
            return
        new_node = Node(data)
        current_node = self.head
        while current_node and current_node.data != prev_data:
            current_node = current_node.next
        if current_node == None:
            print('Previous node not found')
            return
        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, data):
        if self.head == None:
            print('The list is empty, use append instead')
            return
        current_node = self.head
        prev = None
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next
        if current_node == None:
            print('Element not found')
            return
        if prev == None:
            self.head = self.head.next
        else:
            prev.next = current_node.next

    def find(self, data):
        current_node = self.head
        while current_node.data != data and current_node:
            current_node = current_node.next
        if current_node == None:
            print('Node not found')
        else:
            print('Node found')

    def show_items(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        
        
        
        

l = LinkedList()
l.append('apple')
l.append('peach')
l.append('plum')
l.insert('peach', 'orange')
l.remove('aaaa')
l.show_items()
l.find('apple')


