## 1697 문제

수빈이는 동생과?숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에?있다.?수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

## 입력

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다.?N과 K는 정수이다.

## 출력

수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

## 예제 입력 1

```
5 17

```

## 예제 출력 1

```
4
```

### My code

```python
import collections

N, K = map(int, input().split())
max_position = 2 * max(N, K) + 1  # 큐의 최대 크기를 계산합니다.
visit = [False] * max_position

def hide():
    q = collections.deque()
    q.append(N)
    visit[N] = True
    count = 0
    
    while q:
        size = len(q)
        for i in range(size):
            temp = q.popleft()

            if temp == K:
                return count

            if temp - 1 >= 0 and not visit[temp - 1]:
                q.append(temp - 1)
                visit[temp - 1] = True

            if temp + 1 < max_position and not visit[temp + 1]:
                q.append(temp + 1)
                visit[temp + 1] = True

            if temp * 2 < max_position and not visit[temp * 2]:
                q.append(temp * 2)
                visit[temp * 2] = True

        count += 1

print(hide())
```

### Solution

- **`max_position`** 변수는 큐의 최대 크기를 계산하기 위해 사용됩니다. 큐의 크기는 **`N`**과 **`K`** 중 더 큰 값의 2배에 1을 더한 값입니다. 이렇게 큐를 초기화하면 충분한 공간을 확보할 수 있습니다.
- **`visit`** 리스트는 방문한 위치를 기록하기 위한 불리언 배열로, 처음에 모든 위치를 방문하지 않았다고 표시합니다.
- **`hide`** 함수는 BFS 알고리즘을 사용하여 N에서 K로 이동하기 위한 최소 이동 횟수를 계산합니다. 다음 단계를 수행합니다:
    1. 큐 **`q`**에 시작 위치 **`N`**을 추가하고, 해당 위치를 방문한 것으로 표시합니다.
    2. **`count`** 변수는 현재까지 이동한 횟수를 나타냅니다.
    3. 큐가 비어있지 않은 동안 다음을 반복합니다:
        - 큐에서 현재 위치 **`temp`**를 가져옵니다.
        - 만약 **`temp`**가 목표 위치인 **`K`**와 같다면, 현재까지의 이동 횟수인 **`count`**를 반환합니다.
        - 그렇지 않으면, **`temp`**에서 이동할 수 있는 위치를 검사합니다.
        - **`temp - 1`**, **`temp + 1`**, **`temp * 2`** 모두 유효한 위치이며 방문하지 않았을 때 큐에 추가하고 해당 위치를 방문한 것으로 표시합니다.
    4. 큐에서 위치를 빼낼 때마다 **`count`**를 증가시키고, 반복을 계속합니다.
- 마지막으로 **`hide()`** 함수를 호출하고 그 결과를 출력합니다. 이 결과는 N에서 K로 이동하기 위한 최소 이동 횟수입니다.

## 13913 문제

수빈이는 동생과?숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에?있다.?수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

## 입력

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다.?N과 K는 정수이다.

## 출력

첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

## 예제 입력 1

```
5 17
```

## 예제 출력 1

```
4
5 10 9 18 17
```

### Code

```python
import collections

N, K = map(int, input().split())
max_position = 2 * max(N, K) + 1  # 큐의 최대 크기를 계산합니다.
visit = [False] * max_position
check = [0] * max_position

def move(current,count):
    position = []
    temp = current
    for _ in range(count):
        position.append(temp)
        temp = check[temp]
    position.append(N)
    print(count)
    print(' '.join(map(str,position[::-1])))

def hide():
    q = collections.deque()
    q.append(N)
    visit[N] = True
    count = 0
    
    while q:
        size = len(q)
        for i in range(size):
            temp = q.popleft()

            if temp == K:
                move(temp,count)
                return

            if temp - 1 >= 0 and not visit[temp - 1]:
                q.append(temp - 1)
                visit[temp - 1] = True
                check[temp - 1] = temp

            if temp + 1 < max_position and not visit[temp + 1]:
                q.append(temp + 1)
                visit[temp + 1] = True
                check[temp + 1] = temp

            if temp * 2 < max_position and not visit[temp * 2]:
                q.append(temp * 2)
                visit[temp * 2] = True
                check[temp * 2] = temp
        count += 1

hide()
```

### Solution

기존 BFS문제와 동일하다. 차이가 있다면 기존에 거쳐왔던 노드들을 기억하고 있어야 한다는 점이다.

이것은 이진 트리가 아니기 때문에 i//2번째로 일반적인 부모 노드 접근은 불가하다. 따라서 임의의 배열을 선언하고 그 배열 안 현재 노드의 인덱스 값 안에 이 전 부모 노드의 번호를 넣는 형식으로 저장한다. 

이것은 temp == K가 성립 될 때, check 배열을 되돌아간다.

## 14226 문제

영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.

영선이는 이미 화면에 이모티콘 1개를 입력했다. 이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.

1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
3. 화면에 있는 이모티콘 중 하나를 삭제한다.

모든 연산은 1초가 걸린다. 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다. 클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다. 또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다. 화면에 이모티콘을 붙여넣기 하면, 클립보드에?있는 이모티콘의 개수가 화면에 추가된다.

영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 S (2 ≤ S ≤ 1000) 가 주어진다.

## 출력

첫째 줄에 이모티콘을 S개 만들기?위해 필요한 시간의 최솟값을 출력한다.

## 예제 입력 1

```
2

```

## 예제 출력 1

```
2
```

### Code

