# 여러개의 쇠막대기를 레이저로 절단
# 효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐놓고 레이저를 수직으로 발사해서 쇠막대기를 자름.

# 조건
# 1. 쇠막대기는 자기보다 긴 막대기 위에만 놓일 수 있음
# 2. 쇠막대기를 다른 쇠막대기 위에 놓는 경우, 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓음
# 3. 각 쇠막대기를 자르는 레이저는 적어도 하나 존재함
# 4. 레이저는 어떤 쇠막대기의 양끝점과도 겹치지 않음

# 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍으로 표현함. 또한 모든 ()는 반드시 레이저를 쏘아야함
# 쇠막대기의 왼쪽 끝은 여는 괄호 ( 로, 오른쪽 끝은 닫는 괄호)로 표현함



def solution(arrangement):
    arrangement = arrangement.replace("()","L")
    stack = []
    answer = 0
    arrangement = list(arrangement)
    for i in arrangement:
        if i == '(':
            stack.append(i)
            answer += 1
        elif i == ')':
            stack.pop()
        elif i == "L":
            answer += len(stack)



    return answer

arrangement = "()(((()())(())()))(())"
print(solution(arrangement))