

import itertools

def solution(numbers):

    tmp, answer = [], 0
    for i in range(1, len(numbers) + 1):
        for j in itertools.permutations(numbers, i):
            sub_tmp = ''
            for k in j:
                sub_tmp += k
            if int(sub_tmp) not in tmp:
                tmp.append(int(sub_tmp))

    for i in tmp:
        if prime_lst[i]:
            answer += 1

    return answer

prime_lst = [1] * 9999999
prime_lst[0], prime_lst[1] = 0, 0

for i in range(2, 9999999):
    if prime_lst[i] == 1:
        for j in range(i*i, 9999999, i):
            prime_lst[j] = 0


numbers = '17'
print(solution(numbers))



