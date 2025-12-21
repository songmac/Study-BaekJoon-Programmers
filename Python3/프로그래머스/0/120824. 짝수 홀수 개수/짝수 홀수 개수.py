def solution(num_list):
    e, d = 0, 0
    for i in num_list:
        if i % 2 == 0:
            e += 1
        else:
            d += 1
            
    return [e, d]