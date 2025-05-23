import numpy as np

x = np.arange(10) #numbers from 0-9
x
x = np.arange(1,17).reshape(4,4) # matrix containing elements from 1-16
print(x)
 
x = np.eye(5) 
print(x)

A = np.random.randint(0,10,size=(2,4))
B = np.random.randint(0,10,size=(3,4))
print(np.vstack((A, B)))                    #verticaly stacking matrices on top of eachother


A = np.random.randint(1,11,size=(3,3))
B = np.random.randint(101,111,size=(3,3))
#np.add(A,B)
#np.multiply(A, 100)


F = np.random.uniform(1,11,size=(3,3)) #float numbers
print(F)
print(np.floor(F))
F = np.round(F, 2)
print(F)

####################     Statistical information about a matrix
A = np.random.randint(1,10, size=(4,5))
print(np.mean(A, axis=0))
#For the whole table
print(np.std(B))
#For the column
print(np.std(B, axis=0))
#For the rows
print(np.std(B, axis=1))



#Pandas
import pandas as pd
serieA = pd.Series([3.0,2,1,'shoe',1.5,['apple','banana'],2,3.0,100])

print(serieA)
print(serieA.values)
print(serieA.index)
print(serieA[2:5])
just_threes= serieA[
    (serieA == 3) #| (my_first_series == 'shoe') #& and syntax
]

print( just_threes*2)

def square(x):
    return x**2

print( just_threes.apply(square))

actor_rating_dict = {'Nicolas Cage':10,'Robert Redford':5,'Julianne Moore':8,
                     'Jeff Bridges':7, 'Idris Elba':8,'Meryl Streep':9,
                     'Pam Grier':9
                     }
actor_rating_series =pd.Series(actor_rating_dict)
actor_frequency_dict = {'Nicolas Cage':20,'Robert Redford':6,
                        'Julianne Moore':10, 'Jeff Bridges':2,
                        'Idris Elba':14,'Mr. Bean':3,'Meryl Streep':7,
                        'Pam Grier':11}

actor_frequency_series = pd.Series(actor_frequency_dict)
df = pd.concat([actor_rating_series,actor_frequency_series], axis=1)#if axis = 0 then it just puts them on top of eachother
print(df)
df.columns = ['Average_Rating','Number_of_Movies']

avg=np.mean(df['Average_Rating'])
df.Average_Rating=df.Average_Rating.fillna(avg)
print(df)