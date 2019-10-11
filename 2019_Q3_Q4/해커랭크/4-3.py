import sys
sys.stdin = open('4.txt','r')


# 1초 내 트랜잭션 갯수는 3을 초과할 수 없음
# 10초 내 트랜잭션의 갯수는 20을 초과할 수 없음
# 10초 기간은 T초에서 T+9초 내 모드 트랜잭션을 카운트함
# 1분내 트랜잭션 MAX : 60개

# 제한을 초과하는 요청은 게이트웨이에 의해 드랍됨


def droppedRequests(requestTime):
    # requestTime.sort()
    M = [0] * (max(requestTime)+1)

    for i in requestTime:
        M[i]+=1
    ten,Now_ten = 10,0
    six,Now_six = 60,0
    ans = 0
    for m in range(1,len(M)):
        Now_ten += M[m]
        Now_six += M[m]
        if M[m] > 3:
            ans += M[m]-3
        if ten-10 < m <= ten and Now_ten > 20:
            if Now_ten-M[m]<=20:
                ans += Now_ten - 20

            else:
                ans += M[m]
            if m == ten:
                ten += 10
                Now_ten = 0
        if six-60 < m <= six and Now_six > 60:
            if Now_six - M[m] <= 60:
                ans += Now_six - 60
            else:
                ans += M[m]
            if m == six:
                six += 60
                Now_six = 0
    return ans

N = int(input())
requestTime = [int(input()) for _ in range(N)]
print(requestTime)
print(droppedRequests(requestTime))