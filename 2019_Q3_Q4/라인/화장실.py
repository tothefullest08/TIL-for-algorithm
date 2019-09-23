import sys
sys.stdin = open('화장실.txt', 'r')

# 부정행위 일어날까 시험장 구석구석
# 화장실 공유?
# 모든 지원자들을 서로 다른 화장실로 보낼 수 있음
# 지원자의 수와 지원자들이 화장실에 간 시간과 화장실에서 돌아온 시간의 목록을 주어졌을 떄,
# 모든 지원자들이 서로 다른 화장실에 들어갈 수 있는 최소 갯수


N = int(input())
toilet_info = [list(map(int, input().split())) for i in range(N)]
toilet_info.sort(key=lambda x:x[0])
toilet_array = []
toilet_array.append(toilet_info.pop(0))
start_time = toilet_array[0][0]

while True:
    start_time += 1
    for i in range(len(toilet_array)):
        if toilet_array[i] != [0, 0]:
            toilet_array[i][1] -= 1

    for i in range(len(toilet_array)):
        if toilet_array[i][0] == toilet_array[i][1]:
            toilet_array[i] = [0, 0]

    flag1 = False
    if toilet_info and start_time == toilet_info[0][0]:
        for i in range(len(toilet_array)):
            if toilet_array[i] == [0, 0]:
                a, b = toilet_info.pop(0)
                toilet_array[i] = [a, b]
                flag1 = True

    if toilet_info:
        if start_time == toilet_info[0][0] and flag1 == False:
            toilet_array.append(toilet_info.pop(0))

    flag = True
    if not toilet_info:
        for i in range(len(toilet_array)):
            if toilet_array[i] != [0, 0]:
                flag = False

        if flag == True:
            break


print(len(toilet_array))

