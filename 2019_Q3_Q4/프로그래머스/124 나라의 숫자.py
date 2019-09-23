# 124 나라
# 124 나라에서는 10진법이 자신만의 규칙으로 수 표현
# 1. 자연수만 존재
# 2. 모든 수를 표현할 때, 1,2,4만 사용


def solution(n):
    num = {1: "1", 2:"2", 0:"4"}
    mok, nam, answer = 1, 1, ''
    while mok:
        mok = n // 3
        nam = n % 3

        if nam == 0:
            mok -= 1

        n = mok
        answer = num[nam] + answer

    return answer


print(solution(10))