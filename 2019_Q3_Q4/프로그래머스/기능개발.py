# 기능 개선 작업 중. 기능은 진도가 100% 일 때 서비스 반영 가능
# 각 기능의 개발속도가 모두 다름. 뒤에 기능이 먼저 개발 될 수 잇음. 뒷 기능은 앞에 기능이 배포될때 함께 배포됨
# 먼저 배포되어야하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발속도가 적힌 spppeds
# 각 배포마다 몇개의 기능이 배포되는지 리턴하는 함수 완성할 것
# 작업의 갯수는 100개 이하
# 작업의 진도는 100 미만 자연수
# 작업의 속도는 100 이하 자연수
# 배포는 하루에 1번만 가능. 하루 끝에 이루어 짐. 진도율 95%인 작업의 개발속도가 하루에 4%라면 2일뒤에 이루어짐

def solution(progresses, speeds):

    Q = []
    answer = []
    for i in progresses:
        Q.append(i)

    while Q:
        #기능 개선
        for i in range(len(Q)):
            Q[i] += speeds[i]

        cnt = 0
        while True:
            if not Q or Q[0] < 100:
                break

            if Q[0] >= 100:
                cnt += 1
                Q.pop(0)
                speeds.pop(0)

        if cnt > 0:
            answer.append(cnt)

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))
# speeds 만큼 더해서 올라갈 것
#