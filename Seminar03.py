import time


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


#Exercise 2

class ListQueue:
    def __init__(self):
        self.head = None        

    def enqueue(self, item):
        item = Node(item)
        if self.head == None:
            self.head = item
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = item
        return

    def pop(self, index):
        result = self.head
        self.head = self.head.next 
        return result       

    def peek(self):
        print(self.head.data)

    def size(self):
        len = 0
        current = self.head
        while current:
            current = current.next
            len += 1
        return len
    
l = ListQueue()
l.enqueue(1)
l.enqueue(1814)
l.enqueue(123)
l.enqueue(156)
l.enqueue(13)
l.enqueue(10)
print(l.size())
print(l.pop(0).data)
print(l.size())
l.peek()
print(l.size())

#exercise 2b
def measure_time(queue_class, db = 100000):
    queue = queue_class
    start = time.time()
    for i in range(100000):
        queue.enqueue(i)
    for i in range(100000):
        queue.pop(0)
    
    
    end = time.time()
    return end-start

#times = measure_time(ListQueue())
#print(f'The time: {times}')

#webhistory type shit
class BrowserHistory:
    def __init__(self):
        self.head = None

    def visit(self, url):
        #Push a new URL onto the stack when a page is visited
        url = Node(url)
        if self.head == None:
            self.head = url
            return
        current = self.head
        self.head = url
        self.head.next = current
        return

    def go_back(self):
        #Pop the last URL from the stack to go back to the previous page
        if self.head == None:
            print('please search before looking at the search history')
        result = self.head
        self.head = self.head.next
        return result.data
        
    def current_page(self):
        if self.head == None:
            print('Empyt history')
            return    
        return self.head.data

    def show_history(self):
        # Display the entire browsing history
        result= ''
        if self.head == None:
            return result
        current = self.head
        while current.next != None:
            result += str(current.data)+' '
            current = current.next
        result += current.data
        return result
#test
# Create a new BrowserHistory object
browser_history = BrowserHistory()

# Visiting pages
browser_history.visit("page1.com")
browser_history.visit("page2.com")
browser_history.visit("page3.com")
browser_history.visit("page4.com")
browser_history.visit("page5.com")
browser_history.visit("page6.com")

# Checking the current page
print("Current page:", browser_history.current_page())

# Going back
print("Going back to:", browser_history.go_back())

# Current page after going back
print("Current page after going back:", browser_history.current_page())

# Show the entire browsing history
print("Browser history:", browser_history.show_history())            