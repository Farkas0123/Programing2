import time
import random
from operator import itemgetter
import statistics

def InsertionSort (l):
    i = 1
    while i < len(l):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j], l[j-1] = l[j-1], l[j]
            j = j-1
        i = i + 1
    return

def WhichSort(listlen, sortname):
    l = []
    for i in range(listlen):
        l.append(random.randint(0,1))
    start = time.time()
    sortname(l)
    end = time.time()
    print(listlen, end-start)
    return

WhichSort(10, InsertionSort)
WhichSort(100, InsertionSort)
WhichSort(1000, InsertionSort)
WhichSort(10000, InsertionSort)
#WhichSort(100000, InsertionSort)

#Exercise2
 
WhichSort(100000, sorted)
WhichSort(100000, list.sort)

#Exercise3
l = []
l.append(('Mariann', 5, 20))
l.append(('Ferenczy', 4, 21))
l.append(('Akhzan', 3, 2))
l.append(('Papp', 3, 220))
l.append(('Farkas', 5, 20))
l.append(('Fullix', 1, 22))
l.append(('Felix', 2, 19))
l.append(('Jutocsa', 3, 18))
l.append(('peter', 4, 20))
l.append(('Albert', 5, 13))

l = sorted(l, key = itemgetter(2))

for i in l:
    print(i)


#Bonus exercise
def LinearSearch(l, target):
    i = 0
    while i < len(l) and l[i] != target:
        i = i + 1
    return i

def BinarySearch(l, target):
    left, right = 0, len(l) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

numbers = list(range(100000000))
l = random.sample(numbers, 100000000)
start = time.time()
l = sorted(l)
end = time.time()
sorttime = end - start
print(f'Time took to sort the list {sorttime}')

lineartime = []
for i in range(100):
    target = random.choice(l)

    start = time.time()
    LinearSearch(l, target)
    end = time.time()
    lintime = end-start
    lineartime.append(lintime)
    ### The binary search takes 0 time. We just focus on the linear search
    # start = time.time()
    # BinarySearch(l, target)
    # end = time.time()
    # bintime = end-start
    # print(f'Binary: {bintime}')
    
average = statistics.mean(lineartime)

print(f'The time spent with sorting: {sorttime} s, The average linear search time: {average} s')