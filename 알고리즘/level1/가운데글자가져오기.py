def solution(s):
    answer = len(s) % 2 == 0 and s[int(len(s)/2)-1]+s[int(len(s)/2)] or s[int(len(s)/2)]
    return answer

solution("qwer")