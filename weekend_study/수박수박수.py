def solution(n):
    return ''.join(['수' if (i+1) % 2 != 0 else '박' for i in range(n)])

# 리스트 컴프리헨션