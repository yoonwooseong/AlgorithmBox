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
