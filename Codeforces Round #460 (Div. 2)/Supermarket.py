# http://codeforces.com/contest/919/problem/A

from operator import itemgetter

n, m = map(int, raw_input().split(" "))

a, b = map(int, raw_input().split(" "))
min_val = (float(a) / b)

for i in range(n - 1):
    a, b = map(int, raw_input().split(" "))
    newMin = (float(a) / b)
    if (newMin < min_val):
        min_val = newMin

print (float(m) * min_val)
