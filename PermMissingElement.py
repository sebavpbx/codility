

def solution(A):

    if len(A) == 0:
        return 1

    elif len(A) == 1:
        if A[0] == 1:
            return 2
        elif A[0] == 0:
            return 1
        else:
            return A[0] - 1
    else:
        A.sort()
        counter = 1
        for number in A:
            if number != counter:
                return counter
            else:
                counter += 1
        return A[len(A) - 1] + 1
