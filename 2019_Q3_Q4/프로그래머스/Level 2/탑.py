# 수평 직선에 탑 N대 세움
# 탑 꼭대기에는 송/수신 장치 설치
# 발사한 신호는 보낸 탑보다 높은에서만 수신. 수신된 신호는 다른 탑으로 송신되지 않음



def solution(heights):
    N = len(heights)
    answer = [0]
    for current_top in range(1, N):
        for previous_top in range(current_top, -1, -1):
            if heights[previous_top] > heights[current_top]:
                answer.append(previous_top+1)
                break
        else:
            answer.append(0)

    return answer

heights = [1,5,3,6,7,6,5]
print(solution(heights))