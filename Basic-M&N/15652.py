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