n=int(input())
array=list(map(int, input().split()))

d=[0]*n
d[0]=1
for i in range(1,n):
  for j in range(i):
    if array[j]>array[i]:
      d[i]=max(d[i], d[j]+1)
    else:
      d[i]=max(d[i], 1)

print(max(d))