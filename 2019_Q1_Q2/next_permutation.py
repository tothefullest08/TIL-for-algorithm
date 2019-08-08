# 3 2 5 4 1
# 3 4 1 2 5


Data = list(map(int, input().split()))
N = len(Data)

cand1 = 0
for i in range(N-1):
    if Data[i] < Data[i+1]:
        cand1 = i

cand2 = N-1
while True:
    cand2 -=1
    if Data[cand1] > Data[cand2]:
        break

Data[cand1], Data[cand2] = Data[cand2], Data[cand1]
Data[cand1+1:] = Data[:cand1:-1]


if cand1 == 0:
    print("다음 순열이 없습니다")
else:
    print(Data)


