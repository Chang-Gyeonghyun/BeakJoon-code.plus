## 10845 문제

정수를 저장하는 큐를?구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

- push X: 정수 X를 큐에 넣는 연산이다.
- pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- size: 큐에 들어있는 정수의 개수를 출력한다.
- empty: 큐가?비어있으면 1, 아니면 0을 출력한다.
- front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- back:?큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

## 입력

첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

## 출력

출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

## 예제 입력 1

```
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
```

## 예제 출력 1

```
1
2
2
0
1
2
-1
0
1
-1
0
3
```

### Code

```python
import sys

N = int(sys.stdin.readline())

queue = []

for i in range(N):
    inst = sys.stdin.readline().split()

    if inst[0] == "push":
        queue.append(inst[1])

    elif inst[0] == "pop":
        if len(queue) != 0: 
            print(queue.pop(0))
        else: print(-1)

    elif inst[0] == "size":
        print(len(queue))

    elif inst[0] == "empty":
        if len(queue) == 0: 
            print(1)
        else : print(0)

    elif inst[0] == "front":
        if len(queue) != 0: 
            print(queue[0])
        else:
            print(-1)

    elif inst[0] == "back":
        if len(queue) == 0: 
            print(-1)
        else: 
            print(queue[-1])
```

### Solution

처음 입력에서 앞의 명령어만 가져온 다음 if문으로 맞는 명령어를 찾아낸다.

그 다음은 해당 명령어에 맞게 pop()이나 append를 인덱스 번호에 유의해서 작성하면 된다.

## 10866 문제

정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

- push_front X: 정수 X를 덱의 앞에 넣는다.
- push_back X: 정수 X를 덱의 뒤에 넣는다.
- pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- pop_back: 덱의 가장 뒤에?있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- size: 덱에 들어있는 정수의 개수를 출력한다.
- empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
- front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- back: 덱의 가장 뒤에 있는 정수를 출력한다.?만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

## 입력

첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

## 출력

출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

## 예제 입력 1

```
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
```

## 예제 출력 1

```
2
1
2
0
2
1
-1
0
1
-1
0
3
```

### Code

```python
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
```

### Solution

파이선 deque 모듈을 활용한 문제이다. deque는 배열 앞과 끝 둘 다 값을 append할 수 있고, 마찬가지로 뺄 수 있다. 

따라서 덱은 스택과 큐의 연산을 모두 지원하는 자료구조라고 볼 수 있다. 나머지 길이 반환이나 empty여부는 스택과 큐처럼 구현하면 된다.

## 13023 문제

BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.

오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

- A는 B와 친구다.
- B는 C와 친구다.
- C는 D와 친구다.
- D는 E와 친구다.

위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.

## 출력

문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.

## 예제 입력 1

```
5 4
0 1
1 2
2 3
3 4
```

## 예제 출력 1

```
1
```

### code

```python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

relationship = [[] for _ in range(N)]
visited = [False] * N
result = False

for _ in range(M):
    a, b = map(int, input().split())
    relationship[a].append(b)
    relationship[b].append(a)

def dfs(depth, x):
    global result
    if depth == 4:
        result = True
        return

    for i in relationship[x]:
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i)
            visited[i] = False

for i in range(N):
    visited[i] = True
    dfs(0, i)
    visited[i] = False
    if result:
        break

if result:
    print(1)
else:
    print(0)
```

### Solution

dfs를 이용하는 백트래킹 문제이다. 친구 관계가 다섯 명 이상 존재해야 하므로 dfs로 깊이가 5까지 이루어져 있는 지 확인해본다.

이 때 시작 기준점에 따라 깊이를 다르게 탐색할 수 있으므로 반복문으로 한번 더 돌려준다.

## 11724 문제

방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

## 출력

첫째 줄에 연결 요소의 개수를 출력한다.

## 예제 입력 1

```
6 5
1 2
2 5
5 1
3 4
4 6
```

## 예제 출력 1

```
2
```

### Code

```python
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
    
```

### Solution

