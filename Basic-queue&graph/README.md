## 10845 ����

������ �����ϴ� ť��?������ ����, �Է����� �־����� ����� ó���ϴ� ���α׷��� �ۼ��Ͻÿ�.

����� �� ���� �����̴�.

- push X: ���� X�� ť�� �ִ� �����̴�.
- pop: ť���� ���� �տ� �ִ� ������ ����, �� ���� ����Ѵ�. ���� ť�� ����ִ� ������ ���� ��쿡�� -1�� ����Ѵ�.
- size: ť�� ����ִ� ������ ������ ����Ѵ�.
- empty: ť��?��������� 1, �ƴϸ� 0�� ����Ѵ�.
- front: ť�� ���� �տ� �ִ� ������ ����Ѵ�. ���� ť�� ����ִ� ������ ���� ��쿡�� -1�� ����Ѵ�.
- back:?ť�� ���� �ڿ� �ִ� ������ ����Ѵ�. ���� ť�� ����ִ� ������ ���� ��쿡�� -1�� ����Ѵ�.

## �Է�

ù° �ٿ� �־����� ����� �� N (1 �� N �� 10,000)�� �־�����. ��° �ٺ��� N���� �ٿ��� ����� �ϳ��� �־�����. �־����� ������ 1���� ũ�ų� ����, 100,000���� �۰ų� ����. ������ �������� ���� ����� �־����� ���� ����.

## ���

����ؾ��ϴ� ����� �־��� ������, �� �ٿ� �ϳ��� ����Ѵ�.

## ���� �Է� 1

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

## ���� ��� 1

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

ó�� �Է¿��� ���� ��ɾ ������ ���� if������ �´� ��ɾ ã�Ƴ���.

�� ������ �ش� ��ɾ �°� pop()�̳� append�� �ε��� ��ȣ�� �����ؼ� �ۼ��ϸ� �ȴ�.

## 10866 ����

������ �����ϴ� ��(Deque)�� ������ ����, �Է����� �־����� ����� ó���ϴ� ���α׷��� �ۼ��Ͻÿ�.

����� �� ���� �����̴�.

- push_front X: ���� X�� ���� �տ� �ִ´�.
- push_back X: ���� X�� ���� �ڿ� �ִ´�.
- pop_front: ���� ���� �տ� �ִ� ���� ����, �� ���� ����Ѵ�. ����, ���� ����ִ� ������ ���� ��쿡�� -1�� ����Ѵ�.
- pop_back: ���� ���� �ڿ�?�ִ� ���� ����, �� ���� ����Ѵ�. ����, ���� ����ִ� ������ ���� ��쿡�� -1�� ����Ѵ�.
- size: ���� ����ִ� ������ ������ ����Ѵ�.
- empty: ���� ��������� 1��, �ƴϸ� 0�� ����Ѵ�.
- front: ���� ���� �տ� �ִ� ������ ����Ѵ�. ���� ���� ����ִ� ������ ���� ��쿡�� -1�� ����Ѵ�.
- back: ���� ���� �ڿ� �ִ� ������ ����Ѵ�.?���� ���� ����ִ� ������ ���� ��쿡�� -1�� ����Ѵ�.

## �Է�

ù° �ٿ� �־����� ����� �� N (1 �� N �� 10,000)�� �־�����. ��° �ٺ��� N���� �ٿ��� ����� �ϳ��� �־�����. �־����� ������ 1���� ũ�ų� ����, 100,000���� �۰ų� ����. ������ �������� ���� ����� �־����� ���� ����.

## ���

����ؾ��ϴ� ����� �־��� ������, �� �ٿ� �ϳ��� ����Ѵ�.

## ���� �Է� 1

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

## ���� ��� 1

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

���̼� deque ����� Ȱ���� �����̴�. deque�� �迭 �հ� �� �� �� ���� append�� �� �ְ�, ���������� �� �� �ִ�. 

���� ���� ���ð� ť�� ������ ��� �����ϴ� �ڷᱸ����� �� �� �ִ�. ������ ���� ��ȯ�̳� empty���δ� ���ð� ťó�� �����ϸ� �ȴ�.

## 13023 ����

