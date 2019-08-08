Data = [55, 7, 78, 12, 42]
N = len(Data)

#i는 왼쪽저울의 위치. 데이터의 길이가 N개일 경우, 왼쪽 저울의 Max 위치는 N-1임
for i in range(N-1):
    for j in range(i, N-1):
        print(Data)
        if Data[j] > Data[j+1]:
            Data[j], Data[j+1] = Data[j+1], Data[j]
        print(Data)
    print(Data)


for i in range(N-1, 0, -1):
    for j in range(0, i):
        print(Data)
        if Data[j] > Data[j+1]:
            Data[j], Data[j+1] = Data[j+1], Data[j]
        print(Data)
    print(Data)