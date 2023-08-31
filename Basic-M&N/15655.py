N, M = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
stack = []
temp = []

def back(s: list):
    
    if len(stack) == M:
        print(" ".join(map(str, stack)))
        temp.append(set(stack))
        return
        
    for i in arr:
        if i not in stack:
            stack.append(i)
            if set(stack) not in temp:
                back(arr)
                stack.pop()
            else: stack.pop()
            
back(arr)