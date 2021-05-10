def solution(s):
    new_list = []
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] not in new_list:
                print("결과 : " + s[i:j] + ", i : "+str(i) + ", j : "+str(j))
                if check(list(s[i:j])) == False:
                    print("여기")
                    new_list.append(s[i:j])
                    count += 1
                else:
                    break

    print(count)


def check(seq):
    return len(seq) != len(set(seq))


solution("abac")
