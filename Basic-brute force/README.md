## 2309 문제

왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

## 입력

아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

## 출력

일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.

## 예제 입력 1

```
20
7
23
19
10
15
25
8
13
```

## 예제 출력 1

```
7
8
10
13
19
20
23
```

## 답안 코드

```python
from itertools import combinations

little = [0] * 9
for i in range(9):
    little[i] = int(input())
comb = list(combinations(little,7))

sum = 0
value = [0]*7
for std in comb:
    for i in range(7):
        sum += std[i]
    if sum == 100:
        value = list(std)
        break
    else:
        sum = 0
value.sort()
for i in value:
    print(i)
```

## 3085 문제

상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다.?이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

## 출력

첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.

## 예제 입력 1

```
3
CCP
CCP
PPC
```

## 예제 출력 1

```
3
```

## 답안코드

```python
def count_adjacent_cells(matrix):
    counts = {'C': 0, 'P': 0, 'Z': 0, 'Y': 0}
    max_counts = {'C': 0, 'P': 0, 'Z': 0, 'Y': 0}
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current_cell = matrix[i][j]
            
            if j > 0 and current_cell == matrix[i][j - 1]:
                counts[current_cell] += 1
            else:
                max_counts[current_cell] = max(max_counts[current_cell], counts[current_cell])
                counts[current_cell] = 1
    
    return max(max_counts.values())

def swap_and_count(matrix, i, j, new_i, new_j):
    matrix[i][j], matrix[new_i][new_j] = matrix[new_i][new_j], matrix[i][j]
    return count_adjacent_cells(matrix)

N = int(input())
Bombo = [list(input()) for _ in range(N)]
max_count = count_adjacent_cells(Bombo)

for i in range(N):
    for j in range(N):
        if j + 1 < N and Bombo[i][j] != Bombo[i][j + 1]:
            new_count = swap_and_count(Bombo, i, j, i, j + 1)
            max_count = max(max_count, new_count)
            swap_and_count(Bombo, i, j, i, j + 1)  # 원래대로 되돌림

        if i + 1 < N and Bombo[i][j] != Bombo[i + 1][j]:
            new_count = swap_and_count(Bombo, i, j, i + 1, j)
            max_count = max(max_count, new_count)
            swap_and_count(Bombo, i, j, i + 1, j)  # 원래대로 되돌림

print(max_count)
```

## 1476 문제

준규가 사는 나라는 우리가 사용하는 연도와 다른 방식을 이용한다. 준규가 사는?나라에서는 수 3개를 이용해서 연도를 나타낸다. 각각의 수는 지구, 태양, 그리고 달을 나타낸다.

지구를 나타내는 수를 E, 태양을 나타내는 수를 S, 달을 나타내는 수를 M이라고 했을 때, 이 세 수는 서로 다른 범위를 가진다. (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)

우리가 알고있는 1년은 준규가 살고있는 나라에서는 1 1 1로 나타낼 수 있다. 1년이 지날 때마다, 세 수는 모두 1씩 증가한다. 만약, 어떤 수가 범위를 넘어가는 경우에는 1이 된다.

예를 들어, 15년은 15 15 15로 나타낼 수 있다. 하지만, 1년이 지나서 16년이 되면 16 16 16이 아니라 1 16 16이 된다. 이유는 1 ≤ E ≤ 15 라서 범위를 넘어가기 때문이다.

E, S, M이 주어졌고, 1년이 준규가 사는 나라에서 1 1 1일때, 준규가 사는 나라에서 E S M이 우리가 알고 있는 연도로 몇 년인지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 세 수 E, S, M이 주어진다. 문제에 나와있는 범위를 지키는 입력만 주어진다.

## 출력

첫째 줄에 E S M으로 표시되는 가장 빠른 연도를 출력한다. 1 1 1은 항상 1이기 때문에, 정답이 음수가 나오는 경우는 없다.

## 예제 입력 1

```
1 16 16
```

## 예제 출력 1

```
16
```

## 답안코드

```python
E, S, M = map(int,input().split())
e, s, m = 0,0,0
count = 0
while True:
    e += 1
    s += 1
    m += 1
    count += 1
    if(e > 15 ): e = 1
    if(s > 28): s = 1
    if(m > 19): m = 1
    
    if(E == e and S == s and M == m):
        break
    
print(count)
```

## 1107 문제

수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는?바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이?0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.

수빈이가 지금 보고 있는 채널은 100번이다.

