import time 

#exercise 1
start = time.time()

def sum_list(l):
    result = 0
    assig = 0
    for i in l:
        result += i
        assig += 1
    return result, assig

def findmax(l):
    comp = 0
    max = l[0]
    for i in l:
        if i > max:
            max = i
        comp += 1
    return max, comp    

list = [1,2,3,4,5,6,7,8,9,10]
end = time.time()
print(f'{sum_list(list)}, time: {end-start}')
print(f'{findmax(list)} time: {end-start}')

#exercise 2
list = []
for i in range(10000, 0, -1):
    list.append(i)
start = time.time()
def bubble(l):
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

bubble(list)
end = time.time()
print(f'bubble time:{end-start}')
list = []
for i in range(1000000, 0, -1):
    list.append(i)
start = time.time()
list.sort()
end = time.time()
print(f'builtin: {end-start}')


############
start = time.time()
list= []
list = [i**2 for i in range(100)]
end = time.time()
print(f'list comprehension: {end-start}')
start = time.time()
list = []
for i in range(100):
    list.append(i**2)
end = time.time()
print(f'for: {end-start}')

#######
def linear(l, v):
    i = 0
    while l[i] != v:
        i += 1
    return i
'''
^^^^
its best if the numb is at the first place
average if its in the middle
worst if its in the end
'''
def binarysearch(l, low, high, v):
    if high >= low:
        mid = (low+high)//2

        if l[mid] == v:
            return mid
        elif l[mid] < v:
            return binarysearch(l, mid+1, high, v)
        elif l[mid] > v:
            return binarysearch(l, low, mid-1, v)
    else:
        return -1
'''
all of the scenarios are the same, since the runtime takes log(n) steps
if the list contains 1.000.000.000.000.000 it would take 50 steps to find the element
'''
list = []
for i in range(1000000000):
    list.append(i)

start = time.time()
vau = linear(list, 10000)
end = time.time()
print(f'linear {end-start}||index({vau})')

start = time.time()
vau = binarysearch(list, 0, len(list)-1, 6009240)
end = time.time()
print(f'binary {end-start}||index({vau})')