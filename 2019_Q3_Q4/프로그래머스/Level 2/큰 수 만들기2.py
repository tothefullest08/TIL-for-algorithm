# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자 구하기

import itertools

def solution(numbers, k):
    answer = 0
    for combi in list(itertools.combinations(numbers, len(numbers) - k)):
        print(combi)
        tmp = ''.join(combi)
        tmp = int(tmp)
        if answer < tmp:
            answer = tmp

    return str(answer)

numbers = "1231234"
k = 3
print(solution(numbers, k))
