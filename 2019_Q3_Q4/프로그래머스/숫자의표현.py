def solution(N):
    start_num = 1
    ans = 0
    while True:
        sub_ans = 0
        for i in range(start_num, N+1):
            if sub_ans < N:
                sub_ans += i
            elif sub_ans == N:
                ans += 1
                break
            elif sub_ans > N:
                break

        start_num += 1

        if start_num > N:
            break
    ans += 1
    return ans

N = 15
print(solution(N))