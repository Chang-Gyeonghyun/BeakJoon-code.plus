import collections, sys
sys.setrecursionlimit(10**7)
N, M = map(int,input().split())

visit = [False for _ in range(N+1)]
graph = collections.defaultdict(list)
for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(current):
    visit[current] = True
    for i in graph[current]:
        if not visit[i]:
            dfs(i)
            
            
count = 0
for i in range(1,N+1):
    if not visit[i]:
        dfs(i)
        count += 1
    
print(count)