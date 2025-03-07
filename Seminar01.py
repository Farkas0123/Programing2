#Exercise 1
import random

l = []
for i in range(1000):
    l.append(random.randint(1,100))

def summing(list):
    szum = 0
    for i in list:
        szum += i**2
    return szum
print(summing(l))

def sumwcomp(l):
    square_value = [i**2 for i in l]
    return sum(square_value)
print(sumwcomp(l))

#Exercise 2

l.clear()
l = [random.randint(1, 10) for i in range(10)] 
def find_first(l, element):
    i = 0
    while i < len(l)-1 and l[i] != element:
        i+=1
    if (l[i] == element):
        return i+1 
    else:
        return -1
print(l)
print(find_first(l, 4))

def find_all(l, element):
    result = []
    for i in range(len(l)):
        if element == l[i]: 
            result.append(i+1)
    return result
print(find_all(l, 4))

#Exercise 4
def lrev(l):
    result = []
    for i in range(len(l)-1, -1, -1):
        result.append(l[i])
    return result
print(lrev(l))
#exercise 5
def palindrom(s):
    s = s.lower()
    if len(s) % 2 == 1:
        if s[:len(s)//2] == s[len(s)//2+1:][::-1]:
            return True
    

    return False
print(palindrom('sasssas'))
