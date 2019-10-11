# 학기 끝. 점수에 따라 랭킹이 매겨져있음
# 교장은 특정 등급이상인 학생들에게 상을 주려고 함
# 동일한 점수일 경우 동일한 등급을 줌.
# 그러나 다음 등급은 전체 학생 점수 리스트 내의 포지션에따라 마킹됨

# marks = [100, 50, 50, 25]
# ranks = [1,2,2,4]

import sys
sys.stdin = open('consolation_prize.txt','r')

def numofPrizes(k, marks):

    marks.sort(reverse=True) # 점수를 내림차순으로 정렬
    rank = [x for x in range(1, N+1)] # 등수 배열 생성

    for i in range(N-1):
        if rank[i] > k: # k 등수보다 더 낮은 등수일 경우 종료 조건
            break

        # marks 배열에서 그다음 점수가 자기 점수와 같을 경우
        # 그다음 등수를 자기 등수로 변경 (공동 등수 설정)
        if marks[i] == marks[i+1]:
            rank[i+1] = rank[i]

    count = 0
    for i in range(N):
        # k 등수 내 사람 수 count // 0점 이상인 경우만 count 조건 추가
        if rank[i] <= k and marks[i] > 0:
            count += 1

    return count

k = int(input())
N = int(input())
marks = [int(input()) for x in range(N)]
print(marks, k)
print(numofPrizes(k, marks))
