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