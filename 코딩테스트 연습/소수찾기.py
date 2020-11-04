# 에라토스테네스의 체
# n값까지 소수 몇개인지 판별할때 좋고
# n이 소수인지만 판별할때는 그냥 for문 한번 O(n)이 좋다. - HR Day25 RunningTime and Complexity 참고
def solution(n):
    distinguish = [False, False]+[True]*(n-1)
    m = int(n**0.5)
    for i in range(2, m+1):
        if distinguish[i] == True:
            for j in range(i*2, n+1, i):
                distinguish[j] = False
    print(distinguish)
    return distinguish.count(True)
    # return [i for i in range(2, n) if distinguish[i] == True]


solution(5)
'''

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''