```python
import collections

S = int(input())
visit = [[False] * (S + 1) for _ in range(S + 1)]  # 화면에 i개, 클립보드에 j개 이모티콘 있는지 체크
q = collections.deque()
q.append((1, 0, 0))  # 화면에 1개 있는 상태에서 시작

while q:
    screen, clipboard, time = q.popleft()
    
    # 이모티콘 개수가 S개가 되면 최소 시간 출력
    if screen == S:
        print(time)
        break
    
    # 복사 연산
    if not visit[screen][screen]:
        q.append((screen, screen, time + 1))
        visit[screen][screen] = True
    
    # 붙여넣기 연산
    if clipboard > 0 and screen + clipboard <= S and not visit[screen + clipboard][clipboard]:
        q.append((screen + clipboard, clipboard, time + 1))
        visit[screen + clipboard][clipboard] = True
    
    # 삭제 연산
    if screen > 0 and not visit[screen - 1][clipboard]:
        q.append((screen - 1, clipboard, time + 1))
        visit[screen - 1][clipboard] = True
```

### Solution

BFS로 문제를 해결하였다.

visit 방문을 2차원 배열로 만들었다. [화면][클립] 이렇게 값을 대입하고 탐색 유무를 판단한다.

화면과 클립의 값을 튜플로 만들어 queue에 넣는다. 큐에서 pop한 것을 위와 같이 복사, 붙여 넣기, 삭제 연산을 실행한다.

## 13549 문제

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

## 입력

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

## 출력

수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

## 예제 입력 1

```
5 17

```

## 예제 출력 1

```
2
```

### Code

```python
import collections

N, K = map(int, input().split())
max_position = 2 * max(N, K) + 1  # 큐의 최대 크기를 계산합니다.
visit = [False] * max_position

def hide():
    q = collections.deque()
    q.append((N,0))
    visit[N] = True
    
    while q:
        size = len(q)
        for i in range(size):
            temp, time = q.popleft()

            if temp == K:
                return time
            if temp * 2 < max_position and not visit[temp * 2]:
                q.append((temp * 2,time))
                visit[temp * 2] = True

            if temp - 1 >= 0 and not visit[temp - 1]:
                q.append((temp - 1,time+1))
                visit[temp - 1] = True

            if temp + 1 < max_position and not visit[temp + 1]:
                q.append((temp + 1,time+1))
                visit[temp + 1] = True

print(hide())
```

### Solution

기존 숨바꼭질 문제와 동일하게 BFS로 풀었다. 앞 뒤로 움직일 때와, 순간 이동 할 때의 시간 값을 다르게 계산해야 하므로 q에 넣을 때 시간까지 같이 넣어준다.  그리고 순간 이동 연산 시, time값을 업데이트 하지 않고 그대로 넣어준다.

이 때 주의할 점이 기존 숨바꼭질 문제에서는 뒤, 앞, 순간 이동 순서로 코드를 구현하여도 문제가 없었다. 하지만 이번 문제에서는 순간 이동 시간이 0초이므로 나중에 연산을 하면 앞 뒤로 움직이는 연산들이 time변수를 계속 건들기 때문에 꼬일 수가 있다. 따라서 순간 이동 연산을 제일 앞으로 보내버리면 순간 이동 연산부터 하고 나머지 연산을 수행하기 때문에, 위와 같은 오류를 막을 수 있다.

## 1261 문제

알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 미로는 빈 방?또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.

알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.

만약 이 문제가?[알고스팟](https://www.algospot.com/)에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 안타깝게도 이 문제는?[Baekjoon Online Judge](https://www.acmicpc.net/)에 수록되어 있기 때문에, sudo를 사용할 수 없다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다. 0은 빈 방을 의미하고, 1은?벽을 의미한다.

(1, 1)과 (N, M)은 항상 뚫려있다.

## 출력

첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력한다.

## 예제 입력 1

```
3 3
011
111
110
```

## 예제 출력 1

```
3
```

### Code

```python
import collections

def bfs():
    visit[0][0] = True
    q = collections.deque()
    q.append((0, 0, 0))
    while q:
        size = len(q)
        for _ in range(size):
            (x, y, time) = q.popleft()
            if (x, y) == (N - 1, M - 1):
                return time
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.appendleft((nx, ny, time))
                elif 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    arr[nx][ny] = 0
                    q.append((nx, ny, time+1))

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
print(bfs())
```

### Solution

BFS로 문제를 접근하였다. 

1. **`visit`** 배열은 각 위치를 방문했는지 여부를 표시하는 배열입니다.
2. 큐 **`q`**를 사용하여 너비 우선 탐색을 수행합니다. 미로의 시작 위치 **`(0, 0)`**과 시간 0을 큐에 추가하고, 해당 위치를 방문한 것으로 표시합니다.
3. 큐에서 하나의 노드를 꺼낸 후, 목표 지점 **`(N - 1, M - 1)`**에 도달했는지 확인합니다. 도달했다면 해당 시간을 반환하고 종료합니다.
4. 현재 위치에서 상하좌우로 이동할 수 있는지 확인하고, 가능한 경우 큐에 추가합니다. 이 때, 벽인 경우 벽을 부수고 빈 공간으로 변경하며 시간을 1 증가시킵니다.
5. 큐가 빌 때까지 위 과정을 반복하고, 마지막에 도달한 목표 지점까지 걸린 시간을 반환합니다.

탐색을 시작할 때, 시간을 최소화 하기 위해서는 ‘0’, 즉 길이 뚫려있는 곳을 우선적으로 탐색해야 한다. 따라서 ‘0’을 탐색할 시 queue에 appendleft를 하여 우선적으로 탐색하게 끔 한다.