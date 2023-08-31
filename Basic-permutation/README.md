## 10972 문제

1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성하시오.

사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.

N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.

- 1, 2, 3
- 1, 3, 2
- 2, 1, 3
- 2, 3, 1
- 3, 1, 2
- 3, 2, 1

## 입력

첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.

## 출력

첫째?줄에 입력으로 주어진 순열의 다음에 오는 순열을 출력한다. 만약, 사전순으로 마지막에 오는 순열인 경우에는 -1을 출력한다.

## 예제 입력 1

```
4
1 2 3 4
```

## 예제 출력 1

```
1 2 4 3
```

### First Solution

```jsx
N = int(input())
arr = list(map(int,input().split()))
value = False
stack = []
def number():
    global value
    if value and len(stack) == N:
        print(" ".join(map(str,stack)))
        value = False
        exit(0)
    if stack == arr:
        value = True
        return
    for i in range(1,N+1):
        if i not in stack:
            stack.append(i)
            number()
            stack.pop()
            
number()
print(-1)
```

- 전에 풀었던 재귀와 백트래킹을 이용해 접근하였다. 하지만 런타임 에러가 났고, 이유를 살펴보니 N의 범위가 방대해 백트래킹으로 풀 수 없는 문제였다. 그래서 다른 로직을 생각해본다.

### Final solution

```python
N = int(input())
arr = list(map(int, input().split()))

def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return []  # 이미 가장 큰 순열인 경우
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = sorted(arr[i+1:])
    return arr

ans = next_permutation(arr)
if ans:
    print(" ".join(map(str, ans)))
else:
    print(-1)
```

<aside>
? i번째 인덱스가 그 다음 인덱스보다 작은 경우를 찾는다. 그 i번째 인덱스가 바로 다음에 교체될 인덱스이다. 해당 인덱스를 다음 리스트의 요소들 중 인덱스보다 한 단계 큰 요소로 교체한 다음, i+1번부터는 순서대로 다시 처음부터 시작하므로 sorted를 통해 정렬한다.

</aside>

## 10973 문제

1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 바로 이전에 오는 순열을 구하는 프로그램을 작성하시오.

사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.

N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.

- 1, 2, 3
- 1, 3, 2
- 2, 1, 3
- 2, 3, 1
- 3, 1, 2
- 3, 2, 1

## 입력

첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.

## 출력

첫째?줄에 입력으로 주어진 순열의 이전에 오는 순열을 출력한다. 만약, 사전순으로 가장 처음에 오는 순열인 경우에는 -1을 출력한다.

## 예제 입력 1

```
4
1 2 3 4
```

## 예제 출력 1

```
-1
```

### Code

```python
N = int(input())
arr = list(map(int, input().split()))

def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] <= arr[i + 1]:
        i -= 1
    if i == -1:
        return []  # 이미 가장 작은 순열일 경우
    j = n - 1
    while arr[j] >= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = sorted(arr[i+1:],reverse=True)
    return arr

ans = next_permutation(arr)
if ans:
    print(" ".join(map(str, ans)))
else:
    print(-1)
```

### Solution

이전 문제와 풀이 방식은 똑같다. 단지 이전 순열이니까 인덱스 비교만 반대로 해주면 된다. 또한 정렬할 때, 오름차순으로 정렬하는 것만 주의해준다.

## 10974 문제

N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다.

## 출력

첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

## 예제 입력 1

```
3
```

## 예제 출력 1

```
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

### My Code

```python
N = int(input())
stack = []
def number():
    if len(stack) == N:
        print(" ".join(map(str,stack)))
    for i in range(1,N+1):
        if i not in stack:
            stack.append(i)
            number()
            stack.pop()
number()
```

### Solution

백트래킹 방법을 이용하여 풀었다.

## 10819 문제

N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

## 입력

첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

## 출력

첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는?식의 최댓값을 출력한다.

## 예제 입력 1

```
6
20 1 15 8 4 10
```

## 예제 출력 1

```
62
```

### My code

```python
N = int(input())
arr = list(map(int,input().split()))
stack, numberstack = [], []
maximum = 0
def number():
    global maximum
    if len(stack) == N:
        sum = 0
        for j in range(N-1):
            sum += abs(stack[j] - stack[j+1])
        maximum = max(maximum,sum)
    for idx, i in enumerate(arr):
        if idx not in numberstack:
            numberstack.append(idx)
            stack.append(i)
            number()
            numberstack.pop()
            stack.pop()
