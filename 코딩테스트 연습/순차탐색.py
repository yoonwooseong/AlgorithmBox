'''
순차 탐색은 첫번째부터 하나씩 탐색하는 방법으로 비효율적인 단점이 있다.
'''

data = [1, 2, 3, 4, 5]
a = 3
chk = False
for i in data:
    if a == i:
        chk = True
        print(chk)
        break
    else:
        print(chk)
