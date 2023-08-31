from itertools import combinations

little = [0] * 9
for i in range(9):
    little[i] = int(input())
comb = list(combinations(little,7))

sum = 0
value = [0]*7
for std in comb:
    for i in range(7):
        sum += std[i]
    if sum == 100:
        value = list(std)
        break
    else:
        sum = 0
value.sort()
for i in value:
    print(i)