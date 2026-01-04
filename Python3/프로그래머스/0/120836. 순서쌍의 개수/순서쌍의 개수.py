def solution(n):
    
    i, cnt = 1, 0
    while i <= n:
        if n % i == 0:
            cnt += 1
        i += 1
            
    return cnt