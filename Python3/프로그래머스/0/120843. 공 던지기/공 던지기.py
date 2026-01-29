def solution(numbers, k):
    i = 0
    for _ in range(k - 1):
        i = (i + 2) % len(numbers)
    return numbers[i]
