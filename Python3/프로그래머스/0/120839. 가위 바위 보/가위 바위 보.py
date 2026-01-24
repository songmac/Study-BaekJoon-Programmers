def solution(rsp):
    mapping = {'0': '5', '2': '0', '5': '2'}
    return ''.join(mapping[i] for i in rsp)
