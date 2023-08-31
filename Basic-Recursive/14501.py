import sys

N = int(input())
arr =[]
for i in range(N):
    T, P = map(int,input().split())
    arr.append((T,P))

sum = 0
result = -sys.maxsize

def dfs(start, sum):
    global result
    if start >= len(arr):
        result = max(result, sum)
        return
    
    for i in range(start, N):
        t, p = arr[i]
        if i+t <= len(arr):
            dfs(i+t, sum + p)
        else:
            dfs(i+1, sum)
            
            
            
dfs(0,0)
print(result)