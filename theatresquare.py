# http://codeforces.com/problemset/problem/1/A

from math import ceil

inpt = raw_input().split(" ")
n = int(inpt[0])
m = int(inpt[1])
a = int(inpt[2])

ans = int(ceil(n/float(a))) * int(ceil(m/float(a)))

print (ans)
