def solution(emergency):
    d = {v:i+1 for i, v in enumerate(sorted(emergency, reverse=True))}
    return [d[e] for e in emergency]

