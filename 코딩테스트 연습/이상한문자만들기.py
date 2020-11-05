def solution(s):
    for idx, val in enumerate(list(s)):
        if idx > 1:
            if s[idx-1] == " " and s[idx] != " ":
                s[idx]

solution("try hello world")


'''
def solution(s):
    lists = s.split(" ")
    result = ""
    for i in lists:
        for idx, val in enumerate(list(i)):
            if idx % 2 == 0:
                val = val.upper()
            result += val
        result += " "
    return result[:-1]
'''