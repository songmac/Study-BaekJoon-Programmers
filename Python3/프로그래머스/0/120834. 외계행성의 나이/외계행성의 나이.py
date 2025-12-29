def solution(age):
    pgms_952 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    age_list = [int(d) for d in str(age)]
    return "".join(pgms_952[age_list[i]] for i in range(len(age_list)))