BOJ �˰��� ķ������ �� N���� �����ϰ� �ִ�. ������� 0������ N-1������ ��ȣ�� �Ű��� �ְ�, �Ϻ� ������� ģ���̴�.

������ ������ ���� ģ�� ���踦 ���� ��� A, B, C, D, E�� �����ϴ��� ���غ����� �Ѵ�.

- A�� B�� ģ����.
- B�� C�� ģ����.
- C�� D�� ģ����.
- D�� E�� ģ����.

���� ���� ģ�� ���谡 �����ϴ��� ���ϴ��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

## �Է�

ù° �ٿ� ����� �� N (5 �� N �� 2000)�� ģ�� ������ �� M (1 �� M �� 2000)�� �־�����.

��° �ٺ��� M���� �ٿ��� ���� a�� b�� �־�����, a�� b�� ģ����� ���̴�. (0 �� a, b �� N-1, a �� b) ���� ģ�� ���谡 �� �� �̻� �־����� ���� ����.

## ���

������ ���ǿ� �´� A, B, C, D, E�� �����ϸ� 1�� ������ 0�� ����Ѵ�.

## ���� �Է� 1

```
5 4
0 1
1 2
2 3
3 4
```

## ���� ��� 1

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

dfs�� �̿��ϴ� ��Ʈ��ŷ �����̴�. ģ�� ���谡 �ټ� �� �̻� �����ؾ� �ϹǷ� dfs�� ���̰� 5���� �̷���� �ִ� �� Ȯ���غ���.

�� �� ���� �������� ���� ���̸� �ٸ��� Ž���� �� �����Ƿ� �ݺ������� �ѹ� �� �����ش�.

## 11724 ����

���� ���� �׷����� �־����� ��, ���� ��� (Connected Component)�� ������ ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

## �Է�

ù° �ٿ� ������ ���� N�� ������ ���� M�� �־�����. (1 �� N �� 1,000, 0 �� M �� N��(N-1)/2) ��° �ٺ��� M���� �ٿ� ������ �� ���� u�� v�� �־�����. (1 �� u, v �� N, u �� v) ���� ������ �� ���� �־�����.

## ���

ù° �ٿ� ���� ����� ������ ����Ѵ�.

## ���� �Է� 1

```
6 5
1 2
2 5
5 1
3 4
4 6
```

## ���� ��� 1

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

dfs�� �̿��Ͽ� Ǯ����. bfs�� Ǫ�� ����� ������ ���� ���� ���������� �������� ���� dfs����. ���� ���� ������ Ǯ��� �����ߴ��� ��Ÿ�� ������ ����. ������ ��� ã�ƺ��� ���۸��� �� �� ���, ���̽��� ��� ������ �ɷ� �־� ���� �̻��� ��� �Լ��� ���� �ð� �ʰ��� �ȴٴ� ���̴�. �׷��� `sys.setrecursionlimit(10**7)` �ڵ带 ���� ����� ������ Ǯ���־���.

## 1707 ����

�׷����� ������ ������ �ѷ� �����Ͽ�, �� ���տ� ���� ���������� ���� �������� �ʵ��� ������ �� ���� ��, �׷��� �׷����� Ư���� �̺� �׷��� (Bipartite Graph) �� �θ���.

�׷����� �Է����� �־����� ��, �� �׷����� �̺� �׷������� �ƴ��� �Ǻ��ϴ� ���α׷��� �ۼ��Ͻÿ�.

## �Է�

�Է��� ���� ���� �׽�Ʈ ���̽��� �����Ǿ� �ִµ�, ù° �ٿ� �׽�Ʈ ���̽��� ���� K�� �־�����. �� �׽�Ʈ ���̽��� ù° �ٿ��� �׷����� ������ ���� V�� ������ ���� E�� �� ĭ�� ���̿� �ΰ� ������� �־�����. �� �������� 1���� V���� ���ʷ� ��ȣ�� �پ� �ִ�. �̾ ��° �ٺ��� E���� �ٿ� ���� ������ ���� ������ �־����µ�, �� �ٿ� ������ �� ������ ��ȣ u, v (u �� v)�� �� ĭ�� ���̿� �ΰ� �־�����.

