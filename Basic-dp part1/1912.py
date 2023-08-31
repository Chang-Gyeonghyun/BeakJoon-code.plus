import sys
n = int(input())
nums = list(map(int,input().split()))
max_from=-sys.maxsize
result = -sys.maxsize
for x in nums:
    max_from = max(max_from+x,x)
    result = max(max_from,result)
print(result)