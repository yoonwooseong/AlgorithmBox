def solution(a, b):
    sum = 0
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        sum += i
    return sum


'''
def adder(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))
'''
