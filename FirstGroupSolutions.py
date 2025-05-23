def find_sum_subarray(A, k):
    solutions = []
    actsum = 0
    act = []
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            actsum += A[j]
            act.append(A[j])
            if actsum == k:
                solutions.append(act)
                act = list(act)
        actsum = 0
        act = []
    if len(solutions) == 0:
        return None
    else:
        return tuple(max(solutions, key = lambda x: len(x)))
            
    
assert find_sum_subarray((1,2,3,-1,4,2,-2,1,1), 6) == (3,-1,4,2,-2)
assert find_sum_subarray((4, 5, -2, 1, 0, 5), 9) == (5,-2,1,0,5)
assert find_sum_subarray((4, 5, -2, 1, 0, 4), 9) == (4, 5)
assert find_sum_subarray((4, 4, 5), 16) == None

#Q2222222222222

import random

def random_walk(n):
    if n % 2 == 0:
       n += 1
    x = y = n//2+1
    moves = ['-x', '+x', '-y', '+y']
    num = 0
    while True:
        move = random.choice(moves)
        if move == '-x':
            x -= 1
            num += 1
            if x == 0 or x == n:
                break
        elif move == '+x':
            x += 1
            num += 1
            if x == 0 or x == n:
                break
        elif move == '-y':
            y -= 1
            num += 1
            if y == 0 or y == n:
                break
        else:
            y += 1
            num += 1
            if y == 0 or y == n:
                break
    return num        
            
def simulation(n=21, ntimes=1000):
    lens = []
    for i in range(ntimes):
       lens.append(random_walk(n))
    return lens

mau = simulation()
from matplotlib import pyplot as plt
plt.hist(mau, bins=20)
plt.title("Random Walk Steps to Border (1000 simulations)")
plt.xlabel("Steps")
plt.ylabel("Frequency")
plt.show()
#q333333333333333333333333333


class StackNode:
    def __init__(self, contents=None, next_node=None):
        self.value = contents
        self.next_node = next_node
  
    def __str__(self):
        return f"StackNode({self.value})"
   
    def __eq__(self, other):
        return self.value == other.value
   
class Stack:
    def __init__(self):
       self.top_node = None
       
       
    def pop(self):
        if self.top_node is None:
            return None
        result = self.top_node
        self.top_node = self.top_node.next_node
        return result
  
    def push(self, value):
        self.top_node = StackNode(value, self.top_node)
                         
    def __str__(self):
        to_return = "Stack("
        if self.top_node:
           to_return = to_return + str(self.top_node)
           next_top = self.top_node.next_node
           while next_top is not None:
               to_return = to_return + ", " + str(next_top)
               next_top = next_top.next_node
        return to_return + ")"
       
def reverse_stack(stack):
    NewStack = Stack()
    if stack.top_node:
        nexttop = stack.top_node
        while nexttop is not None:
            newelement = stack.pop()
            NewStack.push(newelement.value)
            nexttop = stack.top_node
    return NewStack

s = Stack()
print(s)
s.push(5)
print(s)
s.push(15)
print(s)
s.push("hello")
print(s)

assert s.pop() == StackNode("hello")
assert s.pop() == StackNode(15)
assert s.pop() == StackNode(5)
assert s.pop() == None

s.push(5)
s.push(15)
s.push("hello")

rs = reverse_stack(s)
assert rs.pop() == StackNode(5)
assert rs.pop() == StackNode(15)
assert rs.pop() == StackNode("hello")
assert rs.pop() == None

#q444444444444444
import pandas as pd
df = pd.read_csv('visits.csv', parse_dates=['Timestamps'])

median_duration = df['Duration'].median()
df['Duration'] = df['Duration'].fillna(median_duration)
df = df[df['Clicks']>2]
df['Clicks/minute'] = df['Clicks']/(df['Duration']*60)
result = df.groupby('User_ID')['Clicks_per_minute'].mean()
