# 프린터 - 인쇄 요청이 들어온 순서대로 인쇄. => 중요문서가 나중에 인쇄 될 수 이씀
# 본완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터 개발
# 인쇄 작업 방식
# 1. 인쇄 대기목록의 가장 앞의 문서(j)를 대기목룍에서 꺼냄
# 2. 나머지 인쇄 대기목록에서 j보다 중요도가 높은 문서가 한개라도 존재하면 j를 대기목록의 마지막에 넣음
# 3. 그렇지 않으면 j를 인쇄
# 내가 인쇄를 요청한 문서가 몇번째에 인쇄되는지


def solution(priorities, location):
    printed_lst= []
    answer = 0
    while print_lst:
        current_priority, current_idx = print_lst.pop(0)
        for i in range(len(print_lst)):
            next_priority, next_idx = print_lst[i]
            if current_priority >= next_priority:
                continue
            else:
                print_lst.append([current_priority, current_idx])
                break

        if print_lst and print_lst[-1] != [current_priority, current_idx]:
            printed_lst.append([current_priority, current_idx])
            if current_idx == location:
                answer = len(printed_lst)
                break
        if not print_lst:
            printed_lst.append([current_priority, current_idx])
            if current_idx == location:
                answer = len(printed_lst)
                break
    return answer



# TC.1
# priorities = [2, 1, 3, 2]
# location = 2

# TC.2
priorities = [1, 1, 9, 1, 1, 1]
location = 0

N = len(priorities)
print_lst = []
for i in range(N):
    print_lst.append([priorities[i], i])
print(print_lst)
print(solution(priorities, location))