from datetime import date


def solution(a, b):
    daylist = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date(2016, a, b).weekday()
    return daylist[day]

    '''
def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    gap = date(2016, a, b) - date(2016, 1, 1)
    return day[int(str(gap).split(" ")[0]) % 7]
    '''


solution(5, 24)
