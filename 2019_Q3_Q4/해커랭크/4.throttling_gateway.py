import sys

sys.stdin = open('4.throttling_gateway.txt', 'r')


def droppedRequests(requestTime):

    sec_array = [0] * (max(requestTime)+1)
    N = len(sec_array)

    for i in requestTime:
        sec_array[i] += 1

    print(sec_array)

    ten, current_ten = 10, 0
    sixty, current_sixty = 60, 0
    ans = 0
    for i in range(1,N):
        current_ten += sec_array[i]
        current_sixty += sec_array[i]

        # 1초 단위 조건
        if sec_array[i] > 3:
            ans += sec_array[i] - 3

        # 10초 단위 조건
        if ten-10 < i <= ten and current_ten > 20:
            if current_ten - sec_array[i] <= 20:
                # 경계에 걸리는 경우
                # (예; current_ten 이 21이며, sec_array[i]가 3인 경우,
                #      sec_array[i]값을 단순히 더할게 아니라, current_ten - sec_array[i] 값인 1을 더해야함
                ans += current_ten - 20
            else:
                ans += sec_array[i] # 이후에는 갯수만큼 더함
            if i == ten:
                ten += 10 # 10초단위에 걸릴 경우, 값 초기화
                current_ten = 0

        # 60초 단위 조건. 하위조건은 10초단위때와 동일
        if sixty - 60 < i <= sixty and current_sixty > 60:
            if current_sixty - sec_array[i] <= 60:
                ans += current_sixty - 60
            else:
                ans += sec_array[i]
            if i == sixty:
                sixty += 60
                current_sixty = 0

    return ans


N = int(input())
requestTime = [int(input()) for _ in range(N)]
print(droppedRequests(requestTime))