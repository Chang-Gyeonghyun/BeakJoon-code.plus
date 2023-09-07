from collections import deque
import sys

deq = deque()
n = int(input())

for i in range(n):
    inst = sys.stdin.readline().split()

    if inst[0] == "push_front":
        deq.appendleft(inst[1])
    elif inst[0] == "push_back":
        deq.append(inst[1])
    elif inst[0] == "pop_front":
        if deq:
            print(deq[0])    
            deq.popleft()
        else:
            print("-1")
    elif inst[0] == "pop_back":
        if deq:
            print(deq[-1])    
            deq.pop()
        else:
            print("-1")
    elif inst[0] == "size":
        print(len(deq))
    elif inst[0] == "empty":
        if deq:
            print("0")
        else:
            print("1")
    elif inst[0] == "front":
        if deq:
            print(deq[0])
        else:
            print("-1")
    elif inst[0] == "back":
        if deq:
            print(deq[-1])
        else:
            print("-1")