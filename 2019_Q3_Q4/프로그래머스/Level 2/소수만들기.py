# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 함

prime_lst = [1] * 3002
prime_lst[0] = 0
prime_lst[1] = 0

for i in range(2, len(prime_lst)):
    if prime_lst[i] == 1:
        for j in range(i*i, len(prime_lst), i):
            prime_lst[j] = 0


import itertools

def solution(nums):
    answer = 0

    for combi in list(itertools.combinations(nums, 3)):
        if prime_lst[sum(combi)]:
            answer += 1

    return answer


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
