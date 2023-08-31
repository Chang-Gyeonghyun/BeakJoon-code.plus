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