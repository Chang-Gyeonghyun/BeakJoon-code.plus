## 1759 문제

바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 702호에 새로운 보안 시스템을 설치하기로 하였다. 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C?≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

## 출력

각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

## 예제 입력 1

```
4 6
a t c i s w
```

## 예제 출력 1

```
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
```

### 내 답안 코드

```python
L, C = map(int,input().split())
arr = list(input().split())
arr.sort()

stack = []
mom = ['a', 'e', 'i', 'o', 'u'] #모음 리스트

def dfs():
    if len(stack) == L:
        momv = False
        sonv = 0
        
        for i in stack: #모음 자음 개수 세기
            if i in mom:
                momv = True
            else:
                sonv += 1

        if momv and sonv>=2:
            print("".join(stack))
        return
            
    
    for i in arr:
        if not stack or i > stack[-1]:
            stack.append(i)
            dfs()
            stack.pop()
            
            
dfs()
```

### solution

전에 풀었던 M과 N문제와 매우 유사하다. 다만 차이점은 모음 1개와 자음 2개 이상을 무조건 포함 시켜야 하는 것이다. 알파벳이 중복되지 않고, 숫자 또한 유한하므로 그냥 기존 M과 N문제에서 조건이 성립될 때에, 모음 자음 개수만 더 추가적으로 검사하도록 하였다.

## 14501 문제

상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.

오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.

백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.

각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

N = 7인 경우에 다음과 같은 상담 일정표를 보자.

|  | 1일 | 2일 | 3일 | 4일 | 5일 | 6일 | 7일 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ti | 3 | 5 | 1 | 1 | 2 | 4 | 2 |
| Pi | 10 | 20 | 10 | 20 | 15 | 40 | 200 |

1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.

상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다. 2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.

또한, N+1일째에는 회사에?없기 때문에, 6, 7일에 있는 상담을 할 수 없다.

퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.

상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti?≤ 5, 1 ≤ Pi?≤?1,000)

## 출력

첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.

## 예제 입력 1

```
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
```

## 예제 출력 1

```
45
```

### 내 답안 코드

```python
import sys

N = int(input())
arr =[]
for i in range(N):
    T, P = map(int,input().split())
    arr.append((T,P))

sum = 0
result = -sys.maxsize

def dfs(start, sum):
    global result
    if start >= len(arr):
        result = max(result, sum)
        return
    
    for i in range(start, N):
        t, p = arr[i]
        if i+t <= len(arr):
            dfs(i+t, sum + p)
        else:
            dfs(i+1, sum)
            
            
            
dfs(0,0)
print(result)
```

### solution

재귀 함수를 이용하여 문제를 접근하였다. 각 요일과 금액을 묶어서 한 리스트에 집어 넣는다. 그리고   따로 스택 리스트를 만들어서 값을 집어 넣고 stack 내부의 요소들을 전부 더할까 했는데, 그렇게 되면 in을 사용하게 되고 시간복잡도가 늘어날 것 같아서 재귀 함수 인자에 더한 값으로 바로바로 업데이트 되도록 하였다. 또한 for문을 돌 때 start를 표시하여 해당 날짜만큼 건너뛰도록 하였다.

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

### 내 답안 코드

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
        link = [ele for ele in range(N) if ele not in start] #나머지 인원들은 link팀에 배치
        differ = find(start) - find(link)
        result = min(result,abs(differ))
        return
        
    
    
    for i in range(head, N): #팀원 뽑기
        start.append(i)
        dfs(i+1) #중복됨으로 인덱스를 굳이 처음부터 셀 필요 없다.
        start.pop()
        
        
def find(arr:list):  #s리스트 안에서 팀원간 능력치 찾고 더하기
    sum = 0
    for i in arr:
        for j in arr:
            sum += s[i][j]
    return sum
        
