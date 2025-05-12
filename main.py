import random
import time
import itertools

class Treasure:
    def __init__(self, weight, value):
        '''
        This initialize one treasure and its attributes.
        I created the treasure class because we did it like this in the class as well (Ex.: LinkedList (Node class, LinkedList class))  
        '''
        self.weight = weight
        self.value = value  
        self.ratio = self.value/self.weight
        
class Backpack:
    def __init__(self, n, v1, v2, w1, w2, s1, s2):
        '''
        This is the init function. Initialize the boundaries of the backpack.
        Basically:
        n = number of treasures
        l = lower boundary
        h = Upper boundary
        v = Value of the treasure (in $)
        w = weight of the treasure (in kg)
        s = size of the backpack (in kg)
        '''
        self.n = n
        self.lv = v1
        self.hv = v2
        self.lw = w1
        self.hw = w2
        self.size = random.randint(s1, s2)
        self.treasures = []
        
    def Generate(self):
        '''
        This function generates the data based on the input values of the BackPack
        '''
        for i in range(self.n):
            new_treasure = Treasure(random.randint(self.lw, self.hw), random.randint(self.lv,self.hv)) 
            self.treasures.append(new_treasure)
    
    def OrderByRatio(self):
        '''
        this funciton orders the treasure regarding to ratio. The most valuable will be the first one
        '''
        self.treasures.sort(key=lambda x: x.ratio, reverse= True)
    
    def FirstSolution(self):
        ''' The idea  behind the first solution
        This is my first solution. It is probably not the fastest, escpecially on a large scale. 
        On the other hand it will probably find the correct solution.
        The basic idea is that I collect all possible combinations (2**n), then I drop those one where the weight limit exceeds.
        Afterwards I just order the solutions and pick the first one.
        If you think about it the problem is obvious, the time consumed is exponantialy increasing 
        therefore a smarter way has to be found.
        There is a few possible fixing and optimization but it would change the time enough
        This is a pure BruteForce algorithm 
        '''
        # This loop collects all of the combinations
        all_combinations = []
        for r in range(len(self.treasures)+1):
            all_combinations.extend(itertools.combinations(self.treasures, r))
        
        valid_combos = [combo for combo in all_combinations if sum(t.weight for t in combo) <= self.size]
        valid_combos.sort(key=lambda combo: sum(t.value for t in combo), reverse=True)

        return valid_combos[0]
    
    def Backtrack(self, index, current_weight, current_value, current_combo, best_result):
        '''Explanation:
        ...
        '''
        if current_weight > self.size:
            return
        if current_value > best_result['value']:
            best_result['value'] = current_value
            best_result['combo'] = current_combo[:]

        for i in range(index, len(self.treasures)):
            t = self.treasures[i]
            current_combo.append(t)
            self.Backtrack(i + 1, current_weight + t.weight, current_value + t.value, current_combo, best_result)
            current_combo.pop()  # backtrack
            
    def SecondSolution(self):
        self.OrderByRatio()
        best_result = {'value': 0, 'combo': []}
        self.Backtrack(0, 0, 0, [], best_result)
        return best_result['combo']
        
    def __str__(self):
        result = ''
        result += f'Size of the backpack: {self.size}\n'
        for i in range(len(self.treasures)):
            result += f'Treasure No.{i+1}; Value: {self.treasures[i].value} / Weight: {self.treasures[i].weight} = Ratio: {round(self.treasures[i].ratio, 2)}\n'
        return result
    
    # def __str__(self):
    #     treasure_lines = [
    #         f'Treasure No.{i}; Value: {t.value} / Weight: {t.weight} = Ratio: {round(t.ratio, 2)}'
    #         for i, t in enumerate(self.treasures)
    #     ]
    #     return f'Size of the backpack: {self.size}\n' + '\n'.join(treasure_lines)

    
Bp = Backpack(100, 11, 15, 9, 17, 40, 60)
Bp.Generate()
print(Bp.size)
# Time FirstSolution (Brute Force)
# start_brute = time.time()
# brute_solution = Bp.FirstSolution()
# end_brute = time.time()
# brute_value = sum(t.value for t in brute_solution)
# brute_weight = sum(t.weight for t in brute_solution)
# brute_time = end_brute - start_brute
# print(f"Brute Force\nTime (s): {round(brute_time, 6)}\nTotal Value{brute_value}\nTotal Weight {brute_weight}\n")

# Time SecondSolution (Backtracking)
start_backtrack = time.time()
backtrack_solution = Bp.SecondSolution()
end_backtrack = time.time()
backtrack_value = sum(t.value for t in backtrack_solution)
backtrack_weight = sum(t.weight for t in backtrack_solution)
backtrack_time = end_backtrack - start_backtrack
print(f"Backtracking\nTime (s): {round(backtrack_time, 6)}\nTotal Value: {backtrack_value}\nTotal Weight: {backtrack_weight}")

'''
Testing in terms of yes
from 20 items till 50 items (n)
weight of the treasures: n*0.8/n*1,2
size of the bag: n*0.8*8/n*1,2*8
value for a treasure n*0.9; n*2
statistical data:
mean
standard deviation
anything basically
'''