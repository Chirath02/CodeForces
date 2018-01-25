# http://codeforces.com/problemset/problem/118/A

inp_string = raw_input().lower()
vowels = ['a', 'o', 'y', 'e', 'u', 'i']

out = ''

for letter in inp_string:
    if letter not in vowels:
        out += '.' + letter

print (out)
