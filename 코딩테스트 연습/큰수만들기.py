def solution(number, k):
    stack = [number[0]]
    for i in number[1:]:
        while len(stack) > 0 and stack[-1] < i and k > 0:
            k -= 1
            stack.pop()
        stack.append(i)

    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


'''
import copy
def solution(number, k):
    if number[k-1] < number[k]:
        return number[k:]
    else:
        imlist = copy.deepcopy(number[1:k])
        prenum = number[k-1]
        for i in number[0:k-1].reverse():
            if prenum < i:
                imlist.pop(0)
'''
solution("1924", 1)
