def solution(prices):
    result = [0]*len(prices)

    for i in range(len(prices)):
        cur = prices.pop(0)
        for val in prices:
            result[i] += 1
            if val < cur:
                break

    print(result)


'''
def solution(prices):
    result = [0]*len(prices)

    for i in range(len(prices)):
        cur = prices.pop(0)
        if len(prices) != 0:
            if cur <= min(prices):
                result[i] += len(prices)
            else:
                for val in prices:
                    result[i] += 1
                    if val < cur:
                        break

    print(result)
'''

solution([1, 2, 3, 2, 3])
