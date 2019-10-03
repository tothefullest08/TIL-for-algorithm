# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자 구하기

import itertools

def solution(number, k):

    N = len(numbers)

    idx_dict = {}
    for i in range(N):
        idx_dict[numbers[i]] = i

    answer = 0
    for permu in list(itertools.permutations(numbers, N - k)):
        print(permu)
        tmp = []
        flag = False
        sub_answer = 0
        for i in permu: tmp.append(idx_dict[i])

        for j in range(len(tmp) - 1):
            if tmp[j] > tmp[j + 1]:
                flag = True

        if not flag:
            sub_answer = int(''.join(permu))

        if answer < sub_answer:
            answer = sub_answer

    return answer


numbers = "1231234"
numbers = list(numbers)
k = 2
print(solution(numbers, k))

