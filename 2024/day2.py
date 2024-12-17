import numpy as np
from collections import defaultdict

def non_decreasing(L):
    return all(x<y for x, y in zip(L, L[1:]))

def non_increasing(L):
    return all(x>y for x, y in zip(L, L[1:]))

def monotonic(L):
    return non_decreasing(L) or non_increasing(L)

def gradual(L):
    return all(abs(x-y)<=3 for x, y in zip(L, L[1:]))

def safe(L):
    return gradual(L) and monotonic(L)

test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

with open("day_2_input.txt", "r") as ifile:
    real_input = ifile.read()

reports = real_input.split("\n")
levels = [[int(x) for x in r.split(" ") if x] for r in reports]

safety = [safe(r) for r in levels]
for i in range(len(safety)):
    if not safety[i]:
        for j in range(len(levels[i])):
            if safe(levels[i][:j]+levels[i][j+1:]):
                safety[i] = True
                break
print(sum(safety))