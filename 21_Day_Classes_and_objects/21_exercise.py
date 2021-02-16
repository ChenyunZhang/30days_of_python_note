# 1. Python has the module called _statistics_ and we can use this module to do all the statistical caluculations.
# However to challlenge ourselves, let's try to develop a program,
# which calculates the measure of central tendency of a sample (mean, median, mode)
# and measure of variability (range, variance, standard deviation).
# In addition to those measures,
# find the min, max, count, percentile, and frequency distribution of the sample.
# You can create a class called Statistics and create all the functions that do statistical calculations as methods
# for the Statistics class. Check the output below.
import math

class Statistics:
    def __init__(self, items=[]):
        self.items = items

    def mean(self):
        try:
            return sum(self.items) / len(self.items)
        except:
            return "List is empty"

    def median(self):
        if len(self.items)%2 == 0:
            return self.items[len(self.items)//2:len(self.items)//2+2]
        else:
            return self.items[len(self.items)//2]
        
    def mode(self):
        hash = {}
        for i in self.items:
            if hash.get(i):
                hash[i]+=1
            else:
                hash[i]=1
        sorted_hash = sorted(hash.items(),key=lambda x:x[1],reverse=True)
        return sorted_hash[0][0]
    
    def range(self):
        return max(self.items) - min(self.items)
    
    # To calculate the Variance, take each difference, square it, and then average the result:
    def variance(self):
        arr_sum = 0
        for i in self.items:
            arr_sum+=(i - self.mean()) ** 2
        
        return round(arr_sum/len(self.items),2)
    
    def standard_deviation(self):
        return round(math.sqrt(self.variance()))
        
    def min(self):
        return min(self.items)
    
    def max(self):
        return max(self.items)
    
    def count(self,element):
        hash = {}
        for i in self.items:
            if hash.get(i):
                hash[i]+=1
            else:
                hash[i]=1
        return hash[element]
    
    # percentile, and frequency distribution
ages = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]
data = Statistics(ages)

print(data.mean())
print(data.median())
print(data.mode())
print(data.range())
print(data.count(26))
print(data.variance())
print(data.standard_deviation())

# print('Count:', data.count()) # 25
# print('Sum: ', data.sum()) # 744
# print('Min: ', data.min()) # 24
# print('Max: ', data.max()) # 38
# print('Range: ', data.range() # 14
# print('Mean: ', data.mean()) # 30
# print('Median: ', data.median()) # 29
# print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
# print('Standard Deviation: ', data.std()) # 4.2
# print('Variance: ', data.var()) # 17.5
# print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]


# ```sh
# # you output should look like this
# print(data.describe())
# Count: 25
# Sum:  744
# Min:  24
# Max:  38
# Range:  14
# Mean:  30
# Median:  29
# Mode:  (26, 5)
# Variance:  17.5
# Standard Deviation:  4.2
# Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
# ```

# 2. Create a class called PersonAccount.
# It has
# firstname,
# lastname,
# incomes,
# expenses properties
# and it has total_income,
# total_expense,
# account_info,
# add_income,
# add_expense
# and account_balance methods.
# Incomes is a set of incomes and its description. The same goes for expenses.
