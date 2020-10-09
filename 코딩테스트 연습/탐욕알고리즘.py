'''
탐욕 알고리즘은 최적해를 구하는 상황에서 사용하는 방법
여러 경우 중 하나를 선택할 때 그것이 그 상황에서 가장 좋다고 생각하는
것을 선택해 나가는 방식으로 진행하여 답을 구한다.

그러나 그 상황에서 선택해나가기 때문에 결과가 최적해는 아니다!
'''


def min_calc(value, coin):
    a = []
    for i in coin:
        a.append([value-i, i])
    res = a[0]
    for i in a:
        if res[0] > i[0] and i[0] > 0:
            res = i
    return res


coin = [1, 50, 100]
value = [362, 0]
dic = {}

for i in coin:
    dic[i] = 0

while True:
    value = min_calc(value[0], coin)
    if value[0] < 0:
        break
    else:
        dic[value[1]] += 1

print(dic)

'''
362 [1, 50, 100]
[361,1]
[312,50]
[262,100]
>361


'''
