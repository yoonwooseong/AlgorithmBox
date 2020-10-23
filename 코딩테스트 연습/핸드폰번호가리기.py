def solution(phone_number):
    for i in range(len(phone_number)-4):
        answer += "*"
    answer += phone_number[-4:]
    return answer


solution("01033334444")

'''
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]
'''
