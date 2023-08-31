# n = int(input())

# for i in range(n):
#     sum = 0
#     a = int(input())
#     for j in range(1, a+1):
#         sum += (a//j)*j
#     print(sum)

# ���� ��쿡 �ð� ���⵵�� m*n���� n^2�� ������. ���� �ð��ʰ�

# �ִ밪 ����
MAX=1000000

# DP 1�� �ʱ�ȭ
dp = [1]*(MAX+1)

# S: �� ���� ����Ʈ
s = [0]*(MAX+1)

for i in range(2, MAX+1):
    j=1
    while i*j <= MAX:
       # i�� ����� �� �߰�
        dp[i*j] += i
        j += 1

for i in range(1, MAX+1):
   # ���� �� ���
    s[i] = s[i-1] + dp[i]

n = int(input())
ans=[]
for _ in range(n):
    a=int(input())
    ans.append(s[a])
print('\n'.join(map(str, ans))+'\n')