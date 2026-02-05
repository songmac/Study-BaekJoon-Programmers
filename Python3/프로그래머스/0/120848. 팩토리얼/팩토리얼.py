def solution(n):
    
    i, result = 1, 1
    while True:
        result *= i
        if result == n:
            return i
        elif result > n:
            return i - 1
        else :
            i += 1


        
