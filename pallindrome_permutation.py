string = input()                  # Reading input from STDIN
#print('Hi, %s.' % name)         # Writing output to STDOUT

d = {}

for c in string:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

count_1 = 0
for value in d.values():
    if count_1 > 1:
        print("NO")
        exit()
    if value%2 == 1:
        count_1 += 1
print("YES")
