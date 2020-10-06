'''
버블 정렬은 두 인접한 값들을 검사하여 정렬하는 방법이다.
시간이 오래걸리나 단순해 자주 사용된다.
'''

a = [3, 2, 4, 1]
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
'''
2 3 4 1

2 3 4 1

2 3 1 4

2 1 3 4

1 2 3 4
'''
print(a)

# 재귀 알고리즘을 사용한 버블 정렬 코드

b = [3, 2, 5, 1, 4, 6]


def bubble_sort(n=0, i=0):

    if i == len(b)-1:
        return
    else:
        if n < len(b)-1:
            if b[n] > b[n+1]:
                b[n], b[n+1] = b[n+1], b[n]
            bubble_sort(n+1, i)
        else:
            bubble_sort(0, i+1)


bubble_sort()
'''
235146
235146
231546
231456
231456
'''
print(b)