## 입력

첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.??둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번?주어지는 경우는 없다.

## 출력

첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를?출력한다.

## 예제 입력 1

```
5457
3
6 7 8
```

## 예제 출력 1

```
6
```

## 답안 코드

```python
def find(N):
    for i in fault_num:
        if str(N).find(i) >= 0:
            return True
    return False

cur_ch = 100
prefer_ch = int(input())
N = int(input())
if N != 0:
    fault_num = list(input().split())
else:
    fault_num = []

#나중에 자릿수를 센다. 그주변에서 위 아래로 다 가보고 가장 최소
count, finalnum = 0,0

UN = prefer_ch
DN = prefer_ch
temp = abs(cur_ch - prefer_ch)
valid = True

if prefer_ch == 100:
    print("0")

elif N == 10:
    print(temp)
    
else:
    while True:
        
        if find(DN) and valid:
            DN -= 1
            if(DN < 0):
                valid = False
        else:
            if valid:
                count = prefer_ch - DN
                finalnum = DN
                break
        if find(UN):
            UN += 1
        else:
            count = UN - prefer_ch
            finalnum = UN
            break
    #print(finalnum ,len(str(finalnum)) , count)
    print(min(len(str(finalnum)) + count, temp))
```

1. 선호하는 값을 가운데로 두고 1씩 더하거나 뺀다. 두 값들 중 고장난 키에 구애 받지 않는 채널이 나타날 경우 해당 채널의 string길이와 채널 이동한 count 수를 더하여 문제를 풀었다.
    
    이 때 선호 채널과 현재 100채널의 차이가 앞서 구한 수보다 작을 경우도 판단한다.
    

1. 고장난 키가 존재하지 않거나 선호 채널이 그대로 100일 경우, 그리고 모든 키가 고장나서 +/-키로만 채널을 움직여야 하는 경우의 수를 모두 생각해준다.

## 14500 문제

폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

- 정사각형은 서로 겹치면 안 된다.
- 도형은 모두 연결되어 있어야 한다.
- 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.

정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14500/1.png

아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.

테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

## 입력

첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4?≤ N, M ≤ 500)

둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

## 출력

첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.

## 예제 입력 1

```
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
```

## 예제 출력 1

```
19
```

## 답안 코드

```python
def dfs(r, c, total,size):
    global ans
    if size == 4:
        ans = max(ans, total)
        return

    for mr, mc in moves:
        new_r, new_c = r+mr, c+mc

        if 0<= new_r < N and 0<= new_c < M and not visited[new_r][new_c]:
            
            if size == 2:
                visited[new_r][new_c] = True
                dfs(r, c, total+A[new_r][new_c],size+1)
                visited[new_r][new_c] = False

            visited[new_r][new_c] = True
            dfs(new_r, new_c, total+A[new_r][new_c],size+1)
            visited[new_r][new_c] = False

moves=[[-1,0],[0,1],[1,0],[0,-1]]

N, M = map(int, input().split())
visited=[[False for _ in range(M)] for _ in range(N)]
A=[]
for _ in range(N):
    A.append(list(map(int, input().split())))
ans=0
for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(r,c,A[r][c],1)
        visited[r][c] = False
print(ans)
```

위dfs탐색으로 4개를 접근했을 때, ㅗ형 블록을 제외한 나머지 블록은 전부 접근할 수 있다. 따라서 dfs탐색으로 접근을 하되, 세 번째 칸까지 찾았을 때엔 마지막 찾는 칸은 다시 이전 칸으로 돌아와서 찾는 경우도 명시를 해야 한다. 

위의 코드는 각각 모든 인덱스에 대해 전부 찾아서 더하고 그 중 큰 값을 고르는 형식이다. 나는 이 방법이 싫어서(시간이 더 걸리므로) 매 인덱스마다 최적화된 값만 찾으려고 노력했지만 포기하고 원래 방법으로 제출했다.

## 6064 문제

