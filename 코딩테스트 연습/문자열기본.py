def solution(s):
    if len(s) < 4 or len(s) > 6:
        return False
    else:
        for i in list(s):
            if ord(i) < 48 or ord(i) > 57:
                return False
        return True

# isalpha함수는 문자열이 문자인지 아닌지를 True,False로 리턴해주고,
# isdigit함수는 문자열이 숫자인지 아닌지를 True,False로 리턴해줍니다.


'''
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
'''
solution("67890")
