import sys
sys.stdin = open('bj14501_퇴사.txt', 'r')

# 오늘부터 N+1 째 되는 날 퇴사. 남은 N일 동안 최대한 상담
# 하루에 하나씩 서로 다른 사람의 상담 잡아 놓음.
#
# 상담을 통해 최대한 수익을 구할 수 있는 프로그램 작성

def DFS(start_day):
    global sub_total, total

    # 현재 날짜가 퇴사일보다 같거나 큰 경우 return
    if start_day >= N:
        # 현재 누적된 sub_total 값이 total 보다 큰경우 => total 값 업데이트
        if sub_total > total:
            total = sub_total
        return

    for i in range(N):
        if not visited[i]:
            time = data[i][0]  # 상담 소요일
            pay = data[i][1]  # 상담 금액
            next_day = i + time  # 현재 날짜 + 상담 소요일 => 상담 끝난 날

            # 상담 끝난 날이 퇴사일을 초과하는 경우
            if next_day > N:
                DFS(next_day)
            # 상담 끝날 날이 퇴사 전인 경우
            else:
                # 상담 한 날까지 visited 값 변경
                for j in range(next_day): visited[j] = 1
                sub_total += pay

                DFS(next_day)

                # 백트래킹: 추가된 상담일의 일정을 다시 제거
                for j in range(start_day, next_day): visited[j] = 0
                sub_total -= pay

N = int(input())
data = []
for _ in range(N):
    init_time, init_pay = map(int, input().split())
    data.append([init_time, init_pay])
sub_total, total = 0, 0
visited = [0] * N
DFS(0)
print(total)