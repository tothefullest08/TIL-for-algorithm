import sys
sys.stdin = open('4.txt','r')


# 1초 내 트랜잭션 갯수는 3을 초과할 수 없음
# 10초 내 트랜잭션의 갯수는 20을 초과할 수 없음
# 10초 기간은 T초에서 T+9초 내 모드 트랜잭션을 카운트함
# 1분내 트랜잭션 MAX : 60개

# 제한을 초과하는 요청은 게이트웨이에 의해 드랍됨


def droppedRequests(requestTime):
    requestTime.sort()
    max_sec = max(requestTime)

    time_array = [[0,0,0] for _ in range(max_sec+1)]
    N = len(time_array)
    ans = 0
    for sec in requestTime:
        time_array[sec][0] += 1

    ten = 10
    six = 60
    for sec in range(1, N):
        if time_array[sec][0] > 3:
            dropped = time_array[sec][0] - 3
            ans += dropped
            time_array[sec][0] = time_array[sec][0] - dropped

        time_array[sec][1] = time_array[sec-1][1] + time_array[sec][0]
        time_array[sec][2] = time_array[sec-1][1] + time_array[sec][0]

        if ten-10 < sec <= ten and time_array[sec][1] > 20:
            

    print(time_array)
    print(ans)



    return ans

N = int(input())
requestTime = [int(input()) for _ in range(N)]
print(requestTime)
print(droppedRequests(requestTime))