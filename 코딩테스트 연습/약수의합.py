def solution(n):
    result = []
    m = int(n**0.5)
    for i in range(1, m+1):
        if n % i == 0:
            result.append(i)
            result.append(n//i)
    result = list(set(result))
    print(result)
    return sum(result)

solution(1)