


import itertools

# n개의 음이 아닌 정수가 있음. 이수를 적절히 더하거나 빼서 타켓 넘버를 구하려고함.

numbers = [1,1,1,1,1]
target = 3


def solution(numbers, target):
    cal = [1, 0]
    N = len(numbers)
    permu_lst = list(itertools.product(cal, repeat=N))
    answer = 0
    for sub_permu in permu_lst:
        tmp = 0
        for i in range(N):
            if sub_permu[i] == 1:
                tmp += numbers[i]
            else:
                tmp -= numbers[i]
        if tmp == target:
            answer += 1

    return answer


print(solution(numbers, target))


