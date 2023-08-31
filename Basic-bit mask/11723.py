import sys
M = int(input())
S = set()

for i in range(M):
    oper = sys.stdin.readline().strip().split()
    if len(oper) != 1:
        value = int(oper[1])
    oper = oper[0]
    if oper == "add":
        S.add(value)
    elif oper == "remove":
        S.discard(value)
    elif oper == "check":
        if value in S:
            print(1)
        else: print(0)
    elif oper == "toggle":
        if value in S:
            S.discard(value)
        else: S.add(value)
    elif oper == "all":
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20} 

    elif oper == "empty":
        S.clear()