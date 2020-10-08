'''
출처: https://gomguard.tistory.com/120?category=711753
'''

# 거리를 short라는 list에 삽입
short = []
index = ['0.집', '1.미용실', '2.슈퍼마켓', '3.영어학원', '4.레스토랑', '5.은행', '6.학교']
short.append([0, 5, 10, 9, 999, 999, 999])
short.append([5, 0, 3, 999, 999, 11, 999])
short.append([10, 3, 0, 7, 3, 10, 999])
short.append([9, 999, 7, 0, 999, 7, 12])
short.append([999, 999, 3, 999, 0, 4, 999])
short.append([999, 11, 10, 7, 4, 0, 2])
short.append([999, 999, 999, 12, 999, 2, 0])

# 출발지, 도착지를 받았을때 계산하기 쉽게 테이블 변환


def convert_table(short, n):
    for i in range(len(short)):
        short[i].insert(0, short[i].pop(n[0]))
        short[i].insert(len(short)-1, short[i].pop(n[1]))
    short.insert(0, short.pop(n[0]))
    short.insert(len(short)-1, short.pop(n[1]))
    print(short)
    return short


# 변환된 테이블에서 최단거리를 계산하는 함수
def calc_table(short):
    for n in range(2, len(short)):
        for i in range(len(short)-n):
            temp = []
            for j in range(n):
                if j == (n-1):
                    temp.append(short[i+j+1][i])
                else:
                    temp.append(short[i+j+1][i]+short[i+n][i+j+1])
            short[i+n][i] = min(temp)
            del temp
    return short


# 시작점과 도착점 입력 받기 위한 텍스트 출력 부분
print(index)
print('시작점 도착점 공백을 구분해 입력해주세요.: ex) 1 3')

# 시작점과 도착점 입력 받을 때 값 검사하는 부분
while True:
    try:
        i = sorted(list(map(int, input().split())))
        if i[0] < 0 or i[1] >= len(short):
            raise ValueError
        break
    except ValueError:
        print('위치 인덱스를 잘못 입력했습니다.')

# 실행부 - 시작점과 도착점이 같을 떄 거리는 0, 다른 경우 계산
if index[i[0]] == index[i[1]]:
    distance = 0
else:
    short = convert_table(short, i)
    short = calc_table(short)
    [print(short[i]) for i in range(len(short))]
    distance = short[len(short)-1][0]

print('{} 과 {} 의 최단거리는 {} 입니다.'.format(index[i[0]], index[i[1]], distance))
