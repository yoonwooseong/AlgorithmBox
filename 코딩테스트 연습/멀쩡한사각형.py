from math import gcd


def solution(w, h):
    return w*h - (w+h-gcd(w, h))


'''
def solution(w, h):
    total = w*h
    result = 0

    result_num = counts(w, h)
    while True:
        if w == h or result_num == 0:
            result += w
            print(total - result)
            return total - result
        else:
            if w > h:
                result += h
                w = result_num
            else:
                result += w
                h = result_num
            result_num = counts(w, h)


def counts(num1, num2):
    # num1이 크게
    if num2 > num1:
        num1, num2 = num2, num1
    return num1 - num2
'''

solution(29999999, 2999991)
