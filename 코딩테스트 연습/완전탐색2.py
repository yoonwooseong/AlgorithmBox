import itertools
from itertools import permutations
'''
def solution(numbers):
    sublist = []
    count = 0

    for i in range(1, len(numbers)+1):
        sublist += list(map(''.join, itertools.permutations(list(numbers), i)))

    for i in set(list(map(int, sublist))):
        if i != 1:
            checkcount = 0
            for j in range(2, i+1):
                if i % j == 0:
                    checkcount += 1
                    if checkcount >= 2:
                        break
                    if checkcount == 1 and i == j:
                        count += 1
    answer = count
    return answer


solution("011")
'''


def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i+1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5)+1):
        a -= set(range(i * 2, max(a)+1, i))
    return len(a)


'''
1
2
3

12 13            1*갯수 -1
21 23
31 32

123 132          1*2
213 231
312 321


1234

1
2
3
4

12 13 14        1*3
21 23 24
31 32 34
41 42 43

123 124 132 134 142 143        1*6

        temp = numbers[0]
        numbers[0] = numbers[1]
        numbers[1] = temp
'''
