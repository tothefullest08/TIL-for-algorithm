Data = list(map(int, input("입력하세요: ").split()))
N = len(Data)
cnt_lst = [0] * 12

for i in range(N):
    cnt_lst[Data[i]] += 1

result = run = triple = i = 0

while True:
    if cnt_lst[i] + cnt_lst[i + 1] + cnt_lst[i + 2] == 3:
        cnt_lst[i] -= 1
        cnt_lst[i + 1] -= 1
        cnt_lst[i + 2] -= 1
        run += 1
        # continue

    if cnt_lst[i] >= 3:
        cnt_lst[i] -= 3
        triple += 1
        # continue

    i += 1

    if i == 10:
        break

if run + triple == 2:
    print("baby jin")

else:
    print("failed")
