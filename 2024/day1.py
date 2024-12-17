import numpy as np
from collections import defaultdict

list_1 = []
list_2 = []

with open("day_1_input.txt", 'r') as ifile:
    for l in ifile.readlines():
        a, b = l.split("   ")
        list_1.append(int(a))
        list_2.append(int(b[:-1]))

#list_1 = [3,4,2,1,3,3]
#list_2 = [4,3,5,3,9,3]

list_1.sort()
list_2.sort()

list_1 = np.array(list_1)
list_2 = np.array(list_2)

print(np.sum(np.abs(list_1-list_2)))

counts = defaultdict(int)

n = list(set(list_2))
for k in n:
    counts[k] = list_2.count(k)

print(sum([i * counts[i] for i in list_1]))