dfs를 이용하여 풀었다. bfs로 푸는 방법도 있지만 제일 먼저 직관적으로 생각나는 것이 dfs였다. 막힘 없이 문제를 풀어가고 제출했더니 런타임 에러가 떴다. 이유를 계속 찾아보려 구글링을 해 본 결과, 파이썬은 재귀 제한이 걸려 있어 일정 이상의 재귀 함수를 쓰면 시간 초과가 된다는 것이다. 그래서 `sys.setrecursionlimit(10**7)` 코드를 통해 재귀의 제한을 풀어주었다.

## 1707 문제

그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

## 입력

입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다.

## 출력

K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

## 제한

- 2 ≤ K ≤ 5
- 1 ≤ V ≤ 20,000
- 1 ≤ E ≤ 200,000

## 예제 입력 1

```
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
```

## 예제 출력 1

```
YES
NO
```

### Code

```python
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
```

### Solution

bfs로 풀었다. visit대신 인접한 노드의 색깔을 다르게 하는 게 목표이므로 color라는 리스트를 하나 추가했다. bfs로 순회하면서 색깔 리스트 번호가 0이면 아직 방문하지 않았다는 것이므로 이전 노드의 반대 그룹에 집어 넣는다. 하지만 그것이 아니라면 이미 방문했다는 것이고, 그것이 지금 넣으려는 그룹 번호와 일치 해야 한다.

따라서 그 때의 조건을 추가로 작성해주고 어긋날 시, “NO”를 반환해준다.

## 2667 문제

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

!https://www.acmicpc.net/upload/images/ITVH9w1Gf6eCRdThfkegBUSOKd.png

## 입력

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

## 출력

첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

## 예제 입력 1

```
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```

## 예제 출력 1

```
3
7
8
9
```

### My code

```python
import collections
        
def bfs(col, row, num):
    count = 0
    group[col][row] = num
    q = collections.deque()
    q.append((col, row))
    while q:
        count += 1
        (x, y) = q.popleft()
        if x + 1 < N and arr[x+1][y] == '1' and group[x + 1][y] == 0:
            group[x + 1][y] = num
            q.append((x + 1, y))
        if 0 <= x - 1 and arr[x-1][y] == '1' and group[x - 1][y] == 0:
            group[x - 1][y] = num
            q.append((x - 1, y))
        if y + 1 < N and arr[x][y+1] == '1' and group[x][y + 1] == 0:
            group[x][y + 1] = num
            q.append((x, y + 1))
        if 0 <= y - 1 and arr[x][y-1] == '1' and group[x][y - 1] == 0:
            group[x][y - 1] = num
            q.append((x, y - 1))
    return count

N = int(input())
arr = [list(input()) for _ in range(N)]
group = [[0] * N for _ in range(N)]
result = []

num = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and group[i][j] == 0:
            result.append(bfs(i, j, num))
            num += 1

print(len(result))
for count in sorted(result):
    print(count)
```

### Solution

bfs로 풀었다. 해당 행,열에 방문하게 되면 그 인접한 주위 집 단지를 살핀다.

집이 있고, group설정이 되어 있지 않으며, 단지를 벗어나지 않는 경우 해당 집을 q에 append하고 bfs탐색을 이어 나간다. 

num 변수를 설정하여 집을 그룹화 한다. 집을 그룹에 한 개씩 넣을 때마다 count를 증가시키고 결과값으로 리턴하여 result 리스트에 넣는다. 

최종적으로 result를 정렬하고 출력하면 된다.

## 2178 문제

N×M크기의 배열로 표현되는 미로가 있다.

| 1 | 0 | 1 | 1 | 1 | 1 |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 1 | 1 |

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

## 입력

첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은?**붙어서**?입력으로 주어진다.

## 출력

첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

## 예제 입력 1

```
4 6
101111
101010
101011
111011
```

## 예제 출력 1

```
15
```

### Code

