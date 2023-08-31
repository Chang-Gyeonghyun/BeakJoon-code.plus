## 15649 문제

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지?자연수 중에서 중복 없이 M개를 고른 수열

## 입력

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

## 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제 입력 1

```
3 1
```

## 예제 출력 1

```
1
2
3
```

## 정답 코드

```jsx
n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()
```

백트래킹은 하나씩 전부 검사해보고 아닐 경우에 다시 되돌아가서 탐색하는 구조이다. 이때 다시 되돌아가기 위해서 가지치기 구조를 띠고, 이는 재귀 함수로 표현할 수 있다.

## 15650 문제

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지?자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

## 입력

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

## 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제 입력 1

```
3 1
```

## 예제 출력 1

```
1
2
3
```

## 답안 코드

```jsx
n,m = list(map(int,input().split()))
 
s = []
 
temp = 0

def dfs():
    global temp
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if (i not in s) and i > temp:
            s.append(i)
            temp = s[-1]
            dfs()
            s.pop()
            if len(s) == 0:
                pass
            else: temp = s[-1]
 
dfs()
```

전에 풀었던 1번 문제에서 조금만 수정 하면 된다. 리스트 안에 값이 있는 지 확인하고 넣어줄 때 그 값이 마지막 인덱스보다 큰 지만 같이 확인해주면 끝난다.

## 문제

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지?자연수 중에서?M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.

## 입력

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

## 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제 입력 1

```
3 1
```

## 예제 출력 1

```
1
2
3
```

## 답안 코드

```python
def n_digit(num, n):
  """
  Express num as a n-number
    
    Args:
        num (int): The original number to be expressed in n digits
        n (int): The base value to represent num
        
    Returns:
        int: num expressed in n digits
  """
  result = 0
  digit = 0
  while num > 0:
    result += (num % n) * (10 ** digit)
    digit += 1
    num //= n
  return result

n, m = map(int, input().split())
upper_bound = n**m
for i in range(upper_bound):
  #print(n_digit(i,n))
  result = str(n_digit(i,n)+(10**m - 1)//9)
  #result_str = '0'*(m - len(result)) + result
  result_str = [result[i//2] if i % 2 == 0 else ' ' for i in range(2 * m - 1)]
  print(''.join(result_str))
```

1과 2에서 풀었던 방식으로 백트래킹을 활용하여 재귀로 풀까 하였다. 하지만 가만히 생각해보니 N진수로 이루어진 수가 1씩 더해지는 형식이다. N진수를 정의하는 함수만 구현한다면 굳이 append pop하는 것보다 시간 복잡도가 훨씬 줄어들 것만 같아서 시도해 본 결과이다.

## 15652 문제

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지?자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
    - 길이가 K인 수열 A가 A?≤ A?≤ ... ≤ A?≤ A를 만족하면, 비내림차순이라고 한다.
        
        1
        
        2
        
        K-1
        
        K
        

## 입력

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

## 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제 입력 1

```
3 1
```

## 예제 출력 1

```
1
2
3
```

## 답안 코드

```python
n,m = list(map(int,input().split()))
 
s = []
temp =0

def dfs():
    global temp
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i >= temp:
            s.append(i)
            temp = s[-1]
            dfs()
            s.pop()
            if len(s) == 0:
                pass
            else :
                temp = s[-1]

dfs()
```

기존에 풀었던 백트래킹 알고리즘에서 s리스트에 넣는 조건만 수정하면 간단히 풀리는 문제이다.


## 15654 문제

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열

## 입력

첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

## 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제 입력 1

```
3 1
4 5 2
```

## 예제 출력 1

```
2
4
5
```

## 답안 코드

```python
N, M = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
stack = []

def back(s: list):
    
    if len(stack) == M:
        print(" ".join(map(str, stack)))
        return
        
    for i in arr:
        if i not in stack:
            stack.append(i)
            back(arr)
            stack.pop()
            
back(arr)
```

백트래킹 알고리즘을 활용하여 재귀적 코드를 작성하면 금방 해결되는 문제이다.

M개의 수만큼 stack에 찰 경우 함수를 리턴하고 pop하여 새로운 값을 할당한다.

## 15655 문제

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

## 입력

첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

## 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제 입력 1

```
3 1
4 5 2
```

## 예제 출력 1

```
2
4
5
```

## 답안 코드

```python
N, M = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
stack = []
temp = []

def back(s: list):
    
    if len(stack) == M:
        print(" ".join(map(str, stack)))
        temp.append(set(stack))
        return
        
    for i in arr:
        if i not in stack:
            stack.append(i)
            if set(stack) not in temp:
                back(arr)
                stack.pop()
            else: stack.pop()
            
back(arr)
```

### solution

전 문제와 마찬가지로 백트래킹을 이용하여 풀었다. 중복을 피해야 하니 집합으로 만들어서 값을 temp로 저장해 둔다. 그리고 값을 넣을 때 temp에 있는 값과 비교하여 없을 때(중복되지 않을 때) 재귀 함수를 실행한다.

## 15656 문제

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.

## 입력

첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

## 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제 입력 1

```
3 1
4 5 2
```

