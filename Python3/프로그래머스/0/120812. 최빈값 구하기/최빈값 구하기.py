from collections import Counter

def solution(array):
    cnt = Counter(array)
    max_freq = max(cnt.values())
    
    answer = [k for k, v in cnt.items() if v == max_freq]
    if len(answer) == 1:
        return answer[0]
    
    return -1