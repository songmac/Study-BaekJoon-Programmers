def solution(n):
    result = n // 7
    if n % 7 > 0 :
        result += 1
    return result