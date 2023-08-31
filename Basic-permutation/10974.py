N = int(input())
stack = []
def number():
    if len(stack) == N:
        print(" ".join(map(str,stack)))
    for i in range(1,N+1):
        if i not in stack:
            stack.append(i)
            number()
            stack.pop()
number()