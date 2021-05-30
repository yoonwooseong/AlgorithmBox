def solution(brown, yellow):
    answer = []
    for i in range(1,int(yellow**0.5)+1):
        if yellow%i == 0 and i*2+int(yellow/i)*2+4 == brown:
            answer.append(int(yellow/i)+2)
            answer.append(i+2)
    print(answer)
    return answer

solution(24,24)