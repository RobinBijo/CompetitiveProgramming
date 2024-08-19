'''
DefaultDict
'''
from collections import defaultdict
a, b = map(int, input().split())
d = defaultdict(list)
for i in range(a):
    d['first'].append(input())
for i in range(b):
    d['second'].append(input())

for i in d['second']:
    result = []
    for j in range(len(d['first'])):
        if i == d['first'][j]:
            result.append(str(j+1))
    if len(result) == 0:
        result.append(str(-1))
    print(' '.join(result))

'''
Named Tuple Program
'''
import math
from collections import namedtuple
N = int(input())
columns = input().split()
x = int(columns.index('MARKS'))
sumy = 0
for i in range(N):
    rec = input().split()
    mark = int(rec[x])
    sumy+= mark
avg = sumy/N
print(round(avg,3))
