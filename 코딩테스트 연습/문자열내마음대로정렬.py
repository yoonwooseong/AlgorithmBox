def solution(strings, n):
    return sorted(sorted(strings), key=lambda strings: strings[n])

# 파이썬에서 "lambda" 는 런타임에 생성해서 사용할 수 있는 익명 함수 입니다


'''
def strange_sort(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)
    return strings
'''
solution(["sun", "bed", "car"], 1)