dfs(0)
print(result)
```

### solution

역시나 다를까 재귀 문제이다. N개의 인덱스에서 N/2 개수 만큼의 수를 start팀으로 뽑는다. 그리고 다 뽑았을 시에 나머지 인원을 link팀에 배치한다. find 함수를 통해 각 팀원들의 조합에 있어 능력치를 조회하고 더한다. 각 팀에 능력치 합을 빼고 그 차이가 가장 작은 값으로 업데이트 한다.

## 문제

오늘은 스타트링크에 다니는 사람들이 모여서?축구를 해보려고 한다. 축구는 평일 오후에 하고?의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이다. 이제 스타트 팀과 링크 팀으로 사람들을 나눠야 한다. 두 팀의 인원수는 같지 않아도 되지만, 한 명 이상이어야 한다.

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

첫째 줄에 N(4 ≤ N ≤ 20)이 주어진다. 둘째?줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij?이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

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

### 내 답안 코드

```python
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
```

### solution

바로 전 문제와 동일하다. 하지만 팀원의 수가 꼭 반반일 필요가 없고, 한 명 이상이면 충분하다는 조건이 붙어있다. 따라서 팀원이 1명일 때부터 N/2명일 때까지 함수 매개변수에 추가로 명시해 놓는다.

## 문제

두 종류의 부등호 기호 ‘<’와 ‘>’가 k개 나열된 순서열 A가 있다. 우리는 이 부등호 기호 앞뒤에 서로 다른 한 자릿수 숫자를 넣어서 모든 부등호 관계를 만족시키려고 한다. 예를 들어, 제시된 부등호 순서열 A가 다음과 같다고 하자.

A ⇒ < < < > < < > < >

부등호 기호 앞뒤에 넣을 수 있는 숫자는 0부터 9까지의 정수이며 선택된 숫자는 모두 달라야 한다. 아래는 부등호 순서열 A를 만족시키는 한 예이다.

**3 < 4 < 5 < 6 > 1 < 2 < 8 > 7 < 9 > 0**

이 상황에서 부등호 기호를 제거한 뒤, 숫자를 모두 붙이면 하나의 수를 만들 수 있는데 이 수를 주어진 부등호 관계를 만족시키는 정수라고 한다. 그런데 주어진 부등호 관계를 만족하는 정수는 하나 이상 존재한다. 예를 들어 3456128790 뿐만 아니라 5689023174도 아래와 같이 부등호 관계 A를 만족시킨다.

**5 < 6 < 8 < 9 > 0 < 2 < 3 > 1 < 7 > 4**

여러분은 제시된 k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서 최댓값과 최솟값을 찾아야 한다. 앞서 설명한 대로 각 부등호의 앞뒤에 들어가는 숫자는 { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }중에서 선택해야 하며?**선택된 숫자는 모두 달라야 한다**.

## 입력

첫 줄에 부등호 문자의 개수를 나타내는 정수 k가 주어진다. 그 다음 줄에는 k개의 부등호 기호가 하나의 공백을 두고 한 줄에 모두 제시된다. k의 범위는 2 ≤ k ≤ 9 이다.

## 출력

여러분은 제시된 부등호 관계를 만족하는 k+1 자리의 최대, 최소 정수를 첫째 줄과 둘째 줄에 각각 출력해야 한다. 단 아래 예(1)과 같이 첫 자리가 0인 경우도 정수에 포함되어야 한다. 모든 입력에 답은 항상 존재하며 출력 정수는 하나의 문자열이 되도록 해야 한다.

## 예제 입력 1

```
2
< >
```

## 예제 출력 1

```
897
021
```

### 내 답안 코드

```python
import sys

k = int(input())
arr = list(input().split())

stack = []
maximum = -sys.maxsize
minimum = sys.maxsize

def dfs(idx):
    global maximum, minimum, stack
    
    if len(stack) == k + 1:
#개수가 다 찼을 경우 결과값을 업데이트 한다.
        temp = int("".join(map(str, stack)))
        maximum = max(maximum, temp)
        minimum = min(minimum, temp)
        return

    for i in range(10):
        if not stack:
            stack.append(i)
            dfs(idx + 1)
            stack.pop()
        elif arr[idx-1] == '<' and i > stack[-1] and i not in stack:
