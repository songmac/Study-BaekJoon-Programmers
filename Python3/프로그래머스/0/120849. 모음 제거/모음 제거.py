def solution(my_string):
    answer = ""
    for s in my_string:
        if s in ["a", "e", "i", "o", "u"]:
            continue
        answer += s
    return answer