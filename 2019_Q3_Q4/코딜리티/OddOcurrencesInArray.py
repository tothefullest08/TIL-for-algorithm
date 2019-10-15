# 비어있지 않는 배열 A, N개의 정수갯수로 구성됨
# A 배열은 홀수로만 구성되어 있음
# 배열 내 값들은 같은 값을 가진 다른 배열과 쌍을 이룰 수 있음
# (하나 남았을 경우 제외)

def solution(A):
    if len(A) == 1:
        return A[0]
    sorted(A)
    for i in range(0, len(A), 2):
        if i+1 == len(A):
            return A[i]
        if A[i] != A[i+1]:
            return A[i]


def solution(A):     
    if len(A) == 1:
         return A[0]
    A = sorted(A)       # O(n*log(N) or N)
    for i in range(0 , len (A) , 2): # O(N)
         if i+1 == len(A):
             return A[i]
         if A[i] != A[i+1]:
             return A[i]
print(solution([1,2,3,4,5]))