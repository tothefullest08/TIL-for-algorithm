# 선행스킬: 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬
# ex) 선행 스킬 순서가 [스파크 -> 라이트닝 볼트 -> 썬더] 일 경우, 썬더를 배우려면 앞의 스킬들을 배워야함
# 위 순서가 없는 다른 스킬들은 순서와 상관없이 배울 수 있음
# 선행 스킬 순서 skill과  유저들이 만든 스킬트리를 담음 skill trees가 주어질 때, 가능한 스킬트리의 갯수를 return

def solution(skill, skill_trees):
    skill = list(skill)
    answer = 0
    for skill_tree in skill_trees:
        N  = len(skill_tree)
        skill_learned = []
        skill_tree = list(skill_tree)
        flag = False

        for i in range(N):
            if skill_tree[i] not in skill:
                continue
            else:
                skill_learned.append(skill_tree[i])
                if skill_learned.index(skill_tree[i]) != skill.index(skill_tree[i]):
                    flag = True
                    break
        if not flag:
            answer += 1


    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))