

def solution(A):
    if len(A) > 1:
        A.sort()
        counter = A[0]
        for element in A:
            if element != counter:
                return counter
            else:
                counter += 1
    else:
        return 0
