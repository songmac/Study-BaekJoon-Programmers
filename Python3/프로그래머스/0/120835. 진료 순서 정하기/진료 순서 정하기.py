def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    rank = {value: idx + 1 for idx, value in enumerate(sorted_emergency)}
    return [rank[value] for value in emergency]
