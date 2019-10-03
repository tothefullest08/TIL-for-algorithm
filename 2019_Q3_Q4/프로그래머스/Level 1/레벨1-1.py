
def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

def LCM(a,b,c):
    return a*b // c

def solution(n, m):

    gcd = GCD(n,m)
    lcm = LCM(n, m ,gcd)
    answer = [gcd, lcm]

    return answer

#36 24
#24 12


n = 6
m = 10
print(solution(n, m))


# a = 6  b = 10
# a = 10, b = 4
# a = 4, b = 2
# a = 2, b= 0


