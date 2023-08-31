## 10430 문제

(A+B)%C는 ((A%C) + (B%C))%C?와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 A, B, C가 순서대로 주어진다. (2?≤ A, B, C ≤ 10000)

## 출력

첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다

## 예제 입력 1

```
5 8 4
```

## 예제 출력 1

```
1
1
0
0
```

## 답안 코드

```python
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

print((A+B)%C)
print((A+B)%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
```

## 4375 문제

2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다.

## 출력

각 자릿수가 모두 1로만 이루어진 n의 배수 중 가장 작은 수의 자리수를 출력한다.

## 예제 입력 1

```
3
7
9901
```

## 예제 출력 1

```
3
6
12
```

## 답안 코드

```python
while True:
    try:
         i = int(input())
    except:
        break
    count = '1'
    countnum = 1
    while True:
        if (int(count))%i == 0:
            break
        else:
            count += '1'
            countnum += 1
    print(countnum)
```

## 1037 문제

양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.?어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다. 둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.

## 출력

첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.

## 예제 입력 1

```
2
4 2
```

## 예제 출력 1

```
8
```

## 답안 코드

```python
N = int(input())
yaksu = list[N]
yaksu = list(map(int,input().split()))
yaksu.sort()
sum = yaksu[0] * yaksu[-1]
print(sum)
```

## 17427 문제

두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.

자연수 N이 주어졌을 때, g(N)을 구해보자.

## 입력

첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

## 출력

첫째 줄에 g(N)를 출력한다.

## 예제 입력 1

```
1
```

## 예제 출력 1

```
1
```

## 내 답안 코드

```python
def yaksu(a):
    sum = 0
    f = set()
    for i in range(a):
        if a%(i+1) == 0:
            f.add(i+1)
    while len(f) >= 1:
        sum += f.pop()
    return sum
        
N = int(input())
sum = 0
for i in range(N):
    sum += yaksu(i+1)
print(sum)
```

위의 경우 시간 복잡도가 n^2라서 시간 초과가 된다. 따라서 아래 정답 코드로 바꿔준다.

## 정답 코드

```python
n = int(input())

sum_ = 0
for i in range(1, n+1):
	# i의 배수의 개수 = i를 약수로 갖는 수
    sum_ += (n//i)*i

print(sum_)
```

## 17425 문제

두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.

자연수 N이 주어졌을 때, g(N)을 구해보자.

## 입력

첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 100,000)가 주어진다. 둘째 줄부터 테스트 케이스가 한 줄에 하나씩 주어지며 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

## 출력

각각의 테스트 케이스마다, 한 줄에 하나씩 g(N)를 출력한다.

## 예제 입력 1

```
5
1
2
10
70
10000
```

## 예제 출력 1

```
1
4
87
4065
82256014
```

## 내 답안 코드

```python
n = int(input())

for i in range(n):
    sum = 0
    a = int(input())
    for j in range(1, a+1):
        sum += (a//j)*j
    print(sum)
```

위의 경우에 시간 복잡도가 m*n으로 n^2에 가깝다. 따라서 시간초과

## 정답 코드

```python
# 최대값 설정
MAX=1000000

# DP 1로 초기화
dp = [1]*(MAX+1)

# S: 값 누적 리스트
s = [0]*(MAX+1)

for i in range(2, MAX+1):
    j=1
    while i*j <= MAX:
       # i의 배수에 값 추가
        dp[i*j] += i
        j += 1

for i in range(1, MAX+1):
   # 누적 값 계산
    s[i] = s[i-1] + dp[i]

n = int(input())
ans=[]
for _ in range(n):
		a=int(input())
    ans.append(s[a])
print('\n'.join(map(str, ans))+'\n')
```

위의 경우 시간 복잡도가 nlogn

## 2609 문제

두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

## 출력

첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

## 예제 입력 1

```
24 18
```

## 예제 출력 1

```
6
72
```

## 답안 코드

```python
A, B = list(map(int,input().split()))

if A > B:
    for i in range(1, B+1):
        if A%i == 0 and B%i == 0:
            yaksu = i
    i = 1
    while True:
        if (B*i) % A ==0 :
            baesu = B*i
            break
        i += 1
elif A < B:
    for i in range(1, A+1):
        if A%i == 0 and B%i == 0:
            yaksu = i
    i = 1
    while True:
        if (A*i) % B ==0 :
            baesu = A*i
            break
        i += 1
else:
    yaksu = A
    baesu = A

print(yaksu)
print(baesu)
```

## 1978 문제

주어진 수 N개?중에서?소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

## 입력

첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

## 출력

주어진 수들 중 소수의 개수를 출력한다.

## 예제 입력 1

```
4
1 3 5 7
```

## 예제 출력 1

```
3
```

## 답안 코드

```python
N = int(input())
num = list(map(int, input().split()))
num.sort()
N = num[-1]
count = 0

sosu = [0]*(N+1)
for i in range(2,N+1):
    for j in range(1,N//i+1):
        sosu[i*j] += 1
            
for i in num:
    if sosu[i] == 1:
        count += 1
        
print(count)
```

## 1929 문제

M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)?M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

## 출력

한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

## 예제 입력 1

```
3 16
```

## 예제 출력 1

```
3
5
7
11
13
```

## 답안 코드

```python
num = list(map(int, input().split()))
N = num[-1]
count = 0

sosu = [0]*(N+1)
for i in range(2,N+1):
    for j in range(1,N//i+1):
        sosu[i*j] += 1
            
for i in range(num[0],num[1]+1):
    if sosu[i] == 1:
        print(i)
```

## 6588 문제

1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

> 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
> 

예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

이 추측은 아직도 해결되지 않은 문제이다.

백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

## 입력

입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.

각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)

입력의 마지막 줄에는 0이 하나 주어진다.

## 출력

각 테스트 케이스에 대해서, n = a + b 형태로 출력한다. 이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다. 만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다. 또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.

## 예제 입력 1

```
8
20
42
0
```

## 예제 출력 1

```
8 = 3 + 5
20 = 3 + 17
42 = 5 + 37
```

## 답안 코드

```python
n = 1000001
# 소수 아닌 모든 홀수 처리
table = [1] * n
for i in range(3, int(n ** 0.5) + 1, 2):
    if table[i]:
        for j in range(i * 2, n, i):
            table[j] = 0
# k가 만들어지는 두 홀수인 소수 검색
while 1:
    k = int(input())
    if not k:
        break
    for i in range(3, int(k / 2) + 1, 2):
        if table[i] and table[k - i]:
            print(f"{k} = {i} + {k - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
```

제곱근을 이용하여 에라토스테네스의 체를 만드는 방법이다.