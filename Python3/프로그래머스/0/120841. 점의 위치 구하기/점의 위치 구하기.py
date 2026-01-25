def solution(dot):
    x, y = dot
    quadrant = {
        (True, True): 1,
        (False, True): 2,
        (False, False): 3,
        (True, False): 4
    }
    return quadrant[(x > 0, y > 0)] # 튜플 (True / False, True / False) 값을 나타냄
