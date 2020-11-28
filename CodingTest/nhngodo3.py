def solution(s, n):
    resultnum = []
    stack = list(s)
    stack2 = set(list(s))
    for i in stack2:
        resultnum.append(stack.count(i))
    resultnum.sort()
    print(resultnum)
    while True:
        if n <= 0:
            break
        else:
            for idx, val in enumerate(resultnum):
                if n <= 0:
                    break
                if val-n <= 0:
                    resultnum.pop(idx)
                n -= val
    print(resultnum)
    if len(resultnum) == 1:
        print(0)
    else:
        print(max(resultnum) - min(resultnum))


'''
    maxnum = 0
    minnum = 50
    stack = list(s)
    stack2 = set(list(s))
    for i in stack:
        if stack.count(i) >= maxnum:
            maxnum = stack.count(i)
        if stack.count(i) <= minnum:
            minnum = stack.count(i)

    if n > maxnum:
        n2 = n - maxnum
        n -= maxnum


    for i in stack2:
        if n == stack.count(i):
            for j in range(n):
                stack.remove(i)

    for i in stack:
        if stack.count(i) >= maxnum:
            maxnum = stack.count(i)
        if stack.count(i) <= minnum:
            minnum = stack.count(i)
    print(stack)
    print(maxnum - minnum)
'''

'''
def solution(s, n):
    stack = list(s)
    maxnum = 0
    minnum = 50
    minstr = ""
    for i in stack:
        if stack.count(i) >= maxnum:
            maxnum = stack.count(i)
        if stack.count(i) <= minnum:
            minnum = stack.count(i)
            minstr = i

    if stack.count(minstr) == n:
        n -= stack.count(minstr)
        for i in range(stack.count(minstr)):
            stack.remove(minstr)

    return stack, maxnum, minnum, minstr, n
'''

solution("aaaabbbbc", 5)
