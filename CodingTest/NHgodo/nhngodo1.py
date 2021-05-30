# 핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.

def solution(goods):
    total = sum(goods)
    count = 0
    for idx, val in enumerate(goods):
        if val >= 50:
            goods[idx] = 0
            count += 1

    if goods.count(0) == 1 and sum(goods) >= 50:
        count += 1
    if goods.count(0) == 0 and sum(goods) >= 50:
        count += 1

    print(total - 10*count)


solution([5, 3, 15])