#현재 인덱스의 전 값이 비교할 부등호임. 그리고 이전 값과 비교하고 그 값이 중복되지 않도록 해야한다.
            stack.append(i)
            dfs(idx + 1)
            stack.pop()
        elif arr[idx-1] == '>' and i < stack[-1] and i not in stack:
            stack.append(i)
            dfs(idx + 1)
            stack.pop()

dfs(0)
print(str(maximum).zfill(len(arr)+1))
print(str(minimum).zfill(len(arr)+1))
```

### solution

숫자를 한 개씩 스택에 집어 넣는다. 그리고 idx를 한 개씩 추가하여 다음 재귀 함수를 돌 때, arr리스트의 다음 부등호를 가르키게 한다. 그 부등호를 조건식에 넣어 값을 stack에 append할 지 여부를 판단한다. 값이 다 채워질 경우 maximum과 minimum을 계속 업데이트 한다.

## 문제

Given a sequence of integers, a1, a2, …, an, we define its sign matrix S such that, for 1 ≤ i ≤ j ≤ n, Sij="+" if ai?+ … + aj?> 0; Sij="?" if ai?+ … + aj?< 0; and Sij="0" otherwise.

For example, if (a1, a2, a3, a4)=( ?1, 5, ?4, 2), then its sign matrix S is a 4×4 matrix:

|  | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 1 | - | + | 0 | + |
| 2 |  | + | + | + |
| 3 |  |  | - | - |
| 4 |  |  |  | + |

We say that the sequence (?1, 5, ?4, 2) generates the sign matrix. A sign matrix is valid if it can be generated by a sequence of integers.

Given a sequence of integers, it is easy to compute its sign matrix. This problem is about the opposite direction: Given a valid sign matrix, find a sequence of integers that generates the sign matrix. Note that two or more different sequences of integers can generate the same sign matrix. For example, the sequence (?2, 5, ?3, 1) generates the same sign matrix as the sequence (?1,5, ?4,2).

Write a program that, given a valid sign matrix, can find a sequence of integers that generates the sign matrix. You may assume that every integer in a sequence is between ?10 and 10, both inclusive.

## 입력

The first line contains an integer n(1 ≤ n ≤ 10), where n is the length of a sequence of integers. The second line contains a string of n(n+1)/2 characters such that the first n characters correspond to the first row of the sign matrix, the next n?1 characters ?to the second row, ..., and the last character to the n-th row.

## 출력

Output exactly one line containing a sequence of n integers which generates the sign matrix. If more than one sequence generates the sign matrix, you may output any one of them. Every integer in the sequence must be between ?10 and 10, both inclusive.

## 예제 입력 1

```
4
-+0++++--+
```

## 예제 출력 1

```
-2 5 -3 1
```

### Answer code

```jsx
n = int(input())
arr = [[0] * n for _ in range(n)]
b = list(input())
v, k = [], 0

def possible(idx):
    s = 0
    for i in range(idx, -1, -1):
        s += v[i]
        if arr[i][idx] == '+' and s <= 0:
            return False
        if arr[i][idx] == '0' and s != 0:
            return False
        if arr[i][idx] == '-' and s >= 0:
            return False
    return True

def solve(idx):
    if idx == n:
        print(' '.join(map(str, v)))
        exit(0)
    for i in range(-10, 11):
        v.append(i)
        if possible(idx):
            solve(idx + 1)
        v.pop()

for i in range(n):
    for j in range(i, n):
        arr[i][j] = b[k]
        k += 1
solve(0)
```

### solution

나는 주어진 배열을 격자 판으로 옮기고, 그 다음 (0,0)부터 (0,k-1)까지의 값을 비교하여 알맞게 넣은 다음에 그 값을 임시로 저장했다. 그렇게 행을 한 칸씩 늘려가며 임시 저장된 값들이 유효한 지 비교하는 것이었다. 하지만 이렇게 하니 메모리 초과가 떴다. 너무 많은 값들을 임시 저장한 탓인듯 싶다. 다른 방법으로 접근해야겠다고 생각하고 다른 사람의 코드를 살펴보았다.
위 코드는 열로 접근하였다. 그 전까지의 열값을 스택에 저장해두고 열로 인한 비교를 하니 바로바로 처리가 되는 것을 볼 수 있었다.