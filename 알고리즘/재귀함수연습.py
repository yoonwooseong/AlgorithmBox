'''
재귀함수란 어떤 함수에서 자신을 다시 호출하여 작업을 수행하는 방식
반복문을 재귀함수로 구현 가능
작성 시 함수내에서 다시 자신을 호출한 후 그 함수가 끝날 때 까지
1. 함수 호출 이후의 명령문이 수행되지 않는 다는 사실과
2. 종료조건이 꼭 포함되어야 한다는 부분을 인지해야함
'''


def countdown(n):
    if n == 0:
        print("boom")
    else:
        print(n, end=' ')
        countdown(n-1)


countdown(10)


def multi_table_2(n):
    if n == 10:
        print('end')
    else:
        print('2 * {} = {}'.format(n, 2*n))
        multi_table_2(n+1)


multi_table_2(1)


def multi_table_3(n):
    if n == 0:
        print('end')
    else:
        multi_table_3(n-1)
        print('2 * {} = {}'.format(n, 2*(n)))


multi_table_3(9)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))
