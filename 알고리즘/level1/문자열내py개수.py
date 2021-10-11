def solution(s):
    pnum = 0
    ynum = 0
    for i in list(s.lower()):
        print(i)
        if i == 'p':
            pnum += 1
        if i == 'y':
            ynum += 1
    if pnum == ynum:
        return True
    else:
        return False


'''
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
'''
solution("pPoooyY")