최근에 ICPC 탐사대는 남아메리카의 잉카 제국이 놀라운 문명을 지닌 카잉 제국을 토대로 하여 세워졌다는 사실을 발견했다. 카잉 제국의 백성들은 특이한 달력을 사용한 것으로 알려져 있다. 그들은 M과 N보다 작거나 같은 두 개의 자연수 x, y를 가지고 각 년도를 <x:y>와 같은 형식으로 표현하였다. 그들은 이 세상의 시초에 해당하는 첫 번째 해를 <1:1>로 표현하고, 두 번째 해를 <2:2>로 표현하였다. <x:y>의 다음 해를 표현한 것을 <x':y'>이라고 하자. 만일 x < M 이면 x' = x + 1이고, 그렇지 않으면 x' = 1이다. 같은 방식으로 만일 y < N이면 y' = y + 1이고, 그렇지 않으면 y' = 1이다. <M:N>은 그들 달력의 마지막 해로서, 이 해에 세상의 종말이 도래한다는 예언이 전해 온다.

예를 들어, M = 10 이고 N = 12라고 하자. 첫 번째 해는 <1:1>로 표현되고, 11번째 해는 <1:11>로 표현된다. <3:1>은 13번째 해를 나타내고, <10:12>는 마지막인 60번째 해를 나타낸다.

네 개의 정수 M, N, x와 y가 주어질 때, <M:N>이 카잉 달력의 마지막 해라고 하면 <x:y>는 몇 번째 해를 나타내는지 구하는 프로그램을 작성하라.

## 입력

입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 구성된다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터는 한 줄로 구성된다. 각 줄에는 네 개의 정수 M, N, x와 y가 주어진다. (1 ≤ M, N ≤ 40,000, 1 ≤ x ≤ M, 1 ≤ y ≤ N) 여기서 <M:N>은 카잉 달력의 마지막 해를 나타낸다.

## 출력

출력은 표준 출력을 사용한다. 각 테스트 데이터에 대해, 정수 k를 한 줄에 출력한다. 여기서 k는 <x:y>가 k번째 해를 나타내는 것을 의미한다. 만일 <x:y>에 의해 표현되는 해가 없다면, 즉, <x:y>가 유효하지 않은 표현이면, -1을 출력한다.

## 예제 입력 1

```
3
10 12 3 9
10 12 7 2
13 11 5 6
```

## 예제 출력 1

```
33
-1
83
```

## 답안 코드

```python
T = int(input())

for i in range(T):
    M,N,x,y = map(int,input().split())
    valid = 0
    for j in range(N):
        if (j*M+x-y)%N == 0:
            print(j*M+x)
            valid = 1
            break
    if valid == 0:
        print("-1")
```

위의 코드에서 j*M+x식을 계산할 경우 전체 count의 수가 나온다. 또한 N*(미지수) +y식을 계산할 경우에도 전체 count식이 나와서 두 식의 값이 일치한다. 이 점을 이용하여 전자의 식에서 y를 빼준다. 미지수를 구할 필요는 없기에 앞선 결과 값이 N으로 나누어 떨어지는 지만 확인하면 된다.

## 1748 문제

1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.

> 1234567891011121314151617181920212223...
> 

이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N(1 ≤ N ≤ 100,000,000)이 주어진다.

## 출력

첫째 줄에 새로운 수의 자릿수를 출력한다.

## 예제 입력 1

```
5
```

## 예제 출력 1

```
5
```

## 답안 코드

```python
def sum(N,M):
    
    if len(str(N)) == M:
        if M == 1:
            return N
        return M * (N - int("9"*(M-1))) + sum(N,M-1)
    
    elif M == 1:
        return 9
    
    else:
        return (M) * (int("9"*(M)) - int("9"*(M-1))) + sum(N,M-1)
    
    
N = int(input())
M=len(str(N))
ans = sum(N,M)
print(ans)
```

처음엔 입력 받은 숫자를 범위로 반복문으로 하여 도는 숫자마다 문자열로 변환하여 더해주었다.  너무 쉽게 풀리길래 시간 초과가 날까 싶었는데 역시 시간 초과가 났다. 입력 받은 숫자만큼 반복문을 돌아서 그런 것이다. 따라서 위와 같이 재귀 함수를 통해 똑같은 자리 수를 가지는 숫자만큼 더해주었다.

## 9095 문제

정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

- 1+1+1+1
- 1+1+2
- 1+2+1
- 2+1+1
- 2+2
- 1+3
- 3+1

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

## 출력

각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

## 예제 입력 1

```
3
4
7
10
```

## 예제 출력 1

```
7
44
274
```

### 답안코드

```python
num = int(input())

sum = 0

def par(i):
    if i == 1:
        return 1
    if i == 2:
        return 2
    if i == 3:
        return 4
    return par(i-1) + par(i-2) + par(i-3)

for i in range(num):
    n = int(input())
    sum = par(n)
    print(sum)
```