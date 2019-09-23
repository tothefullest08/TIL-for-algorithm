import sys
sys.stdin = open('코니와문의술래잡기.txt', 'r')

# 가로, 세로 각각 n, m  모눈종이에서 코니와 문이 술래잡기 중
# 코니가 (x,y)위치로 도망간뒤 문이 코니를 가장 빨리 잡을 수 있는 경우의 수는?
# 코니는 도망간 후 이동하지 않음
# 문은 (0,0) 지저메서 게임 시작
# 문은 가로, 세로로만 이동 가능
# 한칸 이동 시 1초의 시간이 필요
# 코니가 모눈종이 공간 밖으로 도망간 경우, 문은 코니를 잡을 수 없음
# 모눈종이의 공간 n, m크기는 1~24

map_x, map_y = map(int, input().split())
cony_x, cony_y = map(int, input().split())

def fact(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


if (cony_x < 0 and cony_x > map_x) or (cony_y < 0 and cony_y > map_y):
    print('fail')
else:
    time = cony_x + cony_y
    case_num = fact(cony_x + cony_y) // (fact(cony_x)*fact(cony_y))

    print(time)
    print(case_num)


