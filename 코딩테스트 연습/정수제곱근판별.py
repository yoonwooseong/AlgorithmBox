def solution(n):
    result = (n ** 0.5) % 1 == 0 and (n**0.5+1)**2 or -1
    return result


# n ** 0.5    ( n ** 0.5 +1) ** 2
solution(121)
