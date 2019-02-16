
def solution(A):
    A.sort()
    if len(A) > 1:
        for i in range(0, len(A), 2):
            if i == len(A) - 1:
                return A[i]
            elif A[i] != A[i + 1]:
                return A[i]
    else:
        return A[0]

