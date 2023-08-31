N = int(input())
arr = list(map(int,input().split()))
stack, numberstack = [], []
maximum = 0
def number():
    global maximum
    if len(stack) == N:
        sum = 0
        for j in range(N-1):
            sum += abs(stack[j] - stack[j+1])
        maximum = max(maximum,sum)
    for idx, i in enumerate(arr):
        if idx not in numberstack:
            numberstack.append(idx)
            stack.append(i)
            number()
            numberstack.pop()
            stack.pop()
number()
print(maximum)