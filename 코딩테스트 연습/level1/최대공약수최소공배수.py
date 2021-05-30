from math import gcd


def solution(n, m):
    print([gcd(n, m), n*m/gcd(n, m)])
    return [gcd(n, m), n*m/gcd(n, m)]


'''
유클리드 호제법 
x : ab
y : bc
x*y = ab^2c / b = abc

여기서 b는 최대공약수
'''
solution(3, 12)
