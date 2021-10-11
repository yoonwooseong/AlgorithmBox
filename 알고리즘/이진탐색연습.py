'''
이진 탐색이란 탐색 알고리즘 중 직관적이고 간단한 알고리즘이다.
한번 비교할 때마다 데이터의 양이 반씩 줄어드는 형태로 검색을 진행

출처:https://gomguard.tistory.com/112?category=711753
'''


def binary_search(data, number=0):
    mid = int(len(data)/2)
    if len(data) > 1:
        if data[mid] > number:
            binary_search(data[:mid], number)
        elif data[mid] < number:
            binary_search(data[mid:], number)
        else:
            print(number, "True")
    else:
        print(number, data[0] == number)


data = [1, 2, 3, 4, 5, 6, 7, 8]
binary_search(data, 5)