## 예제 출력 1

```
2
4
5
```

## 답안 코드

```python
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
```

### solution

이 문제는 전의 문제와 동일하지만, 이번엔 모든 중복이 허용이 된다. 따라서 어떠한 조건 필요 없이 바로 재귀 알고리즘으로 리스트 값을 채워나가면 된다.

## 15657 문제

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
    - 길이가 K인 수열 A가 A?≤ A?≤ ... ≤ A?≤ A를 만족하면, 비내림차순이라고 한다.
        
        1
        
        2
        
        K-1
        
        K
        

## 입력

첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

## 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제 입력 1

```
3 1
4 5 2
```

## 예제 출력 1

```
2
4
5
```

## 답안 코드

```python
N, M = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
stack = []

def back(s: list):
    
    if len(stack) == M:
        print(" ".join(map(str, stack)))
        return
        
    for i in arr:
        if not stack or i >= stack[-1]:
            stack.append(i)
            back(arr)
            stack.pop()
            
back(arr)
```

### solution

이번 문제는 순열이 오름차순 이어야 한다. 즉 새로 추가되는 값은 마지막 요소의 값보다 커야 하고, 이 조건만 추가하면 된다. `stack[-1]`로 마지막 요소를 접근하고 `stack`이 비어있을 때는 오류가 발생하니 `not stack`을 통해 비어있으면 그냥 값을 추가한다.

## 18290 문제

크기가 N×M인 격자판의 각 칸에 정수가 하나씩 들어있다. 이 격자판에서 칸 K개를 선택할?것이고, 선택한 칸에 들어있는?수를 모두 더한 값의 최댓값을 구하려고 한다. 단, 선택한 두 칸이 인접하면 안된다. r행 c열에 있는 칸을 (r, c)라고 했을 때, (r-1, c), (r+1, c), (r, c-1), (r, c+1)에 있는 칸이 인접한 칸이다.

## 입력

첫째 줄에 N, M, K가 주어진다. 둘째 줄부터 N개의 줄에 격자판에 들어있는 수가 주어진다.

## 출력

선택한 칸에 들어있는 수를 모두 더한 값의 최댓값을 출력한다.

## 제한

- 1 ≤ N, M ≤ 10
- 1 ≤ K ≤ min(4, N×M)
- 격자판에 들어있는 수는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
- 항상 K개의 칸을 선택할 수 있는 경우만 입력으로 주어진다.

## 예제 입력 1

```
1 1 1
1
```

## 예제 출력 1

```
1
```

### 내 코드

```python
N, M , K = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

def adhere(i,j):
    temp = [(i,j), (i-1,j), (i+1,j), (i,j+1), (i,j-1)]
    return temp

stack = []
ans = []
result = 0

def back(arr:list,a,b):
    global result
    if len(ans) == K:
        result = max(sum(ans),result)
        return
    
    for i in range(a,N):
        for j in range(b,M):
            if (i,j) not in stack:
                ans.append(arr[i][j])
                for s in adhere(i,j):
                    stack.append(s)
                back(arr,a,b)
                for s in adhere(i,j):
                    stack.remove(s)
                ans.pop()

back(arr,0,0)           
print(result)
```

위의 코드와 같이 풀었더니 시간 초과가 났다. stack에서 tuple값을 찾는 데 시간이 많이 들었나 하여 일일이 검사하는 식으로 바꿔봤는데 여전히 시간 초과가 뜬다. 그래서 다른 사람의 풀이를 찾아본 결과이다

```python
def dfs(x, y, d, s):
    global ans
    if d == K:
        ans = max(ans, s)
        return
    else:
        for i in range(x, N):
            for j in range(y if i == x else 0, M):
                if [i, j] not in q:
                    if ([i + 1, j] not in q) and ([i - 1, j] not in q) and ([i, j + 1] not in q) and ([i, j - 1] not in q):
                        q.append([i, j])
                        dfs(i, j, d + 1, s + a[i][j])
                        q.pop()

N, M, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
q = []
ans = -1e10
dfs(0, 0, 0, 0)
print(ans)
```

이 코드는 [https://velog.io/@y7y1h13/알고리즘백준-18290-NM과-K1python](https://velog.io/@y7y1h13/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-18290-NM%EA%B3%BC-K1python) 여기서 따온 것이다. 제출은 되지만 실행 결과 엄청난 시간이 소요되는 것을 알 수 있었다. 따라서 이러한 방법 외 다른 방법을 고안해본다.

```python
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(depth, start, v):
    global ans
    if depth == K:
        ans = max(ans, v)
        return
    if v + 10000 * (K-depth) < ans:
        return
    
    for i in range(start, N*M):
        r = i % N
        c = i // N
        if visit[r][c]:
            continue
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if visit[nr][nc] == 1:
                break
        else:
            visit[r][c] = 1
            dfs(depth+1, i+1, v+lst[r][c])
            visit[r][c] = 0

N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]
ans = -1_000_000_000

dfs(0, 0, 0)
print(ans)
```

현재 백준 문제 풀이 1등의 공개 소스 코드이다. 이 분의 경우 dfs를 이용하여 visit사용하였다.