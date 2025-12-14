def solution(babbling):
    sounds = ["aya", "ye", "woo", "ma"]
    answer = 0

    for word in babbling:
        prev = ""
        valid = True

        while word:
            matched = False

            for s in sounds:
                if word.startswith(s) and s != prev:
                    word = word[len(s):]  # 앞부분 제거
                    prev = s
                    matched = True
                    break

            if not matched:
                valid = False
                break

        if valid:
            answer += 1

    return answer
