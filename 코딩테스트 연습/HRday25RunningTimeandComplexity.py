# Enter your code here. Read input from STDIN. Print output to STDOUT
def solution(n):
    if n < 2:
        return False
    v = int(n**0.5)
    for i in range(2, v+1):
        if n % i == 0:
            return False
    return True


n = int(input())
for i in range(n):
    if solution(int(input())):
        print("Prime")
    else:
        print("Not prime")


'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
def solution(numlist):
    n = max(numlist)
    distinguish = [False, False] + [True]*(n-1)
    m = int(n**0.5)
    for i in range(2, m+1):
        if distinguish[i] == True:
            for j in range(i*2, n+1, i):
                distinguish[j] = [False]
    return distinguish

n=int(input())
numlist= []
for i in range(n):
    numlist.append(int(input()))
distinguish = solution(numlist)

for i in numlist:
    if distinguish[i] == True:
        print("Prime")
    else:
        print("Not prime")
'''
