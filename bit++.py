# http://codeforces.com/problemset/problem/282/A

number_of_statements = input()

value_of_x = 0

for statement in range(number_of_statements):
    if '+' in raw_input():
        value_of_x += 1
    else:
        value_of_x -= 1

print (value_of_x)
