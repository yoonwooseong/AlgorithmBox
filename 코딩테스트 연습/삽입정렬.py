'''
삽입 정렬이란 앞의 숫자들을 정렬된 상태라고 가정한 뒤 
정렬되지 않은 숫자들을 하나씩 빼서 정렬되어 있는 숫자 사이의
올바른 위치에 삽입하는 정렬 방법을 의미한다
'''

a = [4, 1, 5, 2, 3]

for i in range(1, len(a)):
    for j in range(i):
        if a[i] < a[j]:
            a.insert(j, a.pop(i))

print(a)

b = [4, 1, 5, 2, 3, 6]


def basic(i=0, j=0):
    if j == len(b):
        return
    else:
        if i == j:
            basic(0, j+1)
        else:
            if b[i] > b[j]:
                b.insert(i, b.pop(j))
            basic(i+1, j)


basic(0, 0)
print(b)