```python
import collections

def bfs():
    count = 0
    visit[0][0] = True
    q = collections.deque()
    q.append((0, 0))
    while q:
        count += 1
        size = len(q)
        for _ in range(size):
            (x, y) = q.popleft()
            if (x, y) == (N - 1, M - 1):
                return count
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '1' and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
print(bfs())
```

### Solution

마찬가지로 bfs함수를 이용하였다. 

(1,1)을 root로 잡고 x,y에 대해 +/- 1씩 하면서 4개의 정점을 돌아보도록 한다. 이 때, 방문했던 곳인지, 그리고 미로 범위 안에 있는 지를 조건으로 걸어준다. 해당 사항이 모두 성립하면 q에 넣어준다.

큐에서 한 level 다 돌면 count를 1씩 더해준다. 깊이를 세는 수단이다.

bfs로 탐색하여 결국 원하던 목적지에 도착하게 된다면, 제일 먼저 방문하게 된 노드의 깊이가 최소 깊이가 될 것이기 때문이다.

## 7576 문제

철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.

https://upload.acmicpc.net/de29c64f-dee7-4fe0-afa9-afd6fc4aad3a/-/preview/

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

## 입력

첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

## 출력

여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

## 예제 입력 1

```
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
```

## 예제 출력 1

```
8
```

### Code

```python
import collections

M, N = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]

def bfs():
    q = collections.deque()
    count = -1
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                q.append((i,j))
    while q:
        count += 1
        
        size = len(q)
        for _ in range(size):
            (x, y) = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    tomato[nx][ny] = 1
                    q.append((nx, ny))
                                 
    for row in tomato:
        for col in row:
            if col == 0:
                return -1
    return count
                    
print(bfs())
```

### Solution

bfs로 최소값을 찾았다.

토마토가 익은 (1) 값들을 전부 찾아서 queue안에 넣는다. 그 후 popleft()를 하면서 하나씩 꺼내어 인접한 토마토들을 살펴본다. 이 때 탐색 인덱스가 범위 안에 있는지, 방문 했는지 여부를 따져 봐야 한다. 그리고 안 익은 토마토가 있다면 1로 바꿔준다.

이렇게 bfs로 탐색하면서 같은 level에 있는 노드들을 전부 탐색하면 깊이 count를 1씩 더해준다. 깊이의 개수가 날짜 수와 동일하기 때문이다.

bfs탐색이 끝난 후에는 tomato 박스 안에 안 익은 토마토가 있는 지 탐색한다. 0이 발견될 시에는 -1 을 반환하고, 그렇지 않은 경우에는 count 깊이 값을 반환한다.

## 7562 문제

체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

!https://www.acmicpc.net/upload/images/knight.png

## 입력

입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤?l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

## 출력

각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

## 예제 입력 1

```
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
```

## 예제 출력 1

```
5
28
0
```

### My code

```python
import collections

K = int(input())
position = [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]

def bfs(xstart, ystart, xend, yend, visit):
    q = collections.deque()
    q.append((xstart, ystart))
    count = -1
    while q:
        count += 1
        size = len(q)
        for _ in range(size):
            (x, y) = q.popleft()
            if (x, y) == (xend, yend):
                return count
            for dx, dy in position:
                nx, ny = x + dx, y + dy
                if 0 <= nx < I and 0 <= ny < I and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))
    

for _ in range(K):
    I = int(input())
    visit = [[False] * I for _ in range(I)]
    xstart, ystart = map(int, input().split())
    xend, yend = map(int, input().split())
    print(bfs(xstart, ystart, xend, yend, visit))
```

### Solution

bfs로 문제를 풀었습니다. 미리 나이트가 이동할 수 있는 경로를 리스트로 지정해 두었습니다.

**bfs** 함수는 너비 우선 탐색(BFS) 알고리즘을 사용하여 최단 경로를 찾습니다. 가능한 나이트의 이동 방향에 따라 새로운 위치를 검사하고, 방문한 적이 없는 유효한 위치를 큐에 추가합니다. 큐가 빌 때까지 이러한 과정을 반복하고, 최종적으로 최소 이동 횟수를 반환합니다.