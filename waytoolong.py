# http://codeforces.com/problemset/problem/71/A

n = input()
for i in range(n):
    word = raw_input()
    word_length = len(word)
    if word_length > 10:
        print (word[0] + str(word_length - 2) + word[word_length - 1])
    else:
        print (word)
