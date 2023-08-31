import sys

N = int(input())
s = [list(map(int,input().split())) for _ in range(N)]


start = []
link = []
result = sys.maxsize

def dfs(head):
    global link, result
    if len(start) == N/2:
        link = [ele for ele in range(N) if ele not in start]
        differ = find(start) - find(link)
        result = min(result,abs(differ))
        return
        
    
    
    for i in range(head, N):
        start.append(i)
        dfs(i+1)
        start.pop()
        
        
def find(arr:list):
    sum = 0
    for i in arr:
        for j in arr:
            sum += s[i][j]
    return sum
        
dfs(0)
print(result)