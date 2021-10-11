# for-else문 중간에 break 등으로 끊기지 않고 끝까지 수행되면 else문 실행
def solution(skill, skill_trees):
    skill = list(skill)
    result = len(skill_trees)

    for val in skill_trees:
        preIndex = -2
        count = 0
        for i in skill:
            if preIndex == -1 and val.find(i) != -1:
                print(val)
                count += 1
                break
            if val.find(i) < preIndex and val.find(i) != -1:
                print(val)
                count += 1
                break
            else:
                preIndex = val.find(i)
        if count == 1:
            result -= 1

    print(result)
    return result


solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
'''
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
'''
