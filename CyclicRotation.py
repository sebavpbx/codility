

def solution(A, K):

    if len(A) > 0:
        for x in range(K):
            A.insert(0, A.pop(len(A) - 1))
    return A
