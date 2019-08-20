import sys
sys.stdin = open('bj13458_시험감독.txt', 'r')

# 시험장 N개, 각각의 시험장 응시자의 수: Ai
# 감독관: 총감독관 & 부감독관
# 총감독관읜 감시가능 응시자수:B명
# 부감독관의 감시가능 응시자수:C명
# 총감독관은 반드시 1명
# 부감독관은 여러명 가능
# 응시자수를 모두 감시하기위한 최소 감독관 수 구하기

# 1번째 줄: 시험장의 개수
# 2번째 줄: 각 시험장의 응시자 수 Ai
# 3번째 줄 : B, C 값

N = int(input())
student_lst = list(map(int, input().split()))
head_capa, sub_capa = map(int, input().split())

cnt = N
for i in range(N):
    #응시자 수에서 총감독관의 감독가능 수 빼기
    student_lst[i] -= head_capa
    #총감독관이 감독할 수 잇는 수를 뺀 후, 남아있는 응시자 수가 '+' 인 경우
    if student_lst[i] > 0:
        #부감독관 수로 나누었을 때 딱 떨어지는 경우
        if student_lst[i] % sub_capa == 0:
            cnt += (student_lst[i] // sub_capa)
        #나머지가 생기는 경우는 +1
        else:
            cnt += (student_lst[i] // sub_capa) +1

print(cnt)