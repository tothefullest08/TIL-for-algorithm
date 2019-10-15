# N개의 갯수로 구성된 A 배열
# 배열의 회전 = 인덱스 오른쪽으로 이동. 젤 끝에 거는 처음인덱스로감

def solution(A, K):
    N = len(A)
    if N == 0:
        return A
    for j in range(K):
        end_num = A[-1]
        for i in range(N-2, -1, -1):
            A[i+1] = A[i]
        A[0] = end_num

    return A




A = [3,8,9,7,6]
K = 3
print(solution(A, K))