## ���

K���� �ٿ� ���� �Է����� �־��� �׷����� �̺� �׷����̸� YES, �ƴϸ� NO�� ������� ����Ѵ�.

## ����

- 2 �� K �� 5
- 1 �� V �� 20,000
- 1 �� E �� 200,000

## ���� �Է� 1

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

## ���� ��� 1

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
    color[start] = 1  # ó�� ������ 1�� �׷�
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if color[neighbor] == 0:
                color[neighbor] = -color[node]  # ������ ������ �ݴ� �׷�����
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

    result = "YES"  # �⺻������ YES�� �ʱ�ȭ
    for i in range(1, V + 1):
        if color[i] == 0:
            result = bfs(i, graph, color)
            if result == "NO":
                break

    print(result)
```

### Solution

bfs�� Ǯ����. visit��� ������ ����� ������ �ٸ��� �ϴ� �� ��ǥ�̹Ƿ� color��� ����Ʈ�� �ϳ� �߰��ߴ�. bfs�� ��ȸ�ϸ鼭 ���� ����Ʈ ��ȣ�� 0�̸� ���� �湮���� �ʾҴٴ� ���̹Ƿ� ���� ����� �ݴ� �׷쿡 ���� �ִ´�. ������ �װ��� �ƴ϶�� �̹� �湮�ߴٴ� ���̰�, �װ��� ���� �������� �׷� ��ȣ�� ��ġ �ؾ� �Ѵ�.

���� �� ���� ������ �߰��� �ۼ����ְ� ��߳� ��, ��NO���� ��ȯ���ش�.

## 2667 ����

<�׸� 1>�� ���� ���簢�� ����� ������ �ִ�. 1�� ���� �ִ� ����, 0�� ���� ���� ���� ��Ÿ����. ö���� �� ������ ������ ����� ���� ������ ������ �����ϰ�, ������ ��ȣ�� ���̷� �Ѵ�. ���⼭ ����Ǿ��ٴ� ���� � ���� �¿�, Ȥ�� �Ʒ����� �ٸ� ���� �ִ� ��츦 ���Ѵ�. �밢���� ���� �ִ� ���� ����� ���� �ƴϴ�. <�׸� 2>�� <�׸� 1>�� �������� ��ȣ�� ���� ���̴�. ������ �Է��Ͽ� �������� ����ϰ�, �� ������ ���ϴ� ���� ���� ������������ �����Ͽ� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.

!https://www.acmicpc.net/upload/images/ITVH9w1Gf6eCRdThfkegBUSOKd.png

## �Է�

ù ��° �ٿ��� ������ ũ�� N(���簢���̹Ƿ� ���ο� ������ ũ��� ������ 5��N��25)�� �Էµǰ�, �� ���� N�ٿ��� ���� N���� �ڷ�(0Ȥ�� 1)�� �Էµȴ�.

## ���

ù ��° �ٿ��� �� �������� ����Ͻÿ�. �׸��� �� ������ ���� ���� ������������ �����Ͽ� �� �ٿ� �ϳ��� ����Ͻÿ�.

## ���� �Է� 1

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

## ���� ��� 1

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

bfs�� Ǯ����. �ش� ��,���� �湮�ϰ� �Ǹ� �� ������ ���� �� ������ ���ɴ�.

���� �ְ�, group������ �Ǿ� ���� ������, ������ ����� �ʴ� ��� �ش� ���� q�� append�ϰ� bfsŽ���� �̾� ������. 

num ������ �����Ͽ� ���� �׷�ȭ �Ѵ�. ���� �׷쿡 �� ���� ���� ������ count�� ������Ű�� ��������� �����Ͽ� result ����Ʈ�� �ִ´�. 

���������� result�� �����ϰ� ����ϸ� �ȴ�.

## 2178 ����

N��Mũ���� �迭�� ǥ���Ǵ� �̷ΰ� �ִ�.

| 1 | 0 | 1 | 1 | 1 | 1 |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 1 | 1 |

�̷ο��� 1�� �̵��� �� �ִ� ĭ�� ��Ÿ����, 0�� �̵��� �� ���� ĭ�� ��Ÿ����. �̷��� �̷ΰ� �־����� ��, (1, 1)���� ����Ͽ� (N, M)�� ��ġ�� �̵��� �� ������ �ϴ� �ּ��� ĭ ���� ���ϴ� ���α׷��� �ۼ��Ͻÿ�. �� ĭ���� �ٸ� ĭ���� �̵��� ��, ���� ������ ĭ���θ� �̵��� �� �ִ�.

���� �������� 15ĭ�� ������ (N, M)�� ��ġ�� �̵��� �� �ִ�. ĭ�� �� ������ ���� ��ġ�� ���� ��ġ�� �����Ѵ�.

## �Է�

ù° �ٿ� �� ���� N, M(2 �� N, M �� 100)�� �־�����. ���� N���� �ٿ��� M���� ������ �̷ΰ� �־�����. ������ ������?**�پ**?�Է����� �־�����.

## ���

ù° �ٿ� ������ �ϴ� �ּ��� ĭ ���� ����Ѵ�. �׻� ������ġ�� �̵��� �� �ִ� ��츸 �Է����� �־�����.

## ���� �Է� 1

```
4 6
101111
101010
101011
111011
```

## ���� ��� 1

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

���������� bfs�Լ��� �̿��Ͽ���. 

(1,1)�� root�� ��� x,y�� ���� +/- 1�� �ϸ鼭 4���� ������ ���ƺ����� �Ѵ�. �� ��, �湮�ߴ� ������, �׸��� �̷� ���� �ȿ� �ִ� ���� �������� �ɾ��ش�. �ش� ������ ��� �����ϸ� q�� �־��ش�.

ť���� �� level �� ���� count�� 1�� �����ش�. ���̸� ���� �����̴�.

bfs�� Ž���Ͽ� �ᱹ ���ϴ� �������� �����ϰ� �ȴٸ�, ���� ���� �湮�ϰ� �� ����� ���̰� �ּ� ���̰� �� ���̱� �����̴�.

## 7576 ����

ö���� �丶�� ���忡���� �丶�並 �����ϴ� ū â�� ������ �ִ�. �丶��� �Ʒ��� �׸��� ���� ���� ��� ������ ĭ�� �ϳ��� �־ â�� �����Ѵ�.

https://upload.acmicpc.net/de29c64f-dee7-4fe0-afa9-afd6fc4aad3a/-/preview/

â�� �����Ǵ� �丶��� �߿��� �� ���� �͵� ������, ���� ���� ���� �丶��鵵 ���� �� �ִ�. ���� �� �Ϸ簡 ������, ���� �丶����� ������ ���� �ִ� ���� ���� �丶����� ���� �丶���� ������ �޾� �Ͱ� �ȴ�. �ϳ��� �丶���� ������ ���� ����, ������, ��, �� �� ���⿡ �ִ� �丶�並 �ǹ��Ѵ�. �밢�� ���⿡ �ִ� �丶��鿡�Դ� ������ ���� ���ϸ�, �丶�䰡 ȥ�� ������ �ʹ� ���� ���ٰ� �����Ѵ�. ö���� â�� ������ �丶����� ��ĥ�� ������ �� �Ͱ� �Ǵ���, �� �ּ� �ϼ��� �˰� �;� �Ѵ�.

�丶�並 â�� �����ϴ� ���ڸ���� ���ڵ��� ũ��� ���� �丶���� ���� ���� �丶����� ������ �־����� ��, ��ĥ�� ������ �丶����� ��� �ʹ���, �� �ּ� �ϼ��� ���ϴ� ���α׷��� �ۼ��϶�. ��, ������ �Ϻ� ĭ���� �丶�䰡 ������� ���� ���� �ִ�.

## �Է�

ù �ٿ��� ������ ũ�⸦ ��Ÿ���� �� ���� M,N�� �־�����. M�� ������ ���� ĭ�� ��, N�� ������ ���� ĭ�� ���� ��Ÿ����. ��, 2 �� M,N �� 1,000 �̴�. ��° �ٺ��ʹ� �ϳ��� ���ڿ� ����� �丶����� ������ �־�����. ��, ��° �ٺ��� N���� �ٿ��� ���ڿ� ��� �丶���� ������ �־�����. �ϳ��� �ٿ��� ���� �����ٿ� ����ִ� �丶���� ���°� M���� ������ �־�����. ���� 1�� ���� �丶��, ���� 0�� ���� ���� �丶��, ���� -1�� �丶�䰡 ������� ���� ĭ�� ��Ÿ����.

�丶�䰡 �ϳ� �̻� �ִ� ��츸 �Է����� �־�����.

## ���

�������� �丶�䰡 ��� ���� �������� �ּ� ��¥�� ����ؾ� �Ѵ�. ����, ����� ������ ��� �丶�䰡 �;��ִ� �����̸� 0�� ����ؾ� �ϰ�, �丶�䰡 ��� ������ ���ϴ� ��Ȳ�̸� -1�� ����ؾ� �Ѵ�.

## ���� �Է� 1

```
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
```

## ���� ��� 1

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

bfs�� �ּҰ��� ã�Ҵ�.

�丶�䰡 ���� (1) ������ ���� ã�Ƽ� queue�ȿ� �ִ´�. �� �� popleft()�� �ϸ鼭 �ϳ��� ������ ������ �丶����� ���캻��. �� �� Ž�� �ε����� ���� �ȿ� �ִ���, �湮 �ߴ��� ���θ� ���� ���� �Ѵ�. �׸��� �� ���� �丶�䰡 �ִٸ� 1�� �ٲ��ش�.

�̷��� bfs�� Ž���ϸ鼭 ���� level�� �ִ� ������ ���� Ž���ϸ� ���� count�� 1�� �����ش�. ������ ������ ��¥ ���� �����ϱ� �����̴�.

bfsŽ���� ���� �Ŀ��� tomato �ڽ� �ȿ� �� ���� �丶�䰡 �ִ� �� Ž���Ѵ�. 0�� �߰ߵ� �ÿ��� -1 �� ��ȯ�ϰ�, �׷��� ���� ��쿡�� count ���� ���� ��ȯ�Ѵ�.

## 7562 ����

ü���� ���� �� ����Ʈ�� ������ �ִ�. ����Ʈ�� �� ���� �̵��� �� �ִ� ĭ�� �Ʒ� �׸��� �����ִ�. ����Ʈ�� �̵��Ϸ��� �ϴ� ĭ�� �־�����. ����Ʈ�� �� �� �����̸� �� ĭ���� �̵��� �� ������?

!https://www.acmicpc.net/upload/images/knight.png

## �Է�

�Է��� ù° �ٿ��� �׽�Ʈ ���̽��� ������ �־�����.

�� �׽�Ʈ ���̽��� �� �ٷ� �̷���� �ִ�. ù° �ٿ��� ü������ �� ���� ���� l(4 ��?l �� 300)�� �־�����. ü������ ũ��� l �� l�̴�. ü������ �� ĭ�� �� ���� �� {0, ..., l-1} �� {0, ..., l-1}�� ��Ÿ�� �� �ִ�. ��° �ٰ� ��° �ٿ��� ����Ʈ�� ���� �ִ� ĭ, ����Ʈ�� �̵��Ϸ��� �ϴ� ĭ�� �־�����.

## ���

�� �׽�Ʈ ���̽����� ����Ʈ�� �ּ� �� ������ �̵��� �� �ִ��� ����Ѵ�.

## ���� �Է� 1

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

## ���� ��� 1

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

bfs�� ������ Ǯ�����ϴ�. �̸� ����Ʈ�� �̵��� �� �ִ� ��θ� ����Ʈ�� ������ �ξ����ϴ�.

**bfs** �Լ��� �ʺ� �켱 Ž��(BFS) �˰����� ����Ͽ� �ִ� ��θ� ã���ϴ�. ������ ����Ʈ�� �̵� ���⿡ ���� ���ο� ��ġ�� �˻��ϰ�, �湮�� ���� ���� ��ȿ�� ��ġ�� ť�� �߰��մϴ�. ť�� �� ������ �̷��� ������ �ݺ��ϰ�, ���������� �ּ� �̵� Ƚ���� ��ȯ�մϴ�.