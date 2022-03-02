#I
from collections import defaultdict
s1 = input()
s2 = input()
mapping = defaultdict(set)
for i,v in enumerate(s1[:-1]):
    mapping[v].add((s1[i+1],i))
print(mapping)

res = 1
for i in s2:
    pass