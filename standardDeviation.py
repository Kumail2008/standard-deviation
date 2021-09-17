import csv
import math
with open('dummyData.csv', newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n    
    return mean

squaredList = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squaredList.append(a)

sum = 0
for i in squaredList:
    sum += i
    print(sum)    

result = sum/(len(data)-1)

stdev = math.sqrt(result)
print(stdev)