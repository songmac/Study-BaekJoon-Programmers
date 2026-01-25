import math as m

def solution(balls, share):
    return m.factorial(balls) / (m.factorial(balls-share) * m.factorial(share))