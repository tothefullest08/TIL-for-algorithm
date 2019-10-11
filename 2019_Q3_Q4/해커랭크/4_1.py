import sys
sys.stdin = open('4.txt','r')


# 1초 내 트랜잭션 갯수는 3을 초과할 수 없음
# 10초 내 트랜잭션의 갯수는 20을 초과할 수 없음
# 10초 기간은 T초에서 T+9초 내 모드 트랜잭션을 카운트함
# 1분내 트랜잭션 MAX : 60개

# 제한을 초과하는 요청은 게이트웨이에 의해 드랍됨


def droppedRequests(requestTime):
    requestTime.sort()
    M = [0] * (max(requestTime)+1)
    ans = 0
    for i in requestTime:
        M[i]+=1
    total = 0
    ten = 10
    six = 60
    for m in range(1,len(M)):
        total += M[m]
        if M[m]>3:
            ans += M[m]-3
        if six-60< m <= six and total > 60:
            ans += 1
            if m ==six:
                six += 60
        elif ten-10 < m <= ten and total >20:
            ans += 1
            if m == ten:
                ten += 10
    return ans

N = int(input())
requestTime = [int(input()) for _ in range(N)]
print(droppedRequests(requestTime))