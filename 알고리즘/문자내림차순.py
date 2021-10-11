def solution(s):
    answerlist = list(s)
    answerlist.sort(reverse=True)
    answer = ""
    for i in answerlist:
        answer += i
    return answer


'''
def solution(s):
    s=list(s)
    return ''.join(sorted(s, reverse=True))
'''
