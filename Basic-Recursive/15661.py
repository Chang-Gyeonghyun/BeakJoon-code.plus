import sys

N = int(input())
s = [list(map(int,input().split())) for _ in range(N)]


start = []
link = []
result = sys.maxsize
K= 0

def dfs(head,K):
    global link, result
    if len(start) == K:
        link = [ele for ele in range(N) if ele not in start]
        differ = find(start) - find(link)
        result = min(result,abs(differ))
        return
        
    
    
    for i in range(head, N):
        start.append(i)
        dfs(i+1,K)
        start.pop()
        
        
def find(arr:list):
    sum = 0
    for i in arr:
        for j in arr:
            sum += s[i][j]
    return sum

for i in range(1,N//2 +1): #팀원 수 설정 N/2가 넘어갈 경우 기존에 탐색했던 팀원 수와 일치하므로 한번만 하면 된다.
    dfs(0,i)       
    
print(result)