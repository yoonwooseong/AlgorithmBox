from math import gcd


def solution(arr):
    cur = arr.pop(0)
    while True:
        if len(arr) == 0:
            print(cur)
            return cur
        else:
            cur = gongbaesu(cur, arr.pop(0))


def gongbaesu(n, m):
    return int(n*m/gcd(n, m))


solution([2, 6, 8, 14])

'''
from fractions import gcd


def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer
'''
