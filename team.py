# http://codeforces.com/problemset/problem/231/A

n = input()
count = 0

for case in range(n):
    if sum(map(int, raw_input().split(' '))) > 1:
        count += 1

print (count)
