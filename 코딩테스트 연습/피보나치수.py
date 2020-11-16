def solution(n):
    num1 = 0
    num2 = 1
    for i in range(n-1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(num1, num2)

    return num2 % 1234567


solution(5)
