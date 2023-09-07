import sys
import collections

def bfs(start, graph, color):
    q = collections.deque([start])
    color[start] = 1  # 처음 정점은 1번 그룹
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if color[neighbor] == 0:
                color[neighbor] = -color[node]  # 인접한 정점은 반대 그룹으로
                q.append(neighbor)
            elif color[neighbor] == color[node]:
                return "NO"
    return "YES"

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = collections.defaultdict(list)
    color = [0] * (V + 1)

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    result = "YES"  # 기본적으로 YES로 초기화
    for i in range(1, V + 1):
        if color[i] == 0:
            result = bfs(i, graph, color)
            if result == "NO":
                break

    print(result)
