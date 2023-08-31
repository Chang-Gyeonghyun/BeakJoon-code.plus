N, M = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
stack = []

def back(s: list):
    
    if len(stack) == M:
        print(" ".join(map(str, stack)))
        return
        
    for i in arr:
        stack.append(i)
        back(arr)
        stack.pop()
            
back(arr)