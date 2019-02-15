

def solution(A, B, K):
    print(A, B, K, '= ', end='')

    amod, bmod = 0, 0

    difference = B - A

    if A % K == 0:
        amod = 1
    if B % K == 0 and difference != 0:
        bmod = 1

    if difference == 0 and amod == 1:
        return 1

    if K >= B:
        return amod + bmod
    else:
        return None

print(solution(0,1,1))
print(solution(1,1,1))
print(solution(0,2,2))
print(solution(0,2,3))
print(solution(2,2,1))
print(solution(9,9,1))
print(solution(1,2,1))