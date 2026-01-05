def solution(hp):
    a = hp // 5
    hp %= 5
    b = hp // 3
    hp %= 3
    c = hp
    return a + b + c
