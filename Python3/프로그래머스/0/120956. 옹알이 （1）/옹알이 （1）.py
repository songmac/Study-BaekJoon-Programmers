def solution(babbling):
    # 발음할 수 있는 단어 목록
    sounds = ["aya", "ye", "woo", "ma"]
    
    # 발음 가능한 단어 개수
    answer = 0

    # babbling 배열에 있는 각 단어에 대해 검사
    for word in babbling:
        prev = ""      # 직전에 사용한 발음을 저장 (연속 사용 방지용)
        i = 0          # 현재 검사 중인 문자열 인덱스
        valid = True   # 해당 단어가 발음 가능한지 여부

        # 문자열 끝까지 검사
        while i < len(word):
            matched = False  # 이번 위치에서 발음이 매칭되었는지 여부

            # 가능한 모든 발음을 순회
            for s in sounds:
                # 현재 위치에서 발음 s로 시작하고,
                # 직전에 사용한 발음과 같지 않은 경우
                if word.startswith(s, i) and s != prev:
                    i += len(s)   # 발음 길이만큼 인덱스 이동
                    prev = s      # 직전 발음 갱신
                    matched = True
                    break         # 하나만 매칭되면 바로 종료

            # 어떤 발음도 매칭되지 않으면 실패
            if not matched:
                valid = False
                break

        # 끝까지 정상적으로 분해되었으면 정답 개수 증가
        if valid:
            answer += 1

    return answer