number()
print(maximum)
```

### solution

백트래킹 방법은 똑같다. 다만 이번은 리스트 내에 중복값이 허용이 된다. 따라서 not in stack이 아니라 열거형으로 바꿔서 해당 인덱스가 들어가 있는 지 여부를 판단하여 stack에 값을 집어 넣는다.

## 10971 문제

외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로 computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다. 여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.

1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다. (길이 없을 수도 있다) 이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 단, 한 번 갔던 도시로는 다시 갈 수 없다. (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외) 이런 여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다. 비용은 대칭적이지 않다.?즉, W[i][j] 는 W[j][i]와 다를 수 있다. 모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다. 경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 10) 다음 N개의 줄에는 비용 행렬이 주어진다. 각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다. W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.

항상 순회할 수 있는 경우만 입력으로 주어진다.

## 출력

첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.

## 예제 입력 1

```
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
```

## 예제 출력 1

```
35
```

### First Solution

```python
import sys
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))
stack = []
maximum = sys.maxsize
sum = 0

def number(start, end, count, sum):
    global maximum
    if len(stack) == N:
        sum += arr[end][start]
        maximum = min(maximum,sum)
        return

    for i in range(N):
        if i not in stack:
            stack.append(i)
            number(start, i, count + 1, sum + arr[end][i])
            stack.pop()

for i in range(N):
    number(i,i,0,0)

print(maximum)
```

위 코드는 백트래킹을 이용하여 재귀 용법을 사용하였다. N의 최대값이 얼마 안돼서 한번 시도해보았지만 역시나 시간 초과가 떴다. 다른 dfs방법으로 풀어야 할 것 같아 수정한 코드가 아래이다.

### Second Solution

```python
import sys

def dfs(start, now, value, cnt):
    global ans
    if cnt == N:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return

    if value > ans:
        return

    for i in range(N):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = 0

N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
ans = sys.maxsize
visited = [0] * N
for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(ans)
```

위 코드의 방식은 visited 배열을 이용하여 해당 도시를 방문했는지 여부를 판단한다. in 리스트에서 찾는 것은 O(N)의 시간복잡도가 걸리지만 visited[]을 이용할 경우 시간복잡도가 O(1)로 줄어들기 때문에 시간초과를 막을 수가 있다.

## 6603 문제

독일 로또는 {1, 2, ..., 49}에서 수?6개를 고른다.

로또 번호를 선택하는데 사용되는 가장 유명한 전략은 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.

예를 들어, k=8, S={1,2,3,5,8,13,21,34}인 경우 이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지이다. ([1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34])

집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있다. 첫 번째 수는 k (6 < k < 13)이고, 다음 k개 수는 집합 S에 포함되는 수이다. S의 원소는 오름차순으로 주어진다.

입력의 마지막 줄에는 0이 하나 주어진다.

## 출력

각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 이때, 사전 순으로 출력한다.

각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.

## 예제 입력 1

```
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
```

## 예제 출력 1

```
1 2 3 4 5 6
1 2 3 4 5 7
1 2 3 4 6 7
1 2 3 5 6 7
1 2 4 5 6 7
1 3 4 5 6 7
2 3 4 5 6 7

1 2 3 5 8 13
1 2 3 5 8 21
1 2 3 5 8 34
1 2 3 5 13 21
1 2 3 5 13 34
1 2 3 5 21 34
1 2 3 8 13 21
1 2 3 8 13 34
1 2 3 8 21 34
1 2 3 13 21 34
1 2 5 8 13 21
1 2 5 8 13 34
1 2 5 8 21 34
1 2 5 13 21 34
1 2 8 13 21 34
1 3 5 8 13 21
1 3 5 8 13 34
1 3 5 8 21 34
1 3 5 13 21 34
1 3 8 13 21 34
1 5 8 13 21 34
2 3 5 8 13 21
2 3 5 8 13 34
2 3 5 8 21 34
2 3 5 13 21 34
2 3 8 13 21 34
2 5 8 13 21 34
3 5 8 13 21 34
```

### My code

```python
def dfs(stack):
    if len(stack) == 6:
        print(" ".join(map(str,stack)))
        return
    for i in s:
        if not stack or i > stack[-1]:
            stack.append(i)
            dfs(stack)
            stack.pop()

while True:
    s = list(map(int,input().split()))
    k = s[0]
    s = s[1:]
    if k == 0:
        exit()
    stack = []
    dfs(stack)
    print()
```

### solution

재귀 백트래킹을 이용하여 문제를 접근하였다. 이전에 접했던 유형에서 input만 다르므로 유의해준다.