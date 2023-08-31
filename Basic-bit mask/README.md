## 11723 문제

비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

- `add x`: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
- `remove x`: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
- `check x`: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
- `toggle x`: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
- `all`: S를 {1, 2, ..., 20} 으로 바꾼다.
- `empty`: S를 공집합으로 바꾼다.

## 입력

첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

## 출력

`check`?연산이 주어질때마다, 결과를 출력한다.

## 예제 입력 1

```
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
```

## 예제 출력 1

```
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
```

### My code

```python
import sys
M = int(input())
S = set()

for i in range(M):
    oper = sys.stdin.readline().strip().split()
    if len(oper) != 1:
        value = int(oper[1])
    oper = oper[0]
    if oper == "add":
        S.add(value)
    elif oper == "remove":
        S.discard(value)
    elif oper == "check":
        if value in S:
            print(1)
        else: print(0)
    elif oper == "toggle":
        if value in S:
            S.discard(value)
        else: S.add(value)
    elif oper == "all":
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20} 

    elif oper == "empty":
        S.clear()
```

### solution

각 문자열 케이스를 나눠서 집합에 대한 set 내장 함수를 사용하였다.

## 1182 문제

N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

## 출력

첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

## 예제 입력 1

```
5 0
-7 -3 -2 5 8
```

## 예제 출력 1

```
1
```

### Solution

```python
n, s = map(int,input().split())
n_list = list(map(int,input().split()))

cnt = 0

def dfs(num,sum):
	global cnt
	if num >= n:
		return
	sum += n_list[num]
	if sum == s:
		cnt += 1

	dfs(num+1,sum)
	dfs(num+1,sum-n_list[num])

dfs(0,0)
print(cnt)
```

전에 풀었던 백트래킹 알고리즘이랑 조금 다르다. 전에 있던 거는 순열로 순서에 따라서도 다른 경우로 인식 했지만 이번 문제에서는 순서가 상관이 없기 때문에, 해당 인덱스를 포함시키느냐 안시키느냐 두 가지로 구분하여 재귀적 함수를 쓰면 된다.

## 14889 문제

오늘은 스타트링크에 다니는 사람들이 모여서?축구를 해보려고 한다. 축구는 평일 오후에 하고?의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게?번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

N=4이고, S가 아래와 같은 경우를 살펴보자.

| i\j | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 1 |  | 1 | 2 | 3 |
| 2 | 4 |  | 5 | 6 |
| 3 | 7 | 1 |  | 2 |
| 4 | 3 | 4 | 5 |  |

예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

- 스타트 팀: S?+ S?= 1 + 4 = 5
    
    12
    
    21
    
- 링크 팀: S?+ S?= 2 + 5 = 7
    
    34
    
    43
    

1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

- 스타트 팀: S?+ S?= 2 + 7 = 9
    
    13
    
    31
    
- 링크 팀: S?+ S?= 6 + 4 = 10
    
    24
    
    42
    

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이?스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

## 입력

첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째?줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij?이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

## 출력

첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

## 예제 입력 1

```
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
```

## 예제 출력 1

```
0
```

### My code

```python
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
```

## 14391 문제

영선이는 숫자가 쓰여 있는 직사각형 종이를 가지고 있다. 종이는 1×1 크기의 정사각형 칸으로 나누어져 있고, 숫자는 각 칸에 하나씩 쓰여 있다. 행은 위에서부터 아래까지 번호가 매겨져 있고, 열은 왼쪽부터 오른쪽까지 번호가 매겨져 있다.

영선이는 직사각형을 겹치지 않는 조각으로 자르려고 한다. 각 조각은 크기가 세로나 가로 크기가 1인 직사각형 모양이다. 길이가 N인 조각은 N자리 수로 나타낼 수 있다. 가로 조각은 왼쪽부터 오른쪽까지 수를 이어 붙인 것이고, 세로 조각은 위에서부터 아래까지 수를 이어붙인 것이다.

아래 그림은 4×4 크기의 종이를 자른 한 가지 방법이다.

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14391/1.png

각 조각의 합은 493 + 7160 + 23 + 58 + 9 + 45 + 91 = 7879 이다.

종이를 적절히 잘라서 조각의 합을 최대로 하는 프로그램을 작성하시오.

## 입력

첫째 줄에 종이 조각의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤?4)

둘째 줄부터 종이 조각이 주어진다. 각 칸에 쓰여 있는 숫자는 0부터 9까지 중 하나이다.

## 출력

영선이가 얻을 수 있는 점수의 최댓값을 출력한다.

## 예제 입력 1

```
2 3
123
312
```

## 예제 출력 1

```
435
```

### Answer Code

```python
def bitmask():
    global maxAns
    # 비트마스크로 2^(N*M)의 경우의 수를 따져본다
    for i in range(1 << n * m):
        total = 0
        # 가로 합 계산
        for row in range(n):
            rowsum = 0
            for col in range(m):
                # idx 는 이차원 배열을 일렬로 늘렸을때의 인덱스가 어디인지 의미
                idx = row * m + col
                # 가로일때
                if i & (1 << idx) != 0:
                    rowsum = rowsum * 10 + arr[row][col]
                # 세로일때 앞에서 나온 수를 total에 더하고 rowsum 초기화
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum

        # 세로 합 계산
        for col in range(m):
            colsum = 0
            for row in range(n):
                # idx 는 이차원 배열을 일렬로 늘렸을때의 인덱스가 어디인지 의미
                idx = row * m + col
                # 세로일때
                if i & (1 << idx) == 0:
                    colsum = colsum * 10 + arr[row][col]
                # 가로일때 앞에서 나온 수를 total에 더하고 colsum 초기화
                else:
                    total += colsum
                    colsum = 0
            total += colsum
        maxAns = max(maxAns, total)

n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

maxAns = 0
bitmask()
print(maxAns)

```

이런저런 다양한 로직을 시도해 보았지만 풀이에 실패하였다. 그렇게 구글링을 했더니 비트 마스크라는 것을 이용하면 된다고 나와있다. 그렇다면 비트 마스크는 무엇인가?

### 비트 마스크

비트마스크는 비트의 형태를 활용한다.

알고리즘보다는 테크닉 중 하나로써,?**정수의 이진수 표현을 활용한 기법이다.**

여기까지 비트를 통해 알 수 있는 2가지 정보는 다음과 같다.

- 이진수는 0, 1 만을 가지고, true/fasle 상태를 가진다.
- 이진수는 십진수로 표현 가능하다.

요소를 뽑아서 그 요소가 가질 수 있는 경우의 수 2가지가 있다면 비트로 나타낼 수 있다.

요소의 인덱스(i)가 비트의 i 번째 숫자가 될 것이고 그 것이 나타내는 것이 해당 경우의 수 중 하나가 될 것이다.

따라서 0과 1 기준으로 가로 세로일 경우로 나누어서 합산 하면 된다.

참고

https://vixxcode.tistory.com/23