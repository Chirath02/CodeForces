# http://codeforces.com/problemset/problem/158/A

n, k = map(int, raw_input().split(' '))
numbers = map(int, raw_input().split(' '))

count = 0

for i in numbers:
    if i > 0 and i >= numbers[k - 1]:
        count += 1

print (count)
